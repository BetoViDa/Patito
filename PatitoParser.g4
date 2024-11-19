grammar PatitoParser;

options {
    tokenVocab = PatitoLexer;
}

@members {
contadorenteroglobal = 1000
contadorflotanteglobal = 3000

contadorenterotemporal = 5000
contadorflotantetemporal = 7500

contadorenterolocal = 10000
contadorflotantelocal = 12500

contadorenteroconstante = 15000
contadorflotanteconstante = 20000
contadorletreroconstante = 25000

}

programa : PROGRAM ID 
{
self.nombrefuncion = $ID.text
self.funcdir.add_funcion($ID.text,"programa")
} SEMI tiene_variables tiene_funciones INICIO cuerpo FIN
{
self.cuadruplo.add_end_Cuadruplo()
};

tiene_variables : vars?;
tiene_funciones : funcs*;

vars: VARS (complemento_vars 
{
partes = $complemento_vars.text.split(":")  
variables_separadas = partes[0].split(",")
tipo = partes[1]

for variable in variables_separadas: 
    if tipo == "entero":
        direccion = self.contadorenteroglobal
        self.funcdir.funciones[self.nombrefuncion]["tabla"].add_var(variable,tipo,direccion)
        self.contadorenteroglobal = self.contadorenteroglobal + 1
    elif tipo == "flotante":
        direccion = self.contadorflotanteglobal
        self.funcdir.funciones[self.nombrefuncion]["tabla"].add_var(variable,tipo,direccion)
        self.contadorflotante = self.contadorflotanteglobal + 1
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
        direccion = self.contadorenterolocal
        self.funcdir.funciones[self.nombrefuncion]["tabla"].add_var(variable,tipo,direccion)
        self.contadorenterolocal = self.contadorenterolocal + 1
    elif tipo == "flotante":
        direccion = self.contadorflotantelocal
        self.funcdir.funciones[self.nombrefuncion]["tabla"].add_var(variable,tipo,direccion)
        self.contadorflotantelocal = self.contadorflotantelocal + 1
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
op = self.cuadruplo.peek_operating()
op_dir = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(op)
if not op_dir:
    op_dir = self.constantes.get_direccion(op)
self.cuadruplo.add_assign_Cuadruplo(self.semantic["="]["codigo"],op_dir,asignar_dir)
} SEMI ;

expresion : exp complemento_expresion;
complemento_expresion : (exp_logicas exp
{
temp = self.cuadruplo.nuevo_temp()
operador = self.cuadruplo.pop_operator()

op2 = self.cuadruplo.pop_operating()
op2_tipo = self.cuadruplo.pop_type()
op2_dir = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(op2)
if not op2_dir:
    op2_dir = self.constantes.get_direccion(op2)

op1 = self.cuadruplo.pop_operating()
op1_tipo = self.cuadruplo.pop_type()
op1_dir = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(op1)
if not op1_dir:
    op1_dir = self.constantes.get_direccion(op1)

temp_tipo = self.semantic[operador][op1_tipo][op2_tipo]
if temp_tipo == "entero":
    direccion = self.contadorenterotemporal
    self.contadorenterotemporal = direccion + 1
else:
    direccion = self.contadorflotantetemporal
    self.contadorflotantetemporal = direccion + 1

tempadd = self.funcdir.funciones[self.nombrefuncion]["tabla"].add_temp(temp,temp_tipo,direccion)
self.cuadruplo.add_Cuadruplo(self.semantic[operador]["codigo"],op1_dir,op2_dir,direccion)
self.cuadruplo.push_operating(direccion)
self.cuadruplo.push_type(temp_tipo)
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
op2_tipo = self.cuadruplo.pop_type()
op2_dir = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(op2)
if not op2_dir:
    op2_dir = self.constantes.get_direccion(op2)

op1 = self.cuadruplo.pop_operating()
op1_tipo = self.cuadruplo.pop_type()
op1_dir = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(op1)
if not op1_dir:
    op1_dir = self.constantes.get_direccion(op1)

temp_tipo = self.semantic[operador][op1_tipo][op2_tipo]
if temp_tipo == "entero":
    direccion = self.contadorenterotemporal
    self.contadorenterotemporal = direccion + 1
else:
    direccion = self.contadorflotantetemporal
    self.contadorflotantetemporal = direccion + 1
    
tempadd = self.funcdir.funciones[self.nombrefuncion]["tabla"].add_temp(temp,temp_tipo,direccion)
self.cuadruplo.add_Cuadruplo(self.semantic[operador]["codigo"],op1_dir,op2_dir,direccion)
self.cuadruplo.push_operating(direccion)
self.cuadruplo.push_type(temp_tipo)
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
op2_tipo = self.cuadruplo.pop_type()
op2_dir = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(op2)
if not op2_dir:
    op2_dir = self.constantes.get_direccion(op2)

op1 = self.cuadruplo.pop_operating()
op1_tipo = self.cuadruplo.pop_type()
op1_dir = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(op1)
if not op1_dir:
    op1_dir = self.constantes.get_direccion(op1)

temp_tipo = self.semantic[operador][op1_tipo][op2_tipo]
if temp_tipo == "entero":
    direccion = self.contadorenterotemporal
    self.contadorenterotemporal = direccion + 1
else:
    direccion = self.contadorflotantetemporal
    self.contadorflotantetemporal = direccion + 1
    
tempadd = self.funcdir.funciones[self.nombrefuncion]["tabla"].add_temp(temp,temp_tipo,direccion)
self.cuadruplo.add_Cuadruplo(self.semantic[operador]["codigo"],op1_dir,op2_dir,direccion)
self.cuadruplo.push_operating(direccion)
self.cuadruplo.push_type(temp_tipo)
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

if not val.startswith("&"):
    val_dir = self.constantes.get_direccion(val)
    val_tipo = self.cuadruplo.pop_type()
    if signo:
        if signo == "-":
            self.constantes.add_constante("-{val}",val_tipo,val_dir)
        else: 
            self.constantes.add_constante("+{val}",val_tipo,val_dir)
else:
    val_dir = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(val)
    val_tipo = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_tipo(val)
    if signo:
        if signo == "-":
            newval = signo + val
            self.funcdir.funciones[self.nombrefuncion]["tabla"].editar_val_por_direccion(val_dir,newval)
        else: 
            newval = signo + val
            self.funcdir.funciones[self.nombrefuncion]["tabla"].editar_val_por_direccion(val_dir,newval)

self.cuadruplo.push_type(val_tipo)
} ;
tiene_signo : PLUS | MINUS ;
tiene_var : ID
{
if not self.funcdir.funciones[self.nombrefuncion]["tabla"].buscar_var($ID.text):
    raise Exception(f"Varible {$ID.text} no declarada")
} | cte ;

cte : CTE_ENTERO
{
direccion = self.contadorenteroconstante
self.contadorenteroconstante = direccion + 1
self.constantes.add_constante($CTE_ENTERO.text,"entero",direccion)
self.cuadruplo.push_type("entero")
} | CTE_FLOTANTE 
{
direccion = self.contadorflotanteconstante
self.contadorflotanteconstante = direccion + 1
self.constantes.add_constante($CTE_FLOTANTE.text,"flotante",direccion)
self.cuadruplo.push_type("flotante")
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
if not add:
    add = self.constantes.get_direccion(val)
self.cuadruplo.add_print_Cuadruplo(add)
} complemento_imprime_aux | CTE_LETRERO
{
direccion = self.contadorletreroconstante
val = self.constantes.add_constante($CTE_LETRERO.text,"letrero",direccion)
self.contadorletreroconstante = direccion + 1
add = self.constantes.get_direccion(direccion)
self.cuadruplo.add_print_Cuadruplo(add)
} complemento_imprime_aux;
complemento_imprime_aux : ( COMMA complemento_imprime)*;