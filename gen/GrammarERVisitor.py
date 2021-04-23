# Generated from /home/andreea/PycharmProjects/tema3LFA/GrammarER.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarERParser import GrammarERParser
else:
    from GrammarERParser import GrammarERParser

# This class defines a complete generic visitor for a parse tree produced by GrammarERParser.

class GrammarERVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarERParser#orr.
    def visitOrr(self, ctx:GrammarERParser.OrrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarERParser#concat.
    def visitConcat(self, ctx:GrammarERParser.ConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarERParser#kleene.
    def visitKleene(self, ctx:GrammarERParser.KleeneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarERParser#gramm.
    def visitGramm(self, ctx:GrammarERParser.GrammContext):
        return self.visitChildren(ctx)



del GrammarERParser