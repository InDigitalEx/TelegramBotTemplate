import logging

from app import start_bot
from utils import get_root_dir


def init_logger() -> None:
    logger = logging.getLogger()
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

    file_handler = logging.FileHandler(f"{get_root_dir()}/logs/debug.log", mode='a')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    logger.setLevel(logging.DEBUG)


def main() -> None:
    init_logger()
    start_bot()


if __name__ == "__main__":
    main()
