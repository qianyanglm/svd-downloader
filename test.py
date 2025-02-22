import numpy as np
from numba import cuda
import math
import time

#  创建一个更复杂的矩阵乘法
@cuda.jit
def gpu_matrix_multiply(A, B, C):
    # 计算线程的二维索引
    row, col = cuda.grid(2)

    if row < C.shape[0] and col < C.shape[1]:
        temp = 0
        for k in range(A.shape[1]):
            temp += A[row, k] * B[k, col]
        C[row, col] = temp

# 设置更大的矩阵维度（例如 16384）
n = 4096*2  # 增大矩阵大小到 16384x16384
A = np.random.random((n, n)).astype(np.float64)  # 使用 float64 增加内存占用
B = np.random.random((n, n)).astype(np.float64)  # 使用 float64 增加内存占用
C = np.zeros((n, n), dtype=np.float64)  # 使用 float64 增加内存占用

# 将数据传输到设备
A_device = cuda.to_device(A)
B_device = cuda.to_device(B)
C_device = cuda.to_device(C)

# 设置线程块和网格的大小
threadsperblock = (32, 32)
blockspergrid = (math.ceil(n / threadsperblock[0]), math.ceil(n / threadsperblock[1]))

# 记录开始时间
start_time = time.time()

# 调用 GPU 进行矩阵乘法
gpu_matrix_multiply[blockspergrid, threadsperblock](A_device, B_device, C_device)

# 将结果从 GPU 拷贝回主机
C_device.copy_to_host(C)

# 记录结束时间
end_time = time.time()

# 打印计算时间
print(f"Matrix multiplication completed in {end_time - start_time:.4f} seconds.")
