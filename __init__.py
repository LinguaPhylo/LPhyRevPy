import getopt
import sys

from lphy.core.parser.LPhyCanonicalBuilder import LPhyCanonicalBuilder
from lphy.core.parser.RevBuilder import RevBuilder
from lphy.core.parser.LPhyParserDictionary import LPhyParserDictionary


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

    # we can create a dummy vector of Taxon objects for simulation
    # for (i in 1:10) { taxa[i] = taxon("Taxon"+i) }
    # data_string = ("L = 200;\n"
    #                "taxa = taxa(names=1:10);\n")
    # model_string = ("Θ ~ LogNormal(meanlog=3.0, sdlog=1.0);\n"
    #                 "ψ ~ Coalescent(theta=Θ, taxa=taxa);\n"
    #                 "Q=jukesCantor();\n"
    #                 "D ~ PhyloCTMC(tree=ψ, L=L, Q=Q);")

    parser_dict = LPhyParserDictionary()
    #TODO why need LPhyMetaParser.DATA and MODEL, parser seems already handled
    # parser_dict.parse(data_string, LPhyMetaParser.DATA)
    parser_dict.parse(input_string)

    #code_builder = LPhyCanonicalBuilder()
    #code = code_builder.get_code(parser_dict)

    #print("\nReconstruct LPhy script below:\n")
    #print(code)

    rev_builder = RevBuilder()
    rev = rev_builder.get_code(parser_dict)

    print("\nConvert to the Rev script below:\n")
    print(rev)


if __name__ == "__main__":
    print('Argument List:', str(sys.argv))

    main()
