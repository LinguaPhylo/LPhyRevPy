from abc import abstractmethod

from antlr4 import InputStream, CommonTokenStream, ParseTreeVisitor

import DataModelLexer
import DataModelParser

import SimulatorLexer


class LPhyParserAction:

    @abstractmethod
    def parse(self, sentence):
        pass

    @abstractmethod
    def parse(self, sentence: str, visitor: ParseTreeVisitor, hasDataModelBlock: bool):
        # empty data block or model block
        if not str(sentence).endswith(";") and str(sentence).strip() != "":
            sentence = str(sentence) + ";"

        # TODO: add custom error listener

        # get lexer
        if hasDataModelBlock:
            lexer = DataModelLexer(InputStream(sentence))
        else:
            lexer = SimulatorLexer(InputStream(sentence))
        # add custom error listener to lexer

        # get tokens
        tokens = CommonTokenStream(lexer)

        if hasDataModelBlock:
            parser = DataModelParser(tokens)
            # add custom error listener
            parse_tree = parser.input()
