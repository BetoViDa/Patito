lexer grammar PatitoLexer;

// Reglas Léxicas (Lexer Rules)
ID : '&' [a-zA-Z0-9]+ ;
CTE_LETRERO : '"' (.)*? '"' ;
CTE_ENTERO : [0-9]+ ;
CTE_FLOTANTE : [0-9]+ '.' [0-9]+ ;

// Palabras clave
PROGRAM : 'programa' ;
NULA : 'nula' ;
INICIO : 'inicio' ;
MIENTRAS : 'mientras' ;
SI : 'si' ;
SINO : 'sino' ;
ENTERO : 'entero' ;
FLOTANTE : 'flotante' ;
ESCRIBE : 'escribe' ;
IMPRIME : 'imprime' ;
FIN : 'fin' ;
VARS : 'vars' ;
HAZ : 'haz' ;

// Símbolos y operadores
LPAREN : '(' ;
RPAREN : ')' ;
LBRACE : '{' ;
RBRACE : '}' ;
COMMA : ',' ;
SEMI : ';' ;
COLON : ':' ;
PLUS : '+' ;
MINUS : '-' ;
MUL : '*' ;
DIV : '/' ;
EQUAL: '=' ;
NEQ : '!=' ;
DEQ : '==' ;
LT : '<' ;
GT : '>' ;

// Ignorar espacios y comentarios
WS : [ \t\r\n]+ -> skip ;
