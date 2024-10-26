grammar PatitoParser;

options {
    tokenVocab = PatitoLexer;
}

programa : 
    PROGRAM ID SEMI tiene_variables tiene_funciones INICIO cuerpo FIN;
tiene_variables : vars?;
tiene_funciones : funcs*;
vars: VARS complemento_vars;
complemento_vars  : ID COMMA complemento_vars  | ID COLON tipo SEMI complemento_vars | ID COLON tipo SEMI ;
tipo : ENTERO | FLOTANTE;
funcs : NULA ID LPAREN complemento_funcs RPAREN LBRACE tiene_variables cuerpo RBRACE SEMI ;
complemento_funcs : (ID COLON tipo)? | (ID COLON tipo COMMA complemento_funcs)?;
cuerpo : LBRACE tiene_estatuto RBRACE;
tiene_estatuto : (estatuto tiene_estatuto)?;
estatuto : asigna | condicion | ciclo | llamada | imprime;
asigna : ID EQUAL expresion SEMI ;
expresion : exp complemento_expresion;
complemento_expresion : (GT exp | LT exp | MINUS exp | DEQ exp)? ;
exp : termino complemento_exp ;
complemento_exp : (PLUS exp | MINUS exp )? ;
termino : factor complemento_termino ;
complemento_termino : (MUL termino | DIV termino)?;
factor : LPAREN expresion RPAREN | tiene_signo tiene_var;
tiene_signo : ( PLUS | MINUS )? ;
tiene_var : ID | cte ;
cte : CTE_ENTERO | CTE_FLOTANTE ;
condicion : SI LPAREN expresion RPAREN HAZ cuerpo complemento_cond SEMI ;
complemento_cond : (SINO cuerpo )? ;
ciclo : MIENTRAS LPAREN expresion RPAREN HAZ cuerpo SEMI ;
llamada : ID LPAREN complemento_llamada RPAREN SEMI ;
complemento_llamada : (tiene_expresion)? ;
tiene_expresion : expresion | expresion COMMA tiene_expresion;
imprime : ESCRIBE LPAREN complemento_imprime RPAREN SEMI ;
complemento_imprime : expresion | CTE_LETRERO | expresion COMMA complemento_imprime | CTE_LETRERO COMMA complemento_imprime ;