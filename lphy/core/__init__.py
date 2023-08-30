import logging
import sys

from lphy.core.parser.CanonicalCodeBuilder import CanonicalCodeBuilder
from lphy.core.parser.RevBuilder import RevBuilder


def main():
    logging.basicConfig(level=logging.DEBUG)

    from lphy.core.parser.LPhyMetaParser import LPhyMetaParser

    # Rev: theta ~ dnNormal(3.0, 1.0)
    input_string = ("Θ ~ LogNormal(meanlog=3.0, sdlog=1.0);\n"
                    "ψ ~ Coalescent(theta=Θ, taxa=taxa(names=1:10));\n"
                    "D ~ PhyloCTMC(tree=ψ, L=200, Q=jukesCantor());")

    meta_parser = LPhyMetaParser()
    meta_parser.parse(input_string, LPhyMetaParser.MODEL)

    code_builder = CanonicalCodeBuilder()
    code = code_builder.get_code(meta_parser)

    print(code)

    rev_builder = RevBuilder()
    rev = rev_builder.get_code(meta_parser)

    print(rev)



if __name__ == "__main__":
    print('Argument List:', str(sys.argv))

    main()
