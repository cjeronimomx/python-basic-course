"""
1.-  pip install -r 11-intermediate-scripting/cli-app/requirements.txt
2.- Create .env file
3.- Crear function load_args
4.- Implement entry point
5.- Call load_dotenv()
5.- Create config and domnain package
6.- Create logs and service module
7.- import modules: logs and service
8.- Configure loggin in module logs
9.- Implement and call print_cpu_info() in service module
10.- Implement and call print_ram_info() in service module
11.- add if-elif-else for call functions in entrypoint block
12.- Create database and repository module in domain package
13.- Implement connect function in database module
14.- Implement write function in repository module
15.- Call write function in service module
16.- Implement and call read function in repository module
"""
import argparse
import datetime
from dotenv import load_dotenv
from config import logs
from domain import service


def load_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--resource", help="Resource to monitor, options: ram,cpu,all", required=True)
    parser.add_argument("-u", "--unit", help="Measure unit", type=str, default='gb')
    return parser.parse_args()


if __name__ == "__main__":
    args = load_args()
    load_dotenv()
    log = logs.config_loggin()

    log.debug(f"App started at: {datetime.datetime.now()} with Args: {args} ")

    if args.resource == "cpu":
        service.print_cpu_info()
    elif args.resource == "ram":
        service.print_ram_info()
    else:
        service.print_cpu_info()
        service.print_ram_info()
