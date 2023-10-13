import sys
import logging
from argparse import ArgumentParser
from downloader import Downloader


def get_logger():
    log_handler = logging.StreamHandler(sys.stdout)
    log_formatter = logging.Formatter(
        fmt="[%(asctime)s] %(levelname)-8s:: %(message)s")
    log_handler.setFormatter(log_formatter)

    logger = logging.Logger("SVD Downloader")
    logger.addHandler(log_handler)
    return logger


if __name__ == "__main__":
    parser = ArgumentParser("SVD Downloader")
    # 修改处，添加了一个默认参数
    parser.add_argument("--out_path", type=str,
                        default=r'svd_downloader', help=("The location of "
                                                        "where to store data"))
    parser.add_argument("--refetch-links", action='store_true', help="Whether to refresh the list of links")
    args = parser.parse_args()

    logger = get_logger()
    downloader = Downloader(
        out_path=args.out_path,
        refetch_links=args.refetch_links,
        logger=logger
    )
    downloader.run()
