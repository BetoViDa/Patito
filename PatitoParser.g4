grammar PatitoParser;

options {
    tokenVocab = PatitoLexer;
}

@members {
contadorentero = 1000
contadorflotante = 2000
contadorconstante = 3000
}

programa : PROGRAM ID 
{
self.nombrefuncion = $ID.text
self.funcdir.add_funcion($ID.text,"programa")
} SEMI tiene_variables tiene_funciones INICIO cuerpo FIN;

tiene_variables : vars?;
tiene_funciones : funcs*;

vars: VARS (complemento_vars 
{
partes = $complemento_vars.text.split(":")  
variables_separadas = partes[0].split(",")
tipo = partes[1]

for variable in variables_separadas: 
    if tipo == "entero":
        direccion = self.contadorentero
        self.funcdir.funciones[self.nombrefuncion]["tabla"].add_var(variable,tipo,direccion)
        self.contadorentero = self.contadorentero + 1
    elif tipo == "flotante":
        direccion = self.contadorflotante
        self.funcdir.funciones[self.nombrefuncion]["tabla"].add_var(variable,tipo,direccion)
        self.contadorflotante = self.contadorflotante + 1
    else:
        raise ValueError(f"Variable no identificada")
} SEMI )+ ;

complemento_vars  : ID (COMMA ID)* COLON tipo   ;
tipo : ENTERO | FLOTANTE;

funcs : NULA ID
{
self.nombrefuncion = $ID.text
self.funcdir.add_funcion($ID.text,"nula")
} LPAREN complemento_funcs
{
argumentos = $complemento_funcs.text.split(",")  
for argumento in argumentos: 
    arg_div = argumento.split(":")
    variable = arg_div[0]
    tipo = arg_div[1]
    if tipo == "entero":
        direccion = self.contadorentero
        self.funcdir.funciones[self.nombrefuncion]["tabla"].add_var(variable,tipo,direccion)
        self.contadorentero = self.contadorentero + 1
    elif tipo == "flotante":
        direccion = self.contadorflotante
        self.funcdir.funciones[self.nombrefuncion]["tabla"].add_var(variable,tipo,direccion)
        self.contadorflotante = self.contadorflotante + 1
    else:
        raise ValueError(f"Variable no identificada")
} RPAREN LBRACE tiene_variables cuerpo RBRACE SEMI ;

complemento_funcs : (ID COLON tipo)? | (ID COLON tipo COMMA complemento_funcs)?;
cuerpo : LBRACE tiene_estatuto RBRACE;
tiene_estatuto : (estatuto tiene_estatuto)?;
estatuto : asigna | condicion | ciclo | llamada | imprime;

asigna : ID EQUAL expresion
{
asignar = $ID.text
asignar_dir = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(asignar)
op = self.cuadruplo.pop_operating()
op_dir = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(op)
self.cuadruplo.add_assign_Cuadruplo(self.semantic["="]["codigo"],op_dir,asignar_dir)
} SEMI ;

expresion : exp complemento_expresion;
complemento_expresion : (exp_logicas exp
{
temp = self.cuadruplo.nuevo_temp()
operador = self.cuadruplo.pop_operator()
op2 = self.cuadruplo.pop_operating()
op2_dir = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(op2)
op1 = self.cuadruplo.pop_operating()
op1_dir = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(op1)
direccion = self.contadorconstante
tempadd = self.funcdir.funciones[self.nombrefuncion]["tabla"].add_constante(temp,"temp",direccion)
self.contadorconstante = direccion + 1
self.cuadruplo.add_Cuadruplo(self.semantic[operador]["codigo"],op1_dir,op2_dir,direccion)
self.cuadruplo.push_operating(direccion)
} )? ;
exp_logicas : GT
{
self.cuadruplo.push_operator('>')
} | LT
{
self.cuadruplo.push_operator('<')
} | NEQ
{
self.cuadruplo.push_operator('!=')
} | DEQ
{
self.cuadruplo.push_operator('==')
} ;

exp : termino (exp_signo
{
self.cuadruplo.push_operator($exp_signo.text);
} termino 
{
temp = self.cuadruplo.nuevo_temp()
operador = self.cuadruplo.pop_operator()
op2 = self.cuadruplo.pop_operating()
op2_dir = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(op2)
op1 = self.cuadruplo.pop_operating()
op1_dir = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(op1)
direccion = self.contadorconstante
tempadd = self.funcdir.funciones[self.nombrefuncion]["tabla"].add_constante(temp,"temp",direccion)
self.contadorconstante = direccion + 1
self.cuadruplo.add_Cuadruplo(self.semantic[operador]["codigo"],op1_dir,op2_dir,direccion)
self.cuadruplo.push_operating(direccion)
}
)*;
exp_signo: (PLUS | MINUS) ;

