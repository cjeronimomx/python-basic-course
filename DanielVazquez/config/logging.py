import os
import logging


def config_logger():
    log = logging.getLogger("poke-app")
    log.setLevel(logging.DEBUG)

    console_formatter = logging.Formatter('%(name)s: %(message)s')
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setLevel(os.getenv("LOG_LEVEL"))
    console_handler.setFormatter(console_formatter)

    file_handler = logging.FileHandler(f'{os.getenv("LOG_PATH")}')
    file_handler.setLevel(level=logging.DEBUG)
    file_handler.setFormatter(file_formatter)

    if log.hasHandlers():
        log.handlers.clear()

    log.addHandler(file_handler)
    log.addHandler(console_handler)

    return log



