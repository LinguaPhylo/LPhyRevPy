import logging
import sys

from lphy.core.parser.LPhyCanonicalBuilder import LPhyCanonicalBuilder
from lphy.core.parser.RevBuilder import RevBuilder


def main():
    logging.basicConfig(level=logging.DEBUG)

    from lphy.core.parser.LPhyMetaParser import LPhyMetaParser

    # TODO inline func
    input_string = ("data {\n  L = 200;\n  taxa = taxa(names=1:10);\n}\n"
                    "model {\n  Θ ~ LogNormal(meanlog=3.0, sdlog=1.0);\n"
                    "  ψ ~ Coalescent(theta=Θ, taxa=taxa);\n"
                    "  D ~ PhyloCTMC(tree=ψ, L=200, Q=jukesCantor());\n}\n")

    meta_parser = LPhyMetaParser()
    meta_parser.parse(input_string)

    code_builder = LPhyCanonicalBuilder()
    code = code_builder.get_code(meta_parser)

    print(code)

    rev_builder = RevBuilder()
    rev = rev_builder.get_code(meta_parser)

    print(rev)



if __name__ == "__main__":
    print('Argument List:', str(sys.argv))

    main()