termino : factor (  term_signo
{
self.cuadruplo.push_operator($term_signo.text);
} factor 
{
temp = self.cuadruplo.nuevo_temp()
operador = self.cuadruplo.pop_operator()
op2 = self.cuadruplo.pop_operating()
op2_dir = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(op2)
op1 = self.cuadruplo.pop_operating()
op1_dir = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(op1)
direccion = self.contadorconstante
tempadd = self.funcdir.funciones[self.nombrefuncion]["tabla"].add_constante(temp,"temp",direccion)
self.contadorconstante = direccion + 1
self.cuadruplo.add_Cuadruplo(self.semantic[operador]["codigo"],op1_dir,op2_dir,direccion)
self.cuadruplo.push_operating(direccion)
}
)*;
term_signo: (MUL | DIV);


factor : LPAREN expresion RPAREN | factor_operaciones
{
self.cuadruplo.push_operating($factor_operaciones.text)
};
factor_operaciones: tiene_signo? tiene_var
{
val = $tiene_var.text
signo = $tiene_signo.text
llave = self.funcdir.funciones[self.nombrefuncion]["tabla"].buscar_var(val)
val_dir = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(val)
if signo:
    if signo == "-":
        newval = signo + val
        self.funcdir.funciones[self.nombrefuncion]["tabla"].editar_val_por_direccion(val_dir,newval)
    else: 
        newval = signo + val
        self.funcdir.funciones[self.nombrefuncion]["tabla"].editar_val_por_direccion(val_dir,newval)
} ;
tiene_signo : PLUS | MINUS ;
tiene_var : ID
{
if not self.funcdir.funciones[self.nombrefuncion]["tabla"].buscar_var($ID.text):
    raise Exception(f"Varible {$ID.text} no declarada")
} | cte ;

cte : CTE_ENTERO
{
direccion = self.contadorconstante
self.contadorconstante = direccion + 1
self.funcdir.funciones[self.nombrefuncion]["tabla"].add_constante($CTE_ENTERO.text,"entero",direccion)
} | CTE_FLOTANTE 
{
direccion = self.contadorconstante
self.contadorconstante = direccion + 1
self.funcdir.funciones[self.nombrefuncion]["tabla"].add_constante($CTE_FLOTANTE.text,"flotante",direccion)
};

condicion : SI LPAREN expresion RPAREN
{
falso = self.cuadruplo.nuevo_label()
op =self.cuadruplo.pop_operating()
self.cuadruplo.add_conditional_jump(op,falso)
self.cuadruplo.push_jump(falso)
} HAZ cuerpo complemento_cond SEMI
{
final = self.cuadruplo.pop_jump()
cuentafinal = self.cuadruplo.get_current_count()
self.cuadruplo.edit_Cuadruplo_by_label(final,cuentafinal) 
} ;

complemento_cond : (SINO
{
bypass = self.cuadruplo.nuevo_label()
self.cuadruplo.add_by_pass_jump(bypass)
salto = self.cuadruplo.pop_jump()
self.cuadruplo.push_jump(bypass)
cuentaelse = self.cuadruplo.get_current_count()
self.cuadruplo.edit_Cuadruplo_by_label(salto,cuentaelse)
} cuerpo )? ;

ciclo : MIENTRAS LPAREN expresion RPAREN HAZ
{
falso = self.cuadruplo.nuevo_label()
op = self.cuadruplo.peek_operating()
cicloInd = self.cuadruplo.get_current_count()
self.cuadruplo.add_conditional_jump(op,falso)
self.cuadruplo.push_jump(falso)
self.cuadruplo.push_jump(cicloInd)
} cuerpo SEMI
{
op = self.cuadruplo.pop_operating()
salto = self.cuadruplo.pop_jump()
self.cuadruplo.add_cycle_jump(op,salto)
cuentafinal = self.cuadruplo.get_current_count()
salto = self.cuadruplo.pop_jump()
self.cuadruplo.edit_Cuadruplo_by_label(salto,cuentafinal) 
} ;

llamada : ID LPAREN complemento_llamada RPAREN SEMI ;
complemento_llamada : (tiene_expresion)? ;
tiene_expresion : expresion | expresion COMMA tiene_expresion;

imprime : ESCRIBE LPAREN complemento_imprime RPAREN SEMI ;
complemento_imprime : expresion
{
val = self.cuadruplo.pop_operating()
add = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(val)
self.cuadruplo.add_print_Cuadruplo(add)
} complemento_imprime_aux | CTE_LETRERO
{
direccion = self.contadorconstante
val = self.funcdir.funciones[self.nombrefuncion]["tabla"].add_constante($CTE_LETRERO,"letrero",direccion)
self.contadorconstante = direccion + 1
add = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(direccion)
self.cuadruplo.add_print_Cuadruplo(add)
} complemento_imprime_aux;
complemento_imprime_aux : ( COMMA complemento_imprime)*;