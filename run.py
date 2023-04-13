from loguru import logger

from bot import start_bot
from bot.misc import get_root_dir


def main() -> None:
    log_path = f"{get_root_dir()}/logs/debug.log"
    logger.add(log_path, format="{time} {level} {message}", level="DEBUG", rotation="10:00")
    start_bot()


if __name__ == "__main__":
    main()
