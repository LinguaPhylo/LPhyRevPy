import getopt
import sys
from typing import List

from lphy.core.parser.LPhyCanonicalBuilder import LPhyCanonicalBuilder
from lphy.core.parser.RevBuilder import RevBuilder
from lphy.core.parser.LPhyParserDictionary import LPhyParserDictionary


def parse_args(argv):
    inputfile = ''
    outputfile = ''
    chainlen = ''
    burnin = ''
    HELP_MSG = 'test.py -i <inputfile> -o <outputfile> -l <chainlength> -b <chainlen>'
    try:
        opts, args = getopt.getopt(argv, "hi:o:l:b:", ["ifile=", "ofile=", "chainlen", "burnin"])
    except getopt.GetoptError:
        print(HELP_MSG)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(HELP_MSG)
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-l", "--chainlen"):
            chainlen = arg
        elif opt in ("-b", "--burnin"):
            burnin = arg
    argsdict = {"in": inputfile, "out": outputfile, "chainlen": chainlen, "burnin": burnin}
    return argsdict


def parse_arg_to_number(arg_val, message, args_builder: List):
    if arg_val:
        try:
            if '.' in arg_val:
                arg_val = float(arg_val)  # Try to convert to a float
            else:
                arg_val = int(arg_val)  # Try to convert to an integer
            # add to args_builder
            args_builder.append(arg_val)
            print(message, arg_val)
        except ValueError:
            pass  # do nothing


def main():
    argsdict = parse_args(sys.argv[1:])

    in_file = argsdict["in"]
    print('Input file is : ', in_file)
    args_builder = [in_file]

    out_file = argsdict["out"]
    print('Output file is : ', out_file)
    # TODO  out ...

    parse_arg_to_number(argsdict["chainlen"], 'Set MCMC chain length = ', args_builder)
    parse_arg_to_number(argsdict["burnin"], 'Set burn-in = ', args_builder)

    # Read input file
    with open(in_file, 'r') as f:
        input_string = f.read()
    # print lphy script
    print(input_string)

    parser_dict = LPhyParserDictionary()
    # TODO why need LPhyMetaParser.DATA and MODEL, parser seems already handled
    # parser_dict.parse(data_string, LPhyMetaParser.DATA)
    parser_dict.parse(input_string)

    # code_builder = LPhyCanonicalBuilder()
    # code = code_builder.get_code(parser_dict)

    # print("\nReconstruct LPhy script below:\n")
    # print(code)

    rev_builder = RevBuilder(*args_builder)
    rev = rev_builder.get_code(parser_dict)

    print("\nConvert to the Rev script below:\n")
    print(rev)


if __name__ == "__main__":
    print('Argument List:', str(sys.argv))

    main()
