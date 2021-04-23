# Generated from /home/andreea/PycharmProjects/tema3LFA/GrammarER.g4 by ANTLR 4.9
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("\61\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\7\2\21\n\2\f\2\16\2\24\13\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\7\3\33\n\3\f\3\16\3\36\13\3\3\4\3\4\3\4\3\4\3\4\7\4%")
        buf.write("\n\4\f\4\16\4(\13\4\3\5\3\5\3\5\3\5\3\5\5\5/\n\5\3\5\2")
        buf.write("\5\2\4\6\6\2\4\6\b\2\2\2\60\2\n\3\2\2\2\4\25\3\2\2\2\6")
        buf.write("\37\3\2\2\2\b.\3\2\2\2\n\13\b\2\1\2\13\f\5\4\3\2\f\22")
        buf.write("\3\2\2\2\r\16\f\4\2\2\16\17\7\4\2\2\17\21\5\4\3\2\20\r")
        buf.write("\3\2\2\2\21\24\3\2\2\2\22\20\3\2\2\2\22\23\3\2\2\2\23")
        buf.write("\3\3\2\2\2\24\22\3\2\2\2\25\26\b\3\1\2\26\27\5\6\4\2\27")
        buf.write("\34\3\2\2\2\30\31\f\4\2\2\31\33\5\6\4\2\32\30\3\2\2\2")
        buf.write("\33\36\3\2\2\2\34\32\3\2\2\2\34\35\3\2\2\2\35\5\3\2\2")
        buf.write("\2\36\34\3\2\2\2\37 \b\4\1\2 !\5\b\5\2!&\3\2\2\2\"#\f")
        buf.write("\4\2\2#%\7\3\2\2$\"\3\2\2\2%(\3\2\2\2&$\3\2\2\2&\'\3\2")
        buf.write("\2\2\'\7\3\2\2\2(&\3\2\2\2)*\7\5\2\2*+\5\2\2\2+,\7\6\2")
        buf.write("\2,/\3\2\2\2-/\7\7\2\2.)\3\2\2\2.-\3\2\2\2/\t\3\2\2\2")
        buf.write("\6\22\34&.")
        return buf.getvalue()


class GrammarERParser ( Parser ):

    grammarFileName = "GrammarER.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'|'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "KLEENE", "OR", "OPEN", "CLOSE", "VAR", 
                      "WS" ]

    RULE_orr = 0
    RULE_concat = 1
    RULE_kleene = 2
    RULE_gramm = 3

    ruleNames =  [ "orr", "concat", "kleene", "gramm" ]

    EOF = Token.EOF
    KLEENE=1
    OR=2
    OPEN=3
    CLOSE=4
    VAR=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class OrrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def concat(self):
            return self.getTypedRuleContext(GrammarERParser.ConcatContext,0)


        def orr(self):
            return self.getTypedRuleContext(GrammarERParser.OrrContext,0)


        def OR(self):
            return self.getToken(GrammarERParser.OR, 0)

        def getRuleIndex(self):
            return GrammarERParser.RULE_orr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrr" ):
                listener.enterOrr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrr" ):
                listener.exitOrr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrr" ):
                return visitor.visitOrr(self)
            else:
                return visitor.visitChildren(self)



    def orr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarERParser.OrrContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_orr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self.concat(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 16
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarERParser.OrrContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_orr)
                    self.state = 11
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 12
                    self.match(GrammarERParser.OR)
                    self.state = 13
                    self.concat(0) 
                self.state = 18
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConcatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kleene(self):
            return self.getTypedRuleContext(GrammarERParser.KleeneContext,0)


        def concat(self):
            return self.getTypedRuleContext(GrammarERParser.ConcatContext,0)


        def getRuleIndex(self):
            return GrammarERParser.RULE_concat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcat" ):
                listener.enterConcat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcat" ):
                listener.exitConcat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcat" ):
                return visitor.visitConcat(self)
            else:
                return visitor.visitChildren(self)



    def concat(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarERParser.ConcatContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_concat, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.kleene(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 26
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarERParser.ConcatContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_concat)
                    self.state = 22
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 23
                    self.kleene(0) 
                self.state = 28
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class KleeneContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def gramm(self):
            return self.getTypedRuleContext(GrammarERParser.GrammContext,0)


        def kleene(self):
            return self.getTypedRuleContext(GrammarERParser.KleeneContext,0)


        def KLEENE(self):
            return self.getToken(GrammarERParser.KLEENE, 0)

        def getRuleIndex(self):
            return GrammarERParser.RULE_kleene

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKleene" ):
                listener.enterKleene(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKleene" ):
                listener.exitKleene(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKleene" ):
                return visitor.visitKleene(self)
            else:
                return visitor.visitChildren(self)



    def kleene(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarERParser.KleeneContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_kleene, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.gramm()
            self._ctx.stop = self._input.LT(-1)
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarERParser.KleeneContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_kleene)
                    self.state = 32
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 33
                    self.match(GrammarERParser.KLEENE) 
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class GrammContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self):
            return self.getToken(GrammarERParser.OPEN, 0)

        def orr(self):
            return self.getTypedRuleContext(GrammarERParser.OrrContext,0)


        def CLOSE(self):
            return self.getToken(GrammarERParser.CLOSE, 0)

        def VAR(self):
            return self.getToken(GrammarERParser.VAR, 0)

        def getRuleIndex(self):
            return GrammarERParser.RULE_gramm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGramm" ):
                listener.enterGramm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGramm" ):
                listener.exitGramm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGramm" ):
                return visitor.visitGramm(self)
            else:
                return visitor.visitChildren(self)




    def gramm(self):

        localctx = GrammarERParser.GrammContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_gramm)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarERParser.OPEN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(GrammarERParser.OPEN)
                self.state = 40
                self.orr(0)
                self.state = 41
                self.match(GrammarERParser.CLOSE)
                pass
            elif token in [GrammarERParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.match(GrammarERParser.VAR)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.orr_sempred
        self._predicates[1] = self.concat_sempred
        self._predicates[2] = self.kleene_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def orr_sempred(self, localctx:OrrContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def concat_sempred(self, localctx:ConcatContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def kleene_sempred(self, localctx:KleeneContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




