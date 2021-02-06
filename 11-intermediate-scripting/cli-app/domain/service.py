import psutil
from config import logs, database
from domain import repository

log = logs.config_loggin()

def print_cpu_info():
    log.info('===================================================================')
    log.info('[                     CPU Information summary                      ]')
    log.info('===================================================================')

    # gives a single float value
    vcc = psutil.cpu_count()
    log.info(f'Total number of CPUs: {vcc}')

    vcpu = psutil.cpu_percent()
    log.info(f'Total CPUs utilized percentage: {vcpu}%')

    db = database.connect()
    log.debug(f"DB -> {db}")
    key = repository.create_metric(db, {'vcc': vcc, 'vcpu': vcpu}, 'cpu')
    result = repository.read_metric(db, key, 'cpu')
    log.info(f"Metric persisted -> {result}")


def print_ram_info():
    log.info('===================================================================')
    log.info('[                     RAM Information summary                      ]')
    log.info('===================================================================')

    ram = dict(psutil.virtual_memory()._asdict())

    def forloop():
        for i in ram:
            log.info(f"{i}: {ram[i] / 1024 / 1024 / 1024}")  # Output will be printed in GBs
    forloop()