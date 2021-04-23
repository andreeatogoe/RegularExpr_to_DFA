grammar GrammarER;

KLEENE: '*';
OR: '|';
OPEN: '(';
CLOSE: ')';
VAR: [a-z];
WS: [ \t\r\n]+ -> skip;

orr : orr OR concat | concat;
concat : concat kleene | kleene;
kleene : kleene KLEENE | gramm;
gramm : OPEN orr CLOSE | VAR;