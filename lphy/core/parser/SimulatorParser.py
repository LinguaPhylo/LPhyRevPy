# Generated from LPhyRevPy/lphy/core/parser/Simulator.g4 by ANTLR 4.12.0

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
        4,1,47,223,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,0,3,0,41,
        8,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,5,2,52,8,2,10,2,12,2,55,
        9,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,63,8,3,1,4,1,4,1,5,1,5,1,5,1,5,1,
        6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,81,8,7,1,8,1,8,1,8,5,8,
        86,8,8,10,8,12,8,89,9,8,1,9,1,9,3,9,93,8,9,1,10,3,10,96,8,10,1,10,
        1,10,1,11,1,11,1,11,5,11,103,8,11,10,11,12,11,106,9,11,1,12,1,12,
        1,12,5,12,111,8,12,10,12,12,12,114,9,12,1,13,1,13,1,13,1,13,1,14,
        1,14,1,14,3,14,123,8,14,1,14,1,14,1,14,1,14,3,14,129,8,14,1,14,3,
        14,132,8,14,1,15,1,15,1,15,1,15,1,15,3,15,139,8,15,1,15,1,15,1,16,
        1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,168,
        8,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,3,18,184,8,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,5,18,218,
        8,18,10,18,12,18,221,9,18,1,18,0,2,4,36,19,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,0,8,2,0,4,4,33,33,3,0,9,10,36,38,40,
        42,2,0,8,8,13,15,1,0,16,19,2,0,8,8,15,15,1,0,20,23,1,0,24,25,1,0,
        13,14,238,0,40,1,0,0,0,2,42,1,0,0,0,4,46,1,0,0,0,6,62,1,0,0,0,8,
        64,1,0,0,0,10,66,1,0,0,0,12,70,1,0,0,0,14,80,1,0,0,0,16,82,1,0,0,
        0,18,92,1,0,0,0,20,95,1,0,0,0,22,99,1,0,0,0,24,107,1,0,0,0,26,115,
        1,0,0,0,28,131,1,0,0,0,30,133,1,0,0,0,32,142,1,0,0,0,34,147,1,0,
        0,0,36,167,1,0,0,0,38,41,1,0,0,0,39,41,3,4,2,0,40,38,1,0,0,0,40,
        39,1,0,0,0,41,1,1,0,0,0,42,43,5,1,0,0,43,44,3,4,2,0,44,45,5,2,0,
        0,45,3,1,0,0,0,46,47,6,2,-1,0,47,48,3,6,3,0,48,53,1,0,0,0,49,50,
        10,1,0,0,50,52,3,6,3,0,51,49,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,
        53,54,1,0,0,0,54,5,1,0,0,0,55,53,1,0,0,0,56,57,3,12,6,0,57,58,5,
        3,0,0,58,63,1,0,0,0,59,60,3,10,5,0,60,61,5,3,0,0,61,63,1,0,0,0,62,
        56,1,0,0,0,62,59,1,0,0,0,63,7,1,0,0,0,64,65,7,0,0,0,65,9,1,0,0,0,
        66,67,3,14,7,0,67,68,3,8,4,0,68,69,3,36,18,0,69,11,1,0,0,0,70,71,
        3,14,7,0,71,72,5,44,0,0,72,73,3,32,16,0,73,13,1,0,0,0,74,75,5,32,
        0,0,75,76,5,5,0,0,76,77,3,16,8,0,77,78,5,6,0,0,78,81,1,0,0,0,79,
        81,5,32,0,0,80,74,1,0,0,0,80,79,1,0,0,0,81,15,1,0,0,0,82,87,3,36,
        18,0,83,84,5,7,0,0,84,86,3,36,18,0,85,83,1,0,0,0,86,89,1,0,0,0,87,
        85,1,0,0,0,87,88,1,0,0,0,88,17,1,0,0,0,89,87,1,0,0,0,90,93,1,0,0,
        0,91,93,3,36,18,0,92,90,1,0,0,0,92,91,1,0,0,0,93,19,1,0,0,0,94,96,
        5,8,0,0,95,94,1,0,0,0,95,96,1,0,0,0,96,97,1,0,0,0,97,98,7,1,0,0,
        98,21,1,0,0,0,99,104,3,34,17,0,100,101,5,7,0,0,101,103,3,34,17,0,
        102,100,1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,
        105,23,1,0,0,0,106,104,1,0,0,0,107,112,3,36,18,0,108,109,5,7,0,0,
        109,111,3,36,18,0,110,108,1,0,0,0,111,114,1,0,0,0,112,110,1,0,0,
        0,112,113,1,0,0,0,113,25,1,0,0,0,114,112,1,0,0,0,115,116,5,1,0,0,
        116,117,3,22,11,0,117,118,5,2,0,0,118,27,1,0,0,0,119,120,5,32,0,
        0,120,122,5,11,0,0,121,123,3,22,11,0,122,121,1,0,0,0,122,123,1,0,
        0,0,123,124,1,0,0,0,124,132,5,12,0,0,125,126,5,32,0,0,126,128,5,
        11,0,0,127,129,3,24,12,0,128,127,1,0,0,0,128,129,1,0,0,0,129,130,
        1,0,0,0,130,132,5,12,0,0,131,119,1,0,0,0,131,125,1,0,0,0,132,29,
        1,0,0,0,133,134,3,14,7,0,134,135,5,43,0,0,135,136,5,32,0,0,136,138,
        5,11,0,0,137,139,3,24,12,0,138,137,1,0,0,0,138,139,1,0,0,0,139,140,
        1,0,0,0,140,141,5,12,0,0,141,31,1,0,0,0,142,143,5,32,0,0,143,144,
        5,11,0,0,144,145,3,22,11,0,145,146,5,12,0,0,146,33,1,0,0,0,147,148,
        5,32,0,0,148,149,5,4,0,0,149,150,3,36,18,0,150,35,1,0,0,0,151,152,
        6,18,-1,0,152,168,3,20,10,0,153,168,5,32,0,0,154,155,5,11,0,0,155,
        156,3,36,18,0,156,157,5,12,0,0,157,168,1,0,0,0,158,159,5,5,0,0,159,
        160,3,24,12,0,160,161,5,6,0,0,161,168,1,0,0,0,162,168,3,28,14,0,
        163,168,3,30,15,0,164,165,7,2,0,0,165,168,3,36,18,13,166,168,3,26,
        13,0,167,151,1,0,0,0,167,153,1,0,0,0,167,154,1,0,0,0,167,158,1,0,
        0,0,167,162,1,0,0,0,167,163,1,0,0,0,167,164,1,0,0,0,167,166,1,0,
        0,0,168,219,1,0,0,0,169,170,10,12,0,0,170,171,7,3,0,0,171,218,3,
        36,18,13,172,173,10,11,0,0,173,174,7,4,0,0,174,218,3,36,18,12,175,
        183,10,10,0,0,176,177,5,20,0,0,177,184,5,20,0,0,178,179,5,21,0,0,
        179,180,5,21,0,0,180,184,5,21,0,0,181,182,5,21,0,0,182,184,5,21,
        0,0,183,176,1,0,0,0,183,178,1,0,0,0,183,181,1,0,0,0,184,185,1,0,
        0,0,185,218,3,36,18,11,186,187,10,9,0,0,187,188,7,5,0,0,188,218,
        3,36,18,10,189,190,10,8,0,0,190,191,7,6,0,0,191,218,3,36,18,9,192,
        193,10,7,0,0,193,194,5,26,0,0,194,218,3,36,18,8,195,196,10,6,0,0,
        196,197,5,27,0,0,197,218,3,36,18,7,198,199,10,5,0,0,199,200,5,28,
        0,0,200,218,3,36,18,6,201,202,10,4,0,0,202,203,5,29,0,0,203,218,
        3,36,18,5,204,205,10,3,0,0,205,206,5,30,0,0,206,218,3,36,18,4,207,
        208,10,2,0,0,208,209,5,31,0,0,209,218,3,36,18,3,210,211,10,17,0,
        0,211,212,5,5,0,0,212,213,3,16,8,0,213,214,5,6,0,0,214,218,1,0,0,
        0,215,216,10,14,0,0,216,218,7,7,0,0,217,169,1,0,0,0,217,172,1,0,
        0,0,217,175,1,0,0,0,217,186,1,0,0,0,217,189,1,0,0,0,217,192,1,0,
        0,0,217,195,1,0,0,0,217,198,1,0,0,0,217,201,1,0,0,0,217,204,1,0,
        0,0,217,207,1,0,0,0,217,210,1,0,0,0,217,215,1,0,0,0,218,221,1,0,
        0,0,219,217,1,0,0,0,219,220,1,0,0,0,220,37,1,0,0,0,221,219,1,0,0,
        0,17,40,53,62,80,87,92,95,104,112,122,128,131,138,167,183,217,219
    ]

