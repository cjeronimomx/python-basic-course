import argparse


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-p", "--pokemon", help="Pokemon Name or Number", required=False, type=str)

    return parser.parse_args()
