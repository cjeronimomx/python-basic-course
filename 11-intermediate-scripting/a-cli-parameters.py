import argparse


# python3 11-intermediate-scripting/a-cli-parameters.py -r all -u gb
# python3 11-intermediate-scripting/a-cli-parameters.py -r=all -u=gb
# python3 11-intermediate-scripting/a-cli-parameters.py --resource all --unit=gb
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--resource", help="Resource to monitor, options: ram,cpu,all", required=True)
    parser.add_argument("-u", "--unit", help="Measure unit", type=str, default='gb')

    args = parser.parse_args()
    resource = args.resource
    unit = args.unit

    print(args)