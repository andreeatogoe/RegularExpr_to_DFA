from GrammarEvalVisitor import GrammarEvalVisitor
from gen.GrammarERLexer import GrammarERLexer
from gen.GrammarERParser import GrammarERParser
from antlr4 import FileStream, CommonTokenStream
import sys
from mainNFA import NFA

if __name__ == '__main__':
    file_stream = FileStream(sys.argv[1])
    lexer = GrammarERLexer(file_stream)
    tokens = CommonTokenStream(lexer)
    parser = GrammarERParser(tokens)

    tree = parser.orr()

    if not tree:
        raise Exception('upss')

    visitor = GrammarEvalVisitor()
    rez = visitor.visit(tree)

    with open(sys.argv[2], 'w') as f:
        print(str(rez), file=f)

    rez.nfa_to_dfa()