class SimulatorParser ( Parser ):

    grammarFileName = "Simulator.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "';'", "'='", "'['", "']'", 
                     "','", "'-'", "'true'", "'false'", "'('", "')'", "'++'", 
                     "'--'", "'+'", "'**'", "'*'", "'/'", "'%'", "'<'", 
                     "'>'", "'<='", "'>='", "'=='", "'!='", "'&'", "'^'", 
                     "'|'", "'&&'", "'||'", "':'", "<INVALID>", "'<-'", 
                     "'length'", "'dim'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'.'", "'~'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NAME", "ARROW", "LENGTH", "DIM", "DECIMAL_LITERAL", 
                      "HEX_LITERAL", "OCT_LITERAL", "BINARY_LITERAL", "FLOAT_LITERAL", 
                      "HEX_FLOAT_LITERAL", "STRING_LITERAL", "DOT", "TILDE", 
                      "WS", "COMMENT", "LINE_COMMENT" ]

    RULE_input = 0
    RULE_relations = 1
    RULE_relation_list = 2
    RULE_relation = 3
    RULE_assignment = 4
    RULE_determ_relation = 5
    RULE_stoch_relation = 6
    RULE_var = 7
    RULE_range_list = 8
    RULE_range_element = 9
    RULE_constant = 10
    RULE_expression_list = 11
    RULE_unnamed_expression_list = 12
    RULE_mapFunction = 13
    RULE_methodCall = 14
    RULE_objectMethodCall = 15
    RULE_distribution = 16
    RULE_named_expression = 17
    RULE_expression = 18

    ruleNames =  [ "input", "relations", "relation_list", "relation", "assignment", 
                   "determ_relation", "stoch_relation", "var", "range_list", 
                   "range_element", "constant", "expression_list", "unnamed_expression_list", 
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
    NAME=32
    ARROW=33
    LENGTH=34
    DIM=35
    DECIMAL_LITERAL=36
    HEX_LITERAL=37
    OCT_LITERAL=38
    BINARY_LITERAL=39
    FLOAT_LITERAL=40
    HEX_FLOAT_LITERAL=41
    STRING_LITERAL=42
    DOT=43
    TILDE=44
    WS=45
    COMMENT=46
    LINE_COMMENT=47

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

        def relation_list(self):
            return self.getTypedRuleContext(SimulatorParser.Relation_listContext,0)


        def getRuleIndex(self):
            return SimulatorParser.RULE_input

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

        localctx = SimulatorParser.InputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_input)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.relation_list(0)
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


    class RelationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relation_list(self):
            return self.getTypedRuleContext(SimulatorParser.Relation_listContext,0)


        def getRuleIndex(self):
            return SimulatorParser.RULE_relations

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

        localctx = SimulatorParser.RelationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_relations)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(SimulatorParser.T__0)
            self.state = 43
            self.relation_list(0)
            self.state = 44
            self.match(SimulatorParser.T__1)
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
            return self.getTypedRuleContext(SimulatorParser.RelationContext,0)


        def relation_list(self):
            return self.getTypedRuleContext(SimulatorParser.Relation_listContext,0)


        def getRuleIndex(self):
            return SimulatorParser.RULE_relation_list

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
        localctx = SimulatorParser.Relation_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_relation_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.relation()
            self._ctx.stop = self._input.LT(-1)
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimulatorParser.Relation_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relation_list)
                    self.state = 49
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 50
                    self.relation() 
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RelationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stoch_relation(self):
            return self.getTypedRuleContext(SimulatorParser.Stoch_relationContext,0)


        def determ_relation(self):
            return self.getTypedRuleContext(SimulatorParser.Determ_relationContext,0)


        def getRuleIndex(self):
            return SimulatorParser.RULE_relation

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

        localctx = SimulatorParser.RelationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_relation)
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.stoch_relation()
                self.state = 57
                self.match(SimulatorParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.determ_relation()
                self.state = 60
                self.match(SimulatorParser.T__2)
                pass


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
            return self.getToken(SimulatorParser.ARROW, 0)

        def getRuleIndex(self):
            return SimulatorParser.RULE_assignment

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

        localctx = SimulatorParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            _la = self._input.LA(1)
            if not(_la==4 or _la==33):
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
            return self.getTypedRuleContext(SimulatorParser.VarContext,0)


        def assignment(self):
            return self.getTypedRuleContext(SimulatorParser.AssignmentContext,0)


        def expression(self):
            return self.getTypedRuleContext(SimulatorParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SimulatorParser.RULE_determ_relation

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

        localctx = SimulatorParser.Determ_relationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_determ_relation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.var()
            self.state = 67
            self.assignment()
            self.state = 68
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
            return self.getTypedRuleContext(SimulatorParser.VarContext,0)


        def TILDE(self):
            return self.getToken(SimulatorParser.TILDE, 0)

        def distribution(self):
            return self.getTypedRuleContext(SimulatorParser.DistributionContext,0)


        def getRuleIndex(self):
            return SimulatorParser.RULE_stoch_relation

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

        localctx = SimulatorParser.Stoch_relationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stoch_relation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.var()
            self.state = 71
            self.match(SimulatorParser.TILDE)
            self.state = 72
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
            return self.getToken(SimulatorParser.NAME, 0)

        def range_list(self):
            return self.getTypedRuleContext(SimulatorParser.Range_listContext,0)


        def getRuleIndex(self):
            return SimulatorParser.RULE_var

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

        localctx = SimulatorParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_var)
        try:
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.match(SimulatorParser.NAME)
                self.state = 75
                self.match(SimulatorParser.T__4)
                self.state = 76
                self.range_list()
                self.state = 77
                self.match(SimulatorParser.T__5)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.match(SimulatorParser.NAME)
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
                return self.getTypedRuleContexts(SimulatorParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SimulatorParser.ExpressionContext,i)


        def getRuleIndex(self):
            return SimulatorParser.RULE_range_list

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

        localctx = SimulatorParser.Range_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_range_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.expression(0)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 83
                self.match(SimulatorParser.T__6)
                self.state = 84
                self.expression(0)
                self.state = 89
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
            return self.getTypedRuleContext(SimulatorParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SimulatorParser.RULE_range_element

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

        localctx = SimulatorParser.Range_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_range_element)
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [1, 5, 8, 9, 10, 11, 13, 14, 15, 32, 36, 37, 38, 40, 41, 42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
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
            return self.getToken(SimulatorParser.FLOAT_LITERAL, 0)

        def DECIMAL_LITERAL(self):
            return self.getToken(SimulatorParser.DECIMAL_LITERAL, 0)

        def OCT_LITERAL(self):
            return self.getToken(SimulatorParser.OCT_LITERAL, 0)

        def HEX_LITERAL(self):
            return self.getToken(SimulatorParser.HEX_LITERAL, 0)

        def HEX_FLOAT_LITERAL(self):
            return self.getToken(SimulatorParser.HEX_FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(SimulatorParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return SimulatorParser.RULE_constant

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

        localctx = SimulatorParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 94
                self.match(SimulatorParser.T__7)


            self.state = 97
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8177617733120) != 0)):
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
                return self.getTypedRuleContexts(SimulatorParser.Named_expressionContext)
            else:
                return self.getTypedRuleContext(SimulatorParser.Named_expressionContext,i)


        def getRuleIndex(self):
            return SimulatorParser.RULE_expression_list

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

        localctx = SimulatorParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.named_expression()
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 100
                self.match(SimulatorParser.T__6)
                self.state = 101
                self.named_expression()
                self.state = 106
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
                return self.getTypedRuleContexts(SimulatorParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SimulatorParser.ExpressionContext,i)


        def getRuleIndex(self):
            return SimulatorParser.RULE_unnamed_expression_list

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

        localctx = SimulatorParser.Unnamed_expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_unnamed_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.expression(0)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 108
                self.match(SimulatorParser.T__6)
                self.state = 109
                self.expression(0)
                self.state = 114
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
            return self.getTypedRuleContext(SimulatorParser.Expression_listContext,0)


        def getRuleIndex(self):
            return SimulatorParser.RULE_mapFunction

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

        localctx = SimulatorParser.MapFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_mapFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(SimulatorParser.T__0)
            self.state = 116
            self.expression_list()
            self.state = 117
            self.match(SimulatorParser.T__1)
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
            return self.getToken(SimulatorParser.NAME, 0)

        def expression_list(self):
            return self.getTypedRuleContext(SimulatorParser.Expression_listContext,0)


        def unnamed_expression_list(self):
            return self.getTypedRuleContext(SimulatorParser.Unnamed_expression_listContext,0)


        def getRuleIndex(self):
            return SimulatorParser.RULE_methodCall

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

        localctx = SimulatorParser.MethodCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_methodCall)
        self._la = 0 # Token type
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.match(SimulatorParser.NAME)
                self.state = 120
                self.match(SimulatorParser.T__10)
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==32:
                    self.state = 121
                    self.expression_list()


                self.state = 124
                self.match(SimulatorParser.T__11)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.match(SimulatorParser.NAME)
                self.state = 126
                self.match(SimulatorParser.T__10)
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8181912760098) != 0):
                    self.state = 127
                    self.unnamed_expression_list()


                self.state = 130
                self.match(SimulatorParser.T__11)
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
            return self.getTypedRuleContext(SimulatorParser.VarContext,0)


        def DOT(self):
            return self.getToken(SimulatorParser.DOT, 0)

        def NAME(self):
            return self.getToken(SimulatorParser.NAME, 0)

        def unnamed_expression_list(self):
            return self.getTypedRuleContext(SimulatorParser.Unnamed_expression_listContext,0)


        def getRuleIndex(self):
            return SimulatorParser.RULE_objectMethodCall

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

        localctx = SimulatorParser.ObjectMethodCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_objectMethodCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.var()
            self.state = 134
            self.match(SimulatorParser.DOT)
            self.state = 135
            self.match(SimulatorParser.NAME)
            self.state = 136
            self.match(SimulatorParser.T__10)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8181912760098) != 0):
                self.state = 137
                self.unnamed_expression_list()


            self.state = 140
            self.match(SimulatorParser.T__11)
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
            return self.getToken(SimulatorParser.NAME, 0)

        def expression_list(self):
            return self.getTypedRuleContext(SimulatorParser.Expression_listContext,0)


        def getRuleIndex(self):
            return SimulatorParser.RULE_distribution

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

        localctx = SimulatorParser.DistributionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_distribution)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(SimulatorParser.NAME)
            self.state = 143
            self.match(SimulatorParser.T__10)
            self.state = 144
            self.expression_list()
            self.state = 145
            self.match(SimulatorParser.T__11)
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
            return self.getToken(SimulatorParser.NAME, 0)

        def expression(self):
            return self.getTypedRuleContext(SimulatorParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SimulatorParser.RULE_named_expression

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

        localctx = SimulatorParser.Named_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_named_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(SimulatorParser.NAME)
            self.state = 148
            self.match(SimulatorParser.T__3)
            self.state = 149
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
            return self.getTypedRuleContext(SimulatorParser.ConstantContext,0)


        def NAME(self):
            return self.getToken(SimulatorParser.NAME, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimulatorParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SimulatorParser.ExpressionContext,i)


        def unnamed_expression_list(self):
            return self.getTypedRuleContext(SimulatorParser.Unnamed_expression_listContext,0)


        def methodCall(self):
            return self.getTypedRuleContext(SimulatorParser.MethodCallContext,0)


        def objectMethodCall(self):
            return self.getTypedRuleContext(SimulatorParser.ObjectMethodCallContext,0)


        def mapFunction(self):
            return self.getTypedRuleContext(SimulatorParser.MapFunctionContext,0)


        def range_list(self):
            return self.getTypedRuleContext(SimulatorParser.Range_listContext,0)


        def getRuleIndex(self):
            return SimulatorParser.RULE_expression

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
        localctx = SimulatorParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 152
                self.constant()
                pass

            elif la_ == 2:
                self.state = 153
                self.match(SimulatorParser.NAME)
                pass

            elif la_ == 3:
                self.state = 154
                self.match(SimulatorParser.T__10)
                self.state = 155
                self.expression(0)
                self.state = 156
                self.match(SimulatorParser.T__11)
                pass

            elif la_ == 4:
                self.state = 158
                self.match(SimulatorParser.T__4)
                self.state = 159
                self.unnamed_expression_list()
                self.state = 160
                self.match(SimulatorParser.T__5)
                pass

            elif la_ == 5:
                self.state = 162
                self.methodCall()
                pass

            elif la_ == 6:
                self.state = 163
                self.objectMethodCall()
                pass

            elif la_ == 7:
                self.state = 164
                localctx.prefix = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 57600) != 0)):
                    localctx.prefix = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 165
                self.expression(13)
                pass

            elif la_ == 8:
                self.state = 166
                self.mapFunction()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 219
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 217
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = SimulatorParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 169
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 170
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 983040) != 0)):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 171
                        self.expression(13)
                        pass

                    elif la_ == 2:
                        localctx = SimulatorParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 172
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 173
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==8 or _la==15):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 174
                        self.expression(12)
                        pass

                    elif la_ == 3:
                        localctx = SimulatorParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 175
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 183
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                        if la_ == 1:
                            self.state = 176
                            self.match(SimulatorParser.T__19)
                            self.state = 177
                            self.match(SimulatorParser.T__19)
                            pass

                        elif la_ == 2:
                            self.state = 178
                            self.match(SimulatorParser.T__20)
                            self.state = 179
                            self.match(SimulatorParser.T__20)
                            self.state = 180
                            self.match(SimulatorParser.T__20)
                            pass

                        elif la_ == 3:
                            self.state = 181
                            self.match(SimulatorParser.T__20)
                            self.state = 182
                            self.match(SimulatorParser.T__20)
                            pass


                        self.state = 185
                        self.expression(11)
                        pass

                    elif la_ == 4:
                        localctx = SimulatorParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 186
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 187
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15728640) != 0)):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 188
                        self.expression(10)
                        pass

                    elif la_ == 5:
                        localctx = SimulatorParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 189
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 190
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==24 or _la==25):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 191
                        self.expression(9)
                        pass

                    elif la_ == 6:
                        localctx = SimulatorParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 192
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 193
                        localctx.bop = self.match(SimulatorParser.T__25)
                        self.state = 194
                        self.expression(8)
                        pass

                    elif la_ == 7:
                        localctx = SimulatorParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 195
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 196
                        localctx.bop = self.match(SimulatorParser.T__26)
                        self.state = 197
                        self.expression(7)
                        pass

                    elif la_ == 8:
                        localctx = SimulatorParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 198
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 199
                        localctx.bop = self.match(SimulatorParser.T__27)
                        self.state = 200
                        self.expression(6)
                        pass

                    elif la_ == 9:
                        localctx = SimulatorParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 201
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 202
                        localctx.bop = self.match(SimulatorParser.T__28)
                        self.state = 203
                        self.expression(5)
                        pass

                    elif la_ == 10:
                        localctx = SimulatorParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 204
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 205
                        localctx.bop = self.match(SimulatorParser.T__29)
                        self.state = 206
                        self.expression(4)
                        pass

                    elif la_ == 11:
                        localctx = SimulatorParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 207
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 208
                        localctx.bop = self.match(SimulatorParser.T__30)
                        self.state = 209
                        self.expression(3)
                        pass

                    elif la_ == 12:
                        localctx = SimulatorParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 210
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 211
                        self.match(SimulatorParser.T__4)
                        self.state = 212
                        self.range_list()
                        self.state = 213
                        self.match(SimulatorParser.T__5)
                        pass

                    elif la_ == 13:
                        localctx = SimulatorParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 215
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 216
                        localctx.postfix = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            localctx.postfix = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass

             
                self.state = 221
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        self._predicates[2] = self.relation_list_sempred
        self._predicates[18] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def relation_list_sempred(self, localctx:Relation_listContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 14)
         




