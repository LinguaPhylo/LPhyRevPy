import logging
import sys


def main():
    logging.basicConfig(level=logging.DEBUG)

    from lphy.core.parser.LPhyMetaParser import LPhyMetaParser

    # Rev: theta ~ dnNormal(3.0, 1.0)
    input_string = "Θ ~ LogNormal(meanlog=3.0, sdlog=1.0);"

    meta_parser = LPhyMetaParser
    meta_parser.parse(input_string, LPhyMetaParser.MODEL)


if __name__ == "__main__":
    print('Argument List:', str(sys.argv))

    main()
