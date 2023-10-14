# svd-downloader

This repo allows downloading the entire Saarbruecken Voice Database.
此存储库允许下载整个萨尔布吕肯语音数据库。
以这个仓库为基础 (https://github.com/rijulg/svd-downloader), 
我只是简单的改动了一点，然后可以直接在pycharm运行，而不是在命令行运行(个人不喜欢命令行)，即不用输入参数，直接运行_main_.
py文件即可。（此时会在当前代码目录自动生成一个svd_downloader文件夹来保存数据集文件）
其次修改的地方在downloader.
py文件添加了一个请求头，不添加请求头每次下载10%几就会报错，添加以后也有可能会报错，但是可以下载的多一点再报错，比如下载到30%才报错，而不是每次都10%几就报错。另外报错后，直接重新运行就行了，不需要修改啥。
我又添加了一个报错机制，可以自动重新申请几次，这样就不会报错了，昨天实验来看，可以一直下载到100%的数据，下载到一小半自动断掉
## Requirements

    - beautifulsoup4
    - dask

## Running
直接运行_main_.py文件


## License

This project itself is licensed under the [MIT License](./LICENSE), but the dataset that will be downloaded is licensed licensed under [SVD dataset License](LICENSE).
