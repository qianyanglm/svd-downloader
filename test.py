import numpy as np
from numba import cuda

@cuda.jit
def gpu_matrix_multiply(A, B, C):
    row, col = cuda.grid(2)
    if row < C.shape[0] and col < C.shape[1]:
        temp = 0.0
        for k in range(A.shape[1]):
            temp += A[row, k] * B[k, col]
        C[row, col] = temp

def main():
    # 配置矩阵维度（约1.5GB/矩阵）
    matrix_size = 15000  # 调整此值至显存容量的70%左右
    dtype = np.float32

    try:
        # 预分配内存
        A = np.random.rand(matrix_size, matrix_size).astype(dtype)
        B = np.random.rand(matrix_size, matrix_size).astype(dtype)
        C = np.zeros((matrix_size, matrix_size), dtype=dtype)
    except MemoryError:
        print("内存不足，请减小matrix_size")
        return

    # CUDA配置（优化后的线程布局）
    threads_per_block = (32, 8)  # 256 threads/block
    blocks_x = (A.shape[0] + threads_per_block[0] - 1) // threads_per_block[0]
    blocks_y = (B.shape[1] + threads_per_block[1] - 1) // threads_per_block[1]

    # 显式内存管理
    stream = cuda.stream()
    try:
        d_A = cuda.to_device(A, stream=stream)
        d_B = cuda.to_device(B, stream=stream)
        d_C = cuda.device_array_like(C, stream=stream)
    except cuda.cudadrv.driver.CudaAPIError as e:
        print(f"显存不足: {e}")
        return

    # 执行内核
    gpu_matrix_multiply[(blocks_x, blocks_y), threads_per_block, stream](d_A, d_B, d_C)

    # 异步传输结果
    d_C.copy_to_host(C, stream=stream)
    stream.synchronize()

if __name__ == "__main__":
    main()
import numpy as np
from numba import cuda

# 使用之前定义的GPU矩阵乘法函数
@cuda.jit
def gpu_matrix_multiply(A, B, C):
    row, col = cuda.grid(2)
    if row < C.shape[0] and col < C.shape[1]:
        temp = 0
        for k in range(A.shape[1]):
            temp += A[row, k] * B[k, col]
        C[row, col] = temp

# 初始化数据
A = np.random.rand(3, 3).astype(np.float32)
B = np.random.rand(3, 3).astype(np.float32)
C = np.zeros((3, 3), dtype=np.float32)

# 配置CUDA线程
threads_per_block = (16, 16)
blocks_per_grid_x = (A.shape[0] + threads_per_block[0] - 1) // threads_per_block[0]
blocks_per_grid_y = (B.shape[1] + threads_per_block[1] - 1) // threads_per_block[1]
blocks_per_grid = (blocks_per_grid_x, blocks_per_grid_y)

# 传输数据到设备
d_A = cuda.to_device(A)
d_B = cuda.to_device(B)
d_C = cuda.to_device(C)

# 启动内核
gpu_matrix_multiply[blocks_per_grid, threads_per_block](d_A, d_B, d_C)

# 取回结果
d_C.copy_to_host(C)

# 验证结果（可选）
expected = np.dot(A, B)
print("GPU结果与CPU结果是否一致:", np.allclose(C, expected, atol=1e-5))
