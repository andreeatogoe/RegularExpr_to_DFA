from gen.GrammarERVisitor import GrammarERVisitor
from gen.GrammarERParser import GrammarERParser
from mainNFA import NFA


class GrammarEvalVisitor(GrammarERVisitor):

    def visitGramm(self, ctx: GrammarERParser.GrammContext):
        var = ctx.VAR()
        if var:
            return NFA(2, set(str(var)), [1], {(0, str(var)): [1]})
        exp = ctx.orr()
        return self.visit(exp)

    def visitKleene(self, ctx: GrammarERParser.KleeneContext):
        exp1 = ctx.kleene()
        if exp1:
            nfa = self.visit(exp1)
            nfa.state_nr_update(1)
            nr = nfa.nrOfStates + 2
            final_state = nr - 1
            new_delta = {(0, ''): [nfa.initialState, final_state]}

            new_delta.update(nfa.delta)

            for i in nfa.finalStates:
                aux = (i, '')
                new_delta[aux] = [final_state, nfa.initialState]

            return NFA(nr, nfa.alphabet, [final_state],  new_delta)
        exp2 = ctx.gramm()
        return self.visit(exp2)

    def visitConcat(self, ctx: GrammarERParser.ConcatContext):
        exp1 = ctx.concat()
        exp2 = ctx.kleene()

        if exp1:
            nfa1 = self.visit(exp1)
            nfa2 = self.visit(exp2)
            nfa2.state_nr_update(nfa1.nrOfStates - 1)
            nr = nfa1.nrOfStates + nfa2.nrOfStates - 1
            nfa1.delta.update(nfa2.delta)
            return NFA(nr, set().union(nfa1.alphabet, nfa2.alphabet), nfa2.finalStates, nfa1.delta)

        return self.visit(exp2)

    def visitOrr(self, ctx: GrammarERParser.OrrContext):
        exp1 = ctx.orr()
        exp2 = ctx.concat()
        if exp1:
            nfa1 = self.visit(exp1)
            nfa1.state_nr_update(1)

            nfa2 = self.visit(exp2)
            nfa2.state_nr_update(nfa1.nrOfStates + 1)

            nr = nfa1.nrOfStates + nfa2.nrOfStates + 2
            final_state = nr - 1

            new_delta = {(0, ''): [1, nfa1.nrOfStates + 1]}
            new_delta.update(nfa1.delta)

            for i in nfa1.finalStates:
                aux = (i, '')
                new_delta[aux] = [final_state]

            new_delta.update(nfa2.delta)

            for i in nfa2.finalStates:
                aux = (i, '')
                new_delta[aux] = [final_state]

            return NFA(nr, nfa1.alphabet.union(nfa2.alphabet), [final_state], new_delta)

        return self.visit(exp2)


