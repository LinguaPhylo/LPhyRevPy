import getopt
import sys

from antlr4 import *

from lphy.core.parser.LPhyMetaParser import LPhyMetaParser


def parse_args(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print('Input file is : ', inputfile)
    print('Output file is : ', outputfile)
    argsdict = {"in": inputfile, "out": "outputfile"}
    return argsdict


def main():
    argsdict = parse_args(sys.argv[1:])

    with open(argsdict["in"], 'r') as f:
        input_string = f.read()
    # print lphy script
    print(input_string)

    # empty data block or model block
    # if not str(sentence).endswith(";") and str(sentence).strip() != "":
    #   sentence = str(sentence) + ";"

    # Rev: theta ~ dnNormal(3.0, 1.0)
    input_string = "Θ ~ LogNormal(meanlog=3.0, sdlog=1.0);"

    meta_parser = LPhyMetaParser()
    meta_parser.parse(input_string, LPhyMetaParser.MODEL)


if __name__ == "__main__":
    print('Argument List:', str(sys.argv))

    main()
