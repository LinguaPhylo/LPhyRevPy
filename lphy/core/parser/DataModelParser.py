# Generated from LPhyRevPy/lphy/core/parser/DataModel.g4 by ANTLR 4.12.0
# encoding: utf-8

from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,51,279,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,3,0,54,
        8,0,1,0,3,0,57,8,0,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,3,3,67,8,3,1,
        3,1,3,1,4,1,4,3,4,73,8,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,5,5,82,8,5,
        10,5,12,5,85,9,5,1,6,1,6,1,6,1,6,1,6,5,6,92,8,6,10,6,12,6,95,9,6,
        1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,109,8,8,1,9,
        1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,
        12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,3,14,137,
        8,14,1,15,1,15,1,15,5,15,142,8,15,10,15,12,15,145,9,15,1,16,1,16,
        3,16,149,8,16,1,17,3,17,152,8,17,1,17,1,17,1,18,1,18,1,18,5,18,159,
        8,18,10,18,12,18,162,9,18,1,19,1,19,1,19,5,19,167,8,19,10,19,12,
        19,170,9,19,1,20,1,20,1,20,1,20,1,21,1,21,1,21,3,21,179,8,21,1,21,
        1,21,1,21,1,21,3,21,185,8,21,1,21,3,21,188,8,21,1,22,1,22,1,22,1,
        22,1,22,3,22,195,8,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,24,1,
        24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,
        25,1,25,1,25,1,25,1,25,1,25,3,25,224,8,25,1,25,1,25,1,25,1,25,1,
        25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,240,8,25,1,
        25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,
        25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,
        25,1,25,1,25,1,25,1,25,1,25,5,25,274,8,25,10,25,12,25,277,9,25,1,
        25,0,3,10,12,50,26,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,38,40,42,44,46,48,50,0,8,2,0,8,8,37,37,3,0,13,14,40,42,44,
        46,2,0,12,12,15,17,1,0,18,21,2,0,12,12,17,17,1,0,22,25,1,0,26,27,
        1,0,15,16,292,0,53,1,0,0,0,2,58,1,0,0,0,4,61,1,0,0,0,6,64,1,0,0,
        0,8,70,1,0,0,0,10,76,1,0,0,0,12,86,1,0,0,0,14,96,1,0,0,0,16,108,
        1,0,0,0,18,110,1,0,0,0,20,113,1,0,0,0,22,120,1,0,0,0,24,122,1,0,
        0,0,26,126,1,0,0,0,28,136,1,0,0,0,30,138,1,0,0,0,32,148,1,0,0,0,
        34,151,1,0,0,0,36,155,1,0,0,0,38,163,1,0,0,0,40,171,1,0,0,0,42,187,
        1,0,0,0,44,189,1,0,0,0,46,198,1,0,0,0,48,203,1,0,0,0,50,223,1,0,
        0,0,52,54,3,2,1,0,53,52,1,0,0,0,53,54,1,0,0,0,54,56,1,0,0,0,55,57,
        3,4,2,0,56,55,1,0,0,0,56,57,1,0,0,0,57,1,1,0,0,0,58,59,5,34,0,0,
        59,60,3,8,4,0,60,3,1,0,0,0,61,62,5,35,0,0,62,63,3,6,3,0,63,5,1,0,
        0,0,64,66,5,1,0,0,65,67,3,10,5,0,66,65,1,0,0,0,66,67,1,0,0,0,67,
        68,1,0,0,0,68,69,5,2,0,0,69,7,1,0,0,0,70,72,5,1,0,0,71,73,3,12,6,
        0,72,71,1,0,0,0,72,73,1,0,0,0,73,74,1,0,0,0,74,75,5,2,0,0,75,9,1,
        0,0,0,76,77,6,5,-1,0,77,78,3,16,8,0,78,83,1,0,0,0,79,80,10,1,0,0,
        80,82,3,16,8,0,81,79,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,
        0,0,0,84,11,1,0,0,0,85,83,1,0,0,0,86,87,6,6,-1,0,87,88,3,14,7,0,
        88,93,1,0,0,0,89,90,10,1,0,0,90,92,3,14,7,0,91,89,1,0,0,0,92,95,
        1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,13,1,0,0,0,95,93,1,0,0,0,
        96,97,3,24,12,0,97,98,5,3,0,0,98,15,1,0,0,0,99,100,3,26,13,0,100,
        101,5,3,0,0,101,109,1,0,0,0,102,103,3,24,12,0,103,104,5,3,0,0,104,
        109,1,0,0,0,105,106,3,18,9,0,106,107,5,3,0,0,107,109,1,0,0,0,108,
        99,1,0,0,0,108,102,1,0,0,0,108,105,1,0,0,0,109,17,1,0,0,0,110,111,
        3,20,10,0,111,112,3,6,3,0,112,19,1,0,0,0,113,114,5,4,0,0,114,115,
        5,5,0,0,115,116,5,36,0,0,116,117,5,6,0,0,117,118,3,32,16,0,118,119,
        5,7,0,0,119,21,1,0,0,0,120,121,7,0,0,0,121,23,1,0,0,0,122,123,3,
        28,14,0,123,124,3,22,11,0,124,125,3,50,25,0,125,25,1,0,0,0,126,127,
        3,28,14,0,127,128,5,48,0,0,128,129,3,46,23,0,129,27,1,0,0,0,130,
        137,5,36,0,0,131,132,5,36,0,0,132,133,5,9,0,0,133,134,3,30,15,0,
        134,135,5,10,0,0,135,137,1,0,0,0,136,130,1,0,0,0,136,131,1,0,0,0,
        137,29,1,0,0,0,138,143,3,50,25,0,139,140,5,11,0,0,140,142,3,50,25,
        0,141,139,1,0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,143,144,1,0,0,
        0,144,31,1,0,0,0,145,143,1,0,0,0,146,149,1,0,0,0,147,149,3,50,25,
        0,148,146,1,0,0,0,148,147,1,0,0,0,149,33,1,0,0,0,150,152,5,12,0,
        0,151,150,1,0,0,0,151,152,1,0,0,0,152,153,1,0,0,0,153,154,7,1,0,
        0,154,35,1,0,0,0,155,160,3,48,24,0,156,157,5,11,0,0,157,159,3,48,
        24,0,158,156,1,0,0,0,159,162,1,0,0,0,160,158,1,0,0,0,160,161,1,0,
        0,0,161,37,1,0,0,0,162,160,1,0,0,0,163,168,3,50,25,0,164,165,5,11,
        0,0,165,167,3,50,25,0,166,164,1,0,0,0,167,170,1,0,0,0,168,166,1,
        0,0,0,168,169,1,0,0,0,169,39,1,0,0,0,170,168,1,0,0,0,171,172,5,1,
        0,0,172,173,3,36,18,0,173,174,5,2,0,0,174,41,1,0,0,0,175,176,5,36,
        0,0,176,178,5,5,0,0,177,179,3,36,18,0,178,177,1,0,0,0,178,179,1,
        0,0,0,179,180,1,0,0,0,180,188,5,7,0,0,181,182,5,36,0,0,182,184,5,
        5,0,0,183,185,3,38,19,0,184,183,1,0,0,0,184,185,1,0,0,0,185,186,
        1,0,0,0,186,188,5,7,0,0,187,175,1,0,0,0,187,181,1,0,0,0,188,43,1,
        0,0,0,189,190,3,28,14,0,190,191,5,47,0,0,191,192,5,36,0,0,192,194,
        5,5,0,0,193,195,3,38,19,0,194,193,1,0,0,0,194,195,1,0,0,0,195,196,
        1,0,0,0,196,197,5,7,0,0,197,45,1,0,0,0,198,199,5,36,0,0,199,200,
        5,5,0,0,200,201,3,36,18,0,201,202,5,7,0,0,202,47,1,0,0,0,203,204,
        5,36,0,0,204,205,5,8,0,0,205,206,3,50,25,0,206,49,1,0,0,0,207,208,
        6,25,-1,0,208,224,3,34,17,0,209,224,5,36,0,0,210,211,5,5,0,0,211,
        212,3,50,25,0,212,213,5,7,0,0,213,224,1,0,0,0,214,215,5,9,0,0,215,
        216,3,38,19,0,216,217,5,10,0,0,217,224,1,0,0,0,218,224,3,42,21,0,
        219,224,3,44,22,0,220,221,7,2,0,0,221,224,3,50,25,13,222,224,3,40,
        20,0,223,207,1,0,0,0,223,209,1,0,0,0,223,210,1,0,0,0,223,214,1,0,
        0,0,223,218,1,0,0,0,223,219,1,0,0,0,223,220,1,0,0,0,223,222,1,0,
        0,0,224,275,1,0,0,0,225,226,10,12,0,0,226,227,7,3,0,0,227,274,3,
        50,25,13,228,229,10,11,0,0,229,230,7,4,0,0,230,274,3,50,25,12,231,
        239,10,10,0,0,232,233,5,22,0,0,233,240,5,22,0,0,234,235,5,23,0,0,
        235,236,5,23,0,0,236,240,5,23,0,0,237,238,5,23,0,0,238,240,5,23,
        0,0,239,232,1,0,0,0,239,234,1,0,0,0,239,237,1,0,0,0,240,241,1,0,
        0,0,241,274,3,50,25,11,242,243,10,9,0,0,243,244,7,5,0,0,244,274,
        3,50,25,10,245,246,10,8,0,0,246,247,7,6,0,0,247,274,3,50,25,9,248,
        249,10,7,0,0,249,250,5,28,0,0,250,274,3,50,25,8,251,252,10,6,0,0,
        252,253,5,29,0,0,253,274,3,50,25,7,254,255,10,5,0,0,255,256,5,30,
        0,0,256,274,3,50,25,6,257,258,10,4,0,0,258,259,5,31,0,0,259,274,
        3,50,25,5,260,261,10,3,0,0,261,262,5,32,0,0,262,274,3,50,25,4,263,
        264,10,2,0,0,264,265,5,33,0,0,265,274,3,50,25,3,266,267,10,17,0,
        0,267,268,5,9,0,0,268,269,3,30,15,0,269,270,5,10,0,0,270,274,1,0,
        0,0,271,272,10,14,0,0,272,274,7,7,0,0,273,225,1,0,0,0,273,228,1,
        0,0,0,273,231,1,0,0,0,273,242,1,0,0,0,273,245,1,0,0,0,273,248,1,
        0,0,0,273,251,1,0,0,0,273,254,1,0,0,0,273,257,1,0,0,0,273,260,1,
        0,0,0,273,263,1,0,0,0,273,266,1,0,0,0,273,271,1,0,0,0,274,277,1,
        0,0,0,275,273,1,0,0,0,275,276,1,0,0,0,276,51,1,0,0,0,277,275,1,0,
        0,0,21,53,56,66,72,83,93,108,136,143,148,151,160,168,178,184,187,
        194,223,239,273,275
    ]

