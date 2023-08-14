import argparse
import sys

from lphy.core.parser.LPhyMetaParser import LPhyMetaParser


def main():
    parser = argparse.ArgumentParser(description="LPhy Parser")
    parser.add_argument("filename", help="Name of the input file")
    args = parser.parse_args()

    if args.filename:
        with open(args.filename, "r") as fin:
            input_string = fin.read()

    # Rev: theta ~ dnNormal(3.0, 1.0)
    input_string = "Θ ~ LogNormal(meanlog=3.0, sdlog=1.0);"

    meta_parser = LPhyMetaParser()
    meta_parser.parse(input_string, LPhyMetaParser.MODEL)


if __name__ == "__main__":
    print('Argument List:', str(sys.argv))

    main()
