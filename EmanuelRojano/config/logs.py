import os
import logging


def config_loggin():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    log = logging.getLogger("migracion-binarios-app")
    file_log = logging.FileHandler(f'{os.getenv("LOG_PATH")}Logs.log')
    file_log.setLevel(logging.DEBUG)  # or any level you want
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_log.setFormatter(fmt=formatter)

    log.addHandler(file_log)
    return log