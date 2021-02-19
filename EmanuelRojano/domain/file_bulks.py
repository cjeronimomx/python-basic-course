import os
from config import logs

log = logs.config_loggin()


def read_last_bulk():
    """
    This function gets the last bulk id (last line)
    """
    # r=read, w=write, a=append
    try:
        with open(os.getenv("BULKS_FILE"), "r") as file:
            return file.readlines()[-1]
    except FileNotFoundError as ex:
        log.error(ex.strerror)


def writte_bulk_id(id):
    """
    This function appends the bulk_id in the bulks.txt file
    """
    with open(os.getenv("BULKS_FILE"), "a") as file:
        file.write('\n'+id)

