# TOGOE ANDREEA 322CB
import sys
from typing import List, Tuple, Set, Dict

State = int
Word = str
Configuration = Tuple[State, Word]
Transition = Tuple[State, Word, List[State]]
EPSILON = ""


class NFA:
    def __init__(self, nrOfStates: int, alphabet: Set[chr], finalStates: Set[State],
                 delta: Dict[Tuple[State, chr], Set[State]]):
        self.nrOfStates = nrOfStates
        self.states = set(range(self.nrOfStates))
        self.alphabet = alphabet
        self.initialState = 0
        self.finalStates = finalStates
        self.delta = delta

    def state_nr_update(self, nr):
        new_delta = {}
        for tranz in self.delta:
            aux1 = tranz[0]
            aux2 = tranz[1]
            new_tranz = tuple([(aux1 + nr), aux2])
            new_set = []
            for i in self.delta[tranz]:
                new_set.append(i + nr)
            new_delta[new_tranz] = new_set

        self.delta = new_delta
        self.initialState += nr;
        for i in range(len(self.finalStates)):
            self.finalStates[i] += nr



    def __str__(self):
        nfa = str(self.nrOfStates) + "\n"
        for i in self.finalStates:
            nfa += str(i)
            nfa += ' '

        nfa += '\n'
        for i in self.delta:
            nfa += str(i[0])
            nfa += ' '
            if str(i[1]) == '':
                nfa += 'eps'
            else:
                nfa += str(i[1])
            nfa += ' '
            for j in self.delta[i]:
                nfa += str(j)
                nfa += ' '
            nfa += '\n'

        return nfa

    def nfa_to_dfa(self):


        with open(sys.argv[2], "r") as file:
            numberOfStates = int(file.readline().rstrip())
            finalStates = set(map(int, file.readline().rstrip().split(" ")))
            delta = dict()
            while True:
                transition = file.readline().rstrip().split(" ")
                if transition == ['']:
                    break
                if transition[1] == "eps":
                    transition[1] = EPSILON

                delta[(int(transition[0]), transition[1])] = set(map(int, transition[2:]))

            nfa = NFA(
                nrOfStates=numberOfStates,
                finalStates=finalStates,
                delta=delta,
                alphabet=set()
            )

		# extrag alfabetul (fara epsilon)
            for i in delta:
                if i[1]:
                    nfa.alphabet.add(i[1])

		# calculez E(q) pt fiecare stare a nfa-ului
            eps = [set() for _ in range(nfa.nrOfStates)]
            for i in range(nfa.nrOfStates):
                eps[i].add(i);
                if ((i, '') in nfa.delta):
                    eps[i].update(nfa.delta[(i, '')])
                    queue = list(nfa.delta[(i, '')])

                    while queue:

                        elem = queue.pop(0)
                        if (elem, '') in nfa.delta:

                            for k in nfa.delta[(elem, '')]:
                                if k not in eps[i]:
                                    queue.append(k)
                                    eps[i].add(k)

        # declar variabile pentru campurile unui dfa
            nr_of_dfa_states = 1
            states_dfa = [0]
            delta_dfa = {}
            dfa_alphabet = nfa.alphabet
            final_dfa_states = set()
            waiting_queue = [eps[0]]

        #   introduc fiecare stare intalnita in waiting_queue, dupa care o procesez folosindu ma
        # de nfa.delta si eps
            while (waiting_queue):
                state = waiting_queue.pop(0)

                for x in dfa_alphabet:
                    next = set()
                    for a in state:
                        if ((a, x) in nfa.delta):
                            for j in nfa.delta[(a, x)]:
                                next.add(j)
                                if len(eps[j]) > 1:
                                    for k in eps[j]:
                                        if (k != j):
                                            next.add(k)

                    if (not next in states_dfa):
                        waiting_queue.append(next)
                        states_dfa.append(next)

                    tup = tuple(state)
                    delta_dfa[(tup, x)] = next

            nr_of_dfa_states = len(states_dfa)
            final_dfa_delta = {}
        # creez un dictionar unde asociez starilor compuse cate o val numerica
        # si totodata alcatuiesc multimea de stari finale
            states_dict = {}
            nr = 0

            for i in delta_dfa:

                if i[0] not in states_dict:
                    states_dict[i[0]] = nr
                    for k in i[0]:
                        if k in nfa.finalStates:
                            final_dfa_states.add(nr)
                            break
                    nr += 1

                if tuple(delta_dfa[i]) not in states_dict:
                    states_dict[tuple(delta_dfa[i])] = nr
                    for k in tuple(delta_dfa[i]):
                        if k in nfa.finalStates:
                            final_dfa_states.add(nr)
                            break
                    nr += 1

            good_delta = {}
            for i in delta_dfa:
                good_delta[(states_dict[i[0]], i[1])] = states_dict[tuple(delta_dfa[i])]

            w = open(sys.argv[3], "w")
            w.write(str(nr_of_dfa_states))
            w.write("\n")
            for i in final_dfa_states:
                w.write(str(i))
                w.write(" ")

            w.write("\n")

        for i in good_delta:
            w.write(str(i[0]))
            w.write(" ")
            w.write(i[1])
            w.write(" ")
            w.write(str(good_delta[i]))
            w.write("\n")

        w.close()
		