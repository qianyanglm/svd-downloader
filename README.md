需要数据集发我谷歌邮箱，我会回复邮件的。

# svd-downloader

This repo allows downloading the entire Saarbruecken Voice Database，based on this repository(https://github.com/rijulg/svd-downloader)
此存储库允许下载整个萨尔布吕肯语音数据库。以这个仓库为基础 (https://github.com/rijulg/svd-downloader).


I changed part of it, and then you can run it directly in pycharm instead of running it in the command line (I personally don't like the command line), that is, you don't need to enter parameters, just run the _main_.py file directly. (At this time, an svd_downloader folder will be automatically generated in the current code directory to save the data set file)
The second modification is to add a request header to the downloader.
py file. Without adding the request header, an error will be reported every time 10% of the download is downloaded. After adding it, there may still be an error, but you can download more and then report an error, such as downloading to 30% before reporting an error, instead of reporting an error every time 10% or so. In addition, if the code reports an error and pauses, just rerun it directly, no need to modify anything.
I also added an error reporting mechanism, which can automatically reapply several times, so that there will be no error. From yesterday's experiment, it can download up to 100% of the data, and automatically disconnect when downloading half of it. I have tried it twice, and I can download 100% of the data every time.
Finally, the data downloaded by this code is not classified by disease name, but by health and disease, and then classified into men and women. This should be noted.

我改动了一部分，可以直接在pycharm运行，而不是在命令行运行(个人不喜欢命令行)，即不用输入参数，直接运行_main_.py文件即可。（此时会在当前代码目录自动生成一个svd_downloader文件夹来保存数据集文件）
其次修改的地方在downloader. py文件添加了一个请求头，不添加请求头每次下载10%几就会报错，添加以后也有可能会报错，但是可以下载的多一点再报错，比如下载到30
%才报错，而不是每次都10%几就报错。另外如果代码报错暂停了，直接重新运行就行了，不需要修改啥。




我又添加了一个报错机制，可以自动重新申请几次，这样就不会报错了，昨天实验来看，可以一直下载到100 %的数据，下载到一小半自动断掉。我已经实验了两次，都可以每次下载100%数据。

最后是这个代码下载的数据不是以疾病名称分类，而是以健康和疾病，其下再分类男女的分类方式，这点要注意。
## Requirements

    - beautifulsoup4
    - dask

## Running
直接运行_main_.py文件

## Question
有啥问题在仓库的issue那里提，我只要在线就会看

## License

This project itself is licensed under the [MIT License](./LICENSE), but the dataset that will be downloaded is licensed licensed under [SVD dataset License](LICENSE).