class DataModelParser ( Parser ):

    grammarFileName = "DataModel.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "';'", "'for'", "'('", "'in'", 
                     "')'", "'='", "'['", "']'", "','", "'-'", "'true'", 
                     "'false'", "'++'", "'--'", "'+'", "'**'", "'*'", "'/'", 
                     "'%'", "'<'", "'>'", "'<='", "'>='", "'=='", "'!='", 
                     "'&'", "'^'", "'|'", "'&&'", "'||'", "':'", "'data'", 
                     "'model'", "<INVALID>", "'<-'", "'length'", "'dim'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'.'", "'~'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "DATA", "MODEL", "NAME", 
                      "ARROW", "LENGTH", "DIM", "DECIMAL_LITERAL", "HEX_LITERAL", 
                      "OCT_LITERAL", "BINARY_LITERAL", "FLOAT_LITERAL", 
                      "HEX_FLOAT_LITERAL", "STRING_LITERAL", "DOT", "TILDE", 
                      "WS", "COMMENT", "LINE_COMMENT" ]

    RULE_input = 0
    RULE_datablock = 1
    RULE_modelblock = 2
    RULE_relations = 3
    RULE_determ_relations = 4
    RULE_relation_list = 5
    RULE_determ_relation_list = 6
    RULE_determ_relation_line = 7
    RULE_relation = 8
    RULE_for_loop = 9
    RULE_counter = 10
    RULE_assignment = 11
    RULE_determ_relation = 12
    RULE_stoch_relation = 13
    RULE_var = 14
    RULE_range_list = 15
    RULE_range_element = 16
    RULE_constant = 17
    RULE_expression_list = 18
    RULE_unnamed_expression_list = 19
    RULE_mapFunction = 20
    RULE_methodCall = 21
    RULE_objectMethodCall = 22
    RULE_distribution = 23
    RULE_named_expression = 24
    RULE_expression = 25

    ruleNames =  [ "input", "datablock", "modelblock", "relations", "determ_relations", 
                   "relation_list", "determ_relation_list", "determ_relation_line", 
                   "relation", "for_loop", "counter", "assignment", "determ_relation", 
                   "stoch_relation", "var", "range_list", "range_element", 
                   "constant", "expression_list", "unnamed_expression_list", 
                   "mapFunction", "methodCall", "objectMethodCall", "distribution", 
                   "named_expression", "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    DATA=34
    MODEL=35
    NAME=36
    ARROW=37
    LENGTH=38
    DIM=39
    DECIMAL_LITERAL=40
    HEX_LITERAL=41
    OCT_LITERAL=42
    BINARY_LITERAL=43
    FLOAT_LITERAL=44
    HEX_FLOAT_LITERAL=45
    STRING_LITERAL=46
    DOT=47
    TILDE=48
    WS=49
    COMMENT=50
    LINE_COMMENT=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class InputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def datablock(self):
            return self.getTypedRuleContext(DataModelParser.DatablockContext,0)


        def modelblock(self):
            return self.getTypedRuleContext(DataModelParser.ModelblockContext,0)


        def getRuleIndex(self):
            return DataModelParser.RULE_input

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput" ):
                listener.enterInput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput" ):
                listener.exitInput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInput" ):
                return visitor.visitInput(self)
            else:
                return visitor.visitChildren(self)




    def input_(self):

        localctx = DataModelParser.InputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_input)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 52
                self.datablock()


            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 55
                self.modelblock()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DatablockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATA(self):
            return self.getToken(DataModelParser.DATA, 0)

        def determ_relations(self):
            return self.getTypedRuleContext(DataModelParser.Determ_relationsContext,0)


        def getRuleIndex(self):
            return DataModelParser.RULE_datablock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDatablock" ):
                listener.enterDatablock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDatablock" ):
                listener.exitDatablock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDatablock" ):
                return visitor.visitDatablock(self)
            else:
                return visitor.visitChildren(self)




    def datablock(self):

        localctx = DataModelParser.DatablockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_datablock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(DataModelParser.DATA)
            self.state = 59
            self.determ_relations()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModelblockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MODEL(self):
            return self.getToken(DataModelParser.MODEL, 0)

        def relations(self):
            return self.getTypedRuleContext(DataModelParser.RelationsContext,0)


        def getRuleIndex(self):
            return DataModelParser.RULE_modelblock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModelblock" ):
                listener.enterModelblock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModelblock" ):
                listener.exitModelblock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModelblock" ):
                return visitor.visitModelblock(self)
            else:
                return visitor.visitChildren(self)




    def modelblock(self):

        localctx = DataModelParser.ModelblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_modelblock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(DataModelParser.MODEL)
            self.state = 62
            self.relations()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relation_list(self):
            return self.getTypedRuleContext(DataModelParser.Relation_listContext,0)


        def getRuleIndex(self):
            return DataModelParser.RULE_relations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelations" ):
                listener.enterRelations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelations" ):
                listener.exitRelations(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelations" ):
                return visitor.visitRelations(self)
            else:
                return visitor.visitChildren(self)




    def relations(self):

        localctx = DataModelParser.RelationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_relations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(DataModelParser.T__0)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4 or _la==36:
                self.state = 65
                self.relation_list(0)


            self.state = 68
            self.match(DataModelParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Determ_relationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def determ_relation_list(self):
            return self.getTypedRuleContext(DataModelParser.Determ_relation_listContext,0)


        def getRuleIndex(self):
            return DataModelParser.RULE_determ_relations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeterm_relations" ):
                listener.enterDeterm_relations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeterm_relations" ):
                listener.exitDeterm_relations(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeterm_relations" ):
                return visitor.visitDeterm_relations(self)
            else:
                return visitor.visitChildren(self)




    def determ_relations(self):

        localctx = DataModelParser.Determ_relationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_determ_relations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(DataModelParser.T__0)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 71
                self.determ_relation_list(0)


            self.state = 74
            self.match(DataModelParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relation_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relation(self):
            return self.getTypedRuleContext(DataModelParser.RelationContext,0)


        def relation_list(self):
            return self.getTypedRuleContext(DataModelParser.Relation_listContext,0)


        def getRuleIndex(self):
            return DataModelParser.RULE_relation_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelation_list" ):
                listener.enterRelation_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelation_list" ):
                listener.exitRelation_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation_list" ):
                return visitor.visitRelation_list(self)
            else:
                return visitor.visitChildren(self)



    def relation_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = DataModelParser.Relation_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_relation_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.relation()
            self._ctx.stop = self._input.LT(-1)
            self.state = 83
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = DataModelParser.Relation_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relation_list)
                    self.state = 79
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 80
                    self.relation() 
                self.state = 85
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Determ_relation_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def determ_relation_line(self):
            return self.getTypedRuleContext(DataModelParser.Determ_relation_lineContext,0)


        def determ_relation_list(self):
            return self.getTypedRuleContext(DataModelParser.Determ_relation_listContext,0)


        def getRuleIndex(self):
            return DataModelParser.RULE_determ_relation_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeterm_relation_list" ):
                listener.enterDeterm_relation_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeterm_relation_list" ):
                listener.exitDeterm_relation_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeterm_relation_list" ):
                return visitor.visitDeterm_relation_list(self)
            else:
                return visitor.visitChildren(self)



    def determ_relation_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = DataModelParser.Determ_relation_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_determ_relation_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.determ_relation_line()
            self._ctx.stop = self._input.LT(-1)
            self.state = 93
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = DataModelParser.Determ_relation_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_determ_relation_list)
                    self.state = 89
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 90
                    self.determ_relation_line() 
                self.state = 95
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Determ_relation_lineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def determ_relation(self):
            return self.getTypedRuleContext(DataModelParser.Determ_relationContext,0)


        def getRuleIndex(self):
            return DataModelParser.RULE_determ_relation_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeterm_relation_line" ):
                listener.enterDeterm_relation_line(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeterm_relation_line" ):
                listener.exitDeterm_relation_line(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeterm_relation_line" ):
                return visitor.visitDeterm_relation_line(self)
            else:
                return visitor.visitChildren(self)




    def determ_relation_line(self):

        localctx = DataModelParser.Determ_relation_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_determ_relation_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.determ_relation()
            self.state = 97
            self.match(DataModelParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stoch_relation(self):
            return self.getTypedRuleContext(DataModelParser.Stoch_relationContext,0)


        def determ_relation(self):
            return self.getTypedRuleContext(DataModelParser.Determ_relationContext,0)


        def for_loop(self):
            return self.getTypedRuleContext(DataModelParser.For_loopContext,0)


        def getRuleIndex(self):
            return DataModelParser.RULE_relation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelation" ):
                listener.enterRelation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelation" ):
                listener.exitRelation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation" ):
                return visitor.visitRelation(self)
            else:
                return visitor.visitChildren(self)




    def relation(self):

        localctx = DataModelParser.RelationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_relation)
        try:
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.stoch_relation()
                self.state = 100
                self.match(DataModelParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.determ_relation()
                self.state = 103
                self.match(DataModelParser.T__2)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 105
                self.for_loop()
                self.state = 106
                self.match(DataModelParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def counter(self):
            return self.getTypedRuleContext(DataModelParser.CounterContext,0)


        def relations(self):
            return self.getTypedRuleContext(DataModelParser.RelationsContext,0)


        def getRuleIndex(self):
            return DataModelParser.RULE_for_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_loop" ):
                listener.enterFor_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_loop" ):
                listener.exitFor_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop" ):
                return visitor.visitFor_loop(self)
            else:
                return visitor.visitChildren(self)




    def for_loop(self):

        localctx = DataModelParser.For_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.counter()
            self.state = 111
            self.relations()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CounterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(DataModelParser.NAME, 0)

        def range_element(self):
            return self.getTypedRuleContext(DataModelParser.Range_elementContext,0)


        def getRuleIndex(self):
            return DataModelParser.RULE_counter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCounter" ):
                listener.enterCounter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCounter" ):
                listener.exitCounter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCounter" ):
                return visitor.visitCounter(self)
            else:
                return visitor.visitChildren(self)




    def counter(self):

        localctx = DataModelParser.CounterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_counter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(DataModelParser.T__3)
            self.state = 114
            self.match(DataModelParser.T__4)
            self.state = 115
            self.match(DataModelParser.NAME)
            self.state = 116
            self.match(DataModelParser.T__5)
            self.state = 117
            self.range_element()
            self.state = 118
            self.match(DataModelParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARROW(self):
            return self.getToken(DataModelParser.ARROW, 0)

        def getRuleIndex(self):
            return DataModelParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = DataModelParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            _la = self._input.LA(1)
            if not(_la==8 or _la==37):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Determ_relationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(DataModelParser.VarContext,0)


        def assignment(self):
            return self.getTypedRuleContext(DataModelParser.AssignmentContext,0)


        def expression(self):
            return self.getTypedRuleContext(DataModelParser.ExpressionContext,0)


        def getRuleIndex(self):
            return DataModelParser.RULE_determ_relation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeterm_relation" ):
                listener.enterDeterm_relation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeterm_relation" ):
                listener.exitDeterm_relation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeterm_relation" ):
                return visitor.visitDeterm_relation(self)
            else:
                return visitor.visitChildren(self)




    def determ_relation(self):

        localctx = DataModelParser.Determ_relationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_determ_relation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.var()
            self.state = 123
            self.assignment()
            self.state = 124
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stoch_relationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(DataModelParser.VarContext,0)


        def TILDE(self):
            return self.getToken(DataModelParser.TILDE, 0)

        def distribution(self):
            return self.getTypedRuleContext(DataModelParser.DistributionContext,0)


        def getRuleIndex(self):
            return DataModelParser.RULE_stoch_relation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStoch_relation" ):
                listener.enterStoch_relation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStoch_relation" ):
                listener.exitStoch_relation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStoch_relation" ):
                return visitor.visitStoch_relation(self)
            else:
                return visitor.visitChildren(self)




    def stoch_relation(self):

        localctx = DataModelParser.Stoch_relationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_stoch_relation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.var()
            self.state = 127
            self.match(DataModelParser.TILDE)
            self.state = 128
            self.distribution()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(DataModelParser.NAME, 0)

        def range_list(self):
            return self.getTypedRuleContext(DataModelParser.Range_listContext,0)


        def getRuleIndex(self):
            return DataModelParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = DataModelParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_var)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.match(DataModelParser.NAME)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.match(DataModelParser.NAME)
                self.state = 132
                self.match(DataModelParser.T__8)
                self.state = 133
                self.range_list()
                self.state = 134
                self.match(DataModelParser.T__9)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DataModelParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(DataModelParser.ExpressionContext,i)


        def getRuleIndex(self):
            return DataModelParser.RULE_range_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange_list" ):
                listener.enterRange_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange_list" ):
                listener.exitRange_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_list" ):
                return visitor.visitRange_list(self)
            else:
                return visitor.visitChildren(self)




    def range_list(self):

        localctx = DataModelParser.Range_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_range_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.expression(0)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 139
                self.match(DataModelParser.T__10)
                self.state = 140
                self.expression(0)
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(DataModelParser.ExpressionContext,0)


        def getRuleIndex(self):
            return DataModelParser.RULE_range_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange_element" ):
                listener.enterRange_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange_element" ):
                listener.exitRange_element(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_element" ):
                return visitor.visitRange_element(self)
            else:
                return visitor.visitChildren(self)




    def range_element(self):

        localctx = DataModelParser.Range_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_range_element)
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [1, 5, 9, 12, 13, 14, 15, 16, 17, 36, 40, 41, 42, 44, 45, 46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.expression(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT_LITERAL(self):
            return self.getToken(DataModelParser.FLOAT_LITERAL, 0)

        def DECIMAL_LITERAL(self):
            return self.getToken(DataModelParser.DECIMAL_LITERAL, 0)

        def OCT_LITERAL(self):
            return self.getToken(DataModelParser.OCT_LITERAL, 0)

        def HEX_LITERAL(self):
            return self.getToken(DataModelParser.HEX_LITERAL, 0)

        def HEX_FLOAT_LITERAL(self):
            return self.getToken(DataModelParser.HEX_FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(DataModelParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return DataModelParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant" ):
                return visitor.visitConstant(self)
            else:
                return visitor.visitChildren(self)




    def constant(self):

        localctx = DataModelParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 150
                self.match(DataModelParser.T__11)


            self.state = 153
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 130841883729920) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def named_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DataModelParser.Named_expressionContext)
            else:
                return self.getTypedRuleContext(DataModelParser.Named_expressionContext,i)


        def getRuleIndex(self):
            return DataModelParser.RULE_expression_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_list" ):
                listener.enterExpression_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_list" ):
                listener.exitExpression_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_list" ):
                return visitor.visitExpression_list(self)
            else:
                return visitor.visitChildren(self)




    def expression_list(self):

        localctx = DataModelParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.named_expression()
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 156
                self.match(DataModelParser.T__10)
                self.state = 157
                self.named_expression()
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unnamed_expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DataModelParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(DataModelParser.ExpressionContext,i)


        def getRuleIndex(self):
            return DataModelParser.RULE_unnamed_expression_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnnamed_expression_list" ):
                listener.enterUnnamed_expression_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnnamed_expression_list" ):
                listener.exitUnnamed_expression_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnnamed_expression_list" ):
                return visitor.visitUnnamed_expression_list(self)
            else:
                return visitor.visitChildren(self)




    def unnamed_expression_list(self):

        localctx = DataModelParser.Unnamed_expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_unnamed_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.expression(0)
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 164
                self.match(DataModelParser.T__10)
                self.state = 165
                self.expression(0)
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MapFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_list(self):
            return self.getTypedRuleContext(DataModelParser.Expression_listContext,0)


        def getRuleIndex(self):
            return DataModelParser.RULE_mapFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapFunction" ):
                listener.enterMapFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapFunction" ):
                listener.exitMapFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapFunction" ):
                return visitor.visitMapFunction(self)
            else:
                return visitor.visitChildren(self)




    def mapFunction(self):

        localctx = DataModelParser.MapFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_mapFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(DataModelParser.T__0)
            self.state = 172
            self.expression_list()
            self.state = 173
            self.match(DataModelParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(DataModelParser.NAME, 0)

        def expression_list(self):
            return self.getTypedRuleContext(DataModelParser.Expression_listContext,0)


        def unnamed_expression_list(self):
            return self.getTypedRuleContext(DataModelParser.Unnamed_expression_listContext,0)


        def getRuleIndex(self):
            return DataModelParser.RULE_methodCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodCall" ):
                listener.enterMethodCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodCall" ):
                listener.exitMethodCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCall" ):
                return visitor.visitMethodCall(self)
            else:
                return visitor.visitChildren(self)




    def methodCall(self):

        localctx = DataModelParser.MethodCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_methodCall)
        self._la = 0 # Token type
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.match(DataModelParser.NAME)
                self.state = 176
                self.match(DataModelParser.T__4)
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
                    self.state = 177
                    self.expression_list()


                self.state = 180
                self.match(DataModelParser.T__6)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.match(DataModelParser.NAME)
                self.state = 182
                self.match(DataModelParser.T__4)
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 130910603440674) != 0):
                    self.state = 183
                    self.unnamed_expression_list()


                self.state = 186
                self.match(DataModelParser.T__6)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectMethodCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(DataModelParser.VarContext,0)


        def DOT(self):
            return self.getToken(DataModelParser.DOT, 0)

        def NAME(self):
            return self.getToken(DataModelParser.NAME, 0)

        def unnamed_expression_list(self):
            return self.getTypedRuleContext(DataModelParser.Unnamed_expression_listContext,0)


        def getRuleIndex(self):
            return DataModelParser.RULE_objectMethodCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjectMethodCall" ):
                listener.enterObjectMethodCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjectMethodCall" ):
                listener.exitObjectMethodCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjectMethodCall" ):
                return visitor.visitObjectMethodCall(self)
            else:
                return visitor.visitChildren(self)




    def objectMethodCall(self):

        localctx = DataModelParser.ObjectMethodCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_objectMethodCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.var()
            self.state = 190
            self.match(DataModelParser.DOT)
            self.state = 191
            self.match(DataModelParser.NAME)
            self.state = 192
            self.match(DataModelParser.T__4)
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 130910603440674) != 0):
                self.state = 193
                self.unnamed_expression_list()


            self.state = 196
            self.match(DataModelParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DistributionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(DataModelParser.NAME, 0)

        def expression_list(self):
            return self.getTypedRuleContext(DataModelParser.Expression_listContext,0)


        def getRuleIndex(self):
            return DataModelParser.RULE_distribution

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistribution" ):
                listener.enterDistribution(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistribution" ):
                listener.exitDistribution(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDistribution" ):
                return visitor.visitDistribution(self)
            else:
                return visitor.visitChildren(self)




    def distribution(self):

        localctx = DataModelParser.DistributionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_distribution)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(DataModelParser.NAME)
            self.state = 199
            self.match(DataModelParser.T__4)
            self.state = 200
            self.expression_list()
            self.state = 201
            self.match(DataModelParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Named_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(DataModelParser.NAME, 0)

        def expression(self):
            return self.getTypedRuleContext(DataModelParser.ExpressionContext,0)


        def getRuleIndex(self):
            return DataModelParser.RULE_named_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamed_expression" ):
                listener.enterNamed_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamed_expression" ):
                listener.exitNamed_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamed_expression" ):
                return visitor.visitNamed_expression(self)
            else:
                return visitor.visitChildren(self)




    def named_expression(self):

        localctx = DataModelParser.Named_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_named_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(DataModelParser.NAME)
            self.state = 204
            self.match(DataModelParser.T__7)
            self.state = 205
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.prefix = None # Token
            self.bop = None # Token
            self.postfix = None # Token

        def constant(self):
            return self.getTypedRuleContext(DataModelParser.ConstantContext,0)


        def NAME(self):
            return self.getToken(DataModelParser.NAME, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DataModelParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(DataModelParser.ExpressionContext,i)


        def unnamed_expression_list(self):
            return self.getTypedRuleContext(DataModelParser.Unnamed_expression_listContext,0)


        def methodCall(self):
            return self.getTypedRuleContext(DataModelParser.MethodCallContext,0)


        def objectMethodCall(self):
            return self.getTypedRuleContext(DataModelParser.ObjectMethodCallContext,0)


        def mapFunction(self):
            return self.getTypedRuleContext(DataModelParser.MapFunctionContext,0)


        def range_list(self):
            return self.getTypedRuleContext(DataModelParser.Range_listContext,0)


        def getRuleIndex(self):
            return DataModelParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = DataModelParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 208
                self.constant()
                pass

            elif la_ == 2:
                self.state = 209
                self.match(DataModelParser.NAME)
                pass

            elif la_ == 3:
                self.state = 210
                self.match(DataModelParser.T__4)
                self.state = 211
                self.expression(0)
                self.state = 212
                self.match(DataModelParser.T__6)
                pass

            elif la_ == 4:
                self.state = 214
                self.match(DataModelParser.T__8)
                self.state = 215
                self.unnamed_expression_list()
                self.state = 216
                self.match(DataModelParser.T__9)
                pass

            elif la_ == 5:
                self.state = 218
                self.methodCall()
                pass

            elif la_ == 6:
                self.state = 219
                self.objectMethodCall()
                pass

            elif la_ == 7:
                self.state = 220
                localctx.prefix = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 233472) != 0)):
                    localctx.prefix = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 221
                self.expression(13)
                pass

            elif la_ == 8:
                self.state = 222
                self.mapFunction()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 275
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 273
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = DataModelParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 225
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 226
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3932160) != 0)):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 227
                        self.expression(13)
                        pass

                    elif la_ == 2:
                        localctx = DataModelParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 228
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 229
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==17):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 230
                        self.expression(12)
                        pass

                    elif la_ == 3:
                        localctx = DataModelParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 231
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 239
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                        if la_ == 1:
                            self.state = 232
                            self.match(DataModelParser.T__21)
                            self.state = 233
                            self.match(DataModelParser.T__21)
                            pass

                        elif la_ == 2:
                            self.state = 234
                            self.match(DataModelParser.T__22)
                            self.state = 235
                            self.match(DataModelParser.T__22)
                            self.state = 236
                            self.match(DataModelParser.T__22)
                            pass

                        elif la_ == 3:
                            self.state = 237
                            self.match(DataModelParser.T__22)
                            self.state = 238
                            self.match(DataModelParser.T__22)
                            pass


                        self.state = 241
                        self.expression(11)
                        pass

                    elif la_ == 4:
                        localctx = DataModelParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 242
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 243
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62914560) != 0)):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 244
                        self.expression(10)
                        pass

                    elif la_ == 5:
                        localctx = DataModelParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 245
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 246
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==26 or _la==27):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 247
                        self.expression(9)
                        pass

                    elif la_ == 6:
                        localctx = DataModelParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 248
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 249
                        localctx.bop = self.match(DataModelParser.T__27)
                        self.state = 250
                        self.expression(8)
                        pass

                    elif la_ == 7:
                        localctx = DataModelParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 251
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 252
                        localctx.bop = self.match(DataModelParser.T__28)
                        self.state = 253
                        self.expression(7)
                        pass

                    elif la_ == 8:
                        localctx = DataModelParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 254
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 255
                        localctx.bop = self.match(DataModelParser.T__29)
                        self.state = 256
                        self.expression(6)
                        pass

                    elif la_ == 9:
                        localctx = DataModelParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 257
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 258
                        localctx.bop = self.match(DataModelParser.T__30)
                        self.state = 259
                        self.expression(5)
                        pass

                    elif la_ == 10:
                        localctx = DataModelParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 260
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 261
                        localctx.bop = self.match(DataModelParser.T__31)
                        self.state = 262
                        self.expression(4)
                        pass

                    elif la_ == 11:
                        localctx = DataModelParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 263
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 264
                        localctx.bop = self.match(DataModelParser.T__32)
                        self.state = 265
                        self.expression(3)
                        pass

                    elif la_ == 12:
                        localctx = DataModelParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 266
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 267
                        self.match(DataModelParser.T__8)
                        self.state = 268
                        self.range_list()
                        self.state = 269
                        self.match(DataModelParser.T__9)
                        pass

                    elif la_ == 13:
                        localctx = DataModelParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 271
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 272
                        localctx.postfix = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            localctx.postfix = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass

             
                self.state = 277
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.relation_list_sempred
        self._predicates[6] = self.determ_relation_list_sempred
        self._predicates[25] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def relation_list_sempred(self, localctx:Relation_listContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def determ_relation_list_sempred(self, localctx:Determ_relation_listContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 14)
         




