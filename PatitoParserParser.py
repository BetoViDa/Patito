# Generated from D:/Mty/Compis/patito/PatitoParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,34,297,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,3,1,79,8,1,1,2,5,2,82,
        8,2,10,2,12,2,85,9,2,1,3,1,3,1,3,1,3,1,3,4,3,92,8,3,11,3,12,3,93,
        1,4,1,4,1,4,5,4,99,8,4,10,4,12,4,102,9,4,1,4,1,4,1,4,1,5,1,5,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,3,7,
        125,8,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,133,8,7,3,7,135,8,7,1,8,1,8,
        1,8,1,8,1,9,1,9,1,9,3,9,144,8,9,1,10,1,10,1,10,1,10,1,10,3,10,151,
        8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,13,
        1,13,3,13,166,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,
        176,8,14,1,15,1,15,1,15,1,15,1,15,1,15,5,15,184,8,15,10,15,12,15,
        187,9,15,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,5,17,197,8,17,10,
        17,12,17,200,9,17,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,
        19,211,8,19,1,20,3,20,214,8,20,1,20,1,20,1,20,1,21,1,21,1,22,1,22,
        1,22,3,22,224,8,22,1,23,1,23,1,23,1,23,3,23,230,8,23,1,24,1,24,1,
        24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,3,25,246,
        8,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,27,
        1,27,1,27,1,27,1,27,1,27,1,28,3,28,266,8,28,1,29,1,29,1,29,1,29,
        1,29,3,29,273,8,29,1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,
        1,31,1,31,1,31,1,31,3,31,288,8,31,1,32,1,32,5,32,292,8,32,10,32,
        12,32,295,9,32,1,32,0,0,33,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,0,3,1,0,
        11,12,1,0,25,26,1,0,27,28,290,0,66,1,0,0,0,2,78,1,0,0,0,4,83,1,0,
        0,0,6,86,1,0,0,0,8,95,1,0,0,0,10,106,1,0,0,0,12,108,1,0,0,0,14,134,
        1,0,0,0,16,136,1,0,0,0,18,143,1,0,0,0,20,150,1,0,0,0,22,152,1,0,
        0,0,24,158,1,0,0,0,26,165,1,0,0,0,28,175,1,0,0,0,30,177,1,0,0,0,
        32,188,1,0,0,0,34,190,1,0,0,0,36,201,1,0,0,0,38,210,1,0,0,0,40,213,
        1,0,0,0,42,218,1,0,0,0,44,223,1,0,0,0,46,229,1,0,0,0,48,231,1,0,
        0,0,50,245,1,0,0,0,52,247,1,0,0,0,54,258,1,0,0,0,56,265,1,0,0,0,
        58,272,1,0,0,0,60,274,1,0,0,0,62,287,1,0,0,0,64,293,1,0,0,0,66,67,
        5,5,0,0,67,68,5,1,0,0,68,69,6,0,-1,0,69,70,5,23,0,0,70,71,3,2,1,
        0,71,72,3,4,2,0,72,73,5,7,0,0,73,74,3,16,8,0,74,75,5,15,0,0,75,76,
        6,0,-1,0,76,1,1,0,0,0,77,79,3,6,3,0,78,77,1,0,0,0,78,79,1,0,0,0,
        79,3,1,0,0,0,80,82,3,12,6,0,81,80,1,0,0,0,82,85,1,0,0,0,83,81,1,
        0,0,0,83,84,1,0,0,0,84,5,1,0,0,0,85,83,1,0,0,0,86,91,5,16,0,0,87,
        88,3,8,4,0,88,89,6,3,-1,0,89,90,5,23,0,0,90,92,1,0,0,0,91,87,1,0,
        0,0,92,93,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,7,1,0,0,0,95,100,
        5,1,0,0,96,97,5,22,0,0,97,99,5,1,0,0,98,96,1,0,0,0,99,102,1,0,0,
        0,100,98,1,0,0,0,100,101,1,0,0,0,101,103,1,0,0,0,102,100,1,0,0,0,
        103,104,5,24,0,0,104,105,3,10,5,0,105,9,1,0,0,0,106,107,7,0,0,0,
        107,11,1,0,0,0,108,109,5,6,0,0,109,110,5,1,0,0,110,111,6,6,-1,0,
        111,112,5,18,0,0,112,113,3,14,7,0,113,114,6,6,-1,0,114,115,5,19,
        0,0,115,116,5,20,0,0,116,117,3,2,1,0,117,118,3,16,8,0,118,119,5,
        21,0,0,119,120,5,23,0,0,120,13,1,0,0,0,121,122,5,1,0,0,122,123,5,
        24,0,0,123,125,3,10,5,0,124,121,1,0,0,0,124,125,1,0,0,0,125,135,
        1,0,0,0,126,127,5,1,0,0,127,128,5,24,0,0,128,129,3,10,5,0,129,130,
        5,22,0,0,130,131,3,14,7,0,131,133,1,0,0,0,132,126,1,0,0,0,132,133,
        1,0,0,0,133,135,1,0,0,0,134,124,1,0,0,0,134,132,1,0,0,0,135,15,1,
        0,0,0,136,137,5,20,0,0,137,138,3,18,9,0,138,139,5,21,0,0,139,17,
        1,0,0,0,140,141,3,20,10,0,141,142,3,18,9,0,142,144,1,0,0,0,143,140,
        1,0,0,0,143,144,1,0,0,0,144,19,1,0,0,0,145,151,3,22,11,0,146,151,
        3,48,24,0,147,151,3,52,26,0,148,151,3,54,27,0,149,151,3,60,30,0,
        150,145,1,0,0,0,150,146,1,0,0,0,150,147,1,0,0,0,150,148,1,0,0,0,
        150,149,1,0,0,0,151,21,1,0,0,0,152,153,5,1,0,0,153,154,5,29,0,0,
        154,155,3,24,12,0,155,156,6,11,-1,0,156,157,5,23,0,0,157,23,1,0,
        0,0,158,159,3,30,15,0,159,160,3,26,13,0,160,25,1,0,0,0,161,162,3,
        28,14,0,162,163,3,30,15,0,163,164,6,13,-1,0,164,166,1,0,0,0,165,
        161,1,0,0,0,165,166,1,0,0,0,166,27,1,0,0,0,167,168,5,33,0,0,168,
        176,6,14,-1,0,169,170,5,32,0,0,170,176,6,14,-1,0,171,172,5,30,0,
        0,172,176,6,14,-1,0,173,174,5,31,0,0,174,176,6,14,-1,0,175,167,1,
        0,0,0,175,169,1,0,0,0,175,171,1,0,0,0,175,173,1,0,0,0,176,29,1,0,
        0,0,177,185,3,34,17,0,178,179,3,32,16,0,179,180,6,15,-1,0,180,181,
        3,34,17,0,181,182,6,15,-1,0,182,184,1,0,0,0,183,178,1,0,0,0,184,
        187,1,0,0,0,185,183,1,0,0,0,185,186,1,0,0,0,186,31,1,0,0,0,187,185,
        1,0,0,0,188,189,7,1,0,0,189,33,1,0,0,0,190,198,3,38,19,0,191,192,
        3,36,18,0,192,193,6,17,-1,0,193,194,3,38,19,0,194,195,6,17,-1,0,
        195,197,1,0,0,0,196,191,1,0,0,0,197,200,1,0,0,0,198,196,1,0,0,0,
        198,199,1,0,0,0,199,35,1,0,0,0,200,198,1,0,0,0,201,202,7,2,0,0,202,
        37,1,0,0,0,203,204,5,18,0,0,204,205,3,24,12,0,205,206,5,19,0,0,206,
        211,1,0,0,0,207,208,3,40,20,0,208,209,6,19,-1,0,209,211,1,0,0,0,
        210,203,1,0,0,0,210,207,1,0,0,0,211,39,1,0,0,0,212,214,3,42,21,0,
        213,212,1,0,0,0,213,214,1,0,0,0,214,215,1,0,0,0,215,216,3,44,22,
        0,216,217,6,20,-1,0,217,41,1,0,0,0,218,219,7,1,0,0,219,43,1,0,0,
        0,220,221,5,1,0,0,221,224,6,22,-1,0,222,224,3,46,23,0,223,220,1,
        0,0,0,223,222,1,0,0,0,224,45,1,0,0,0,225,226,5,3,0,0,226,230,6,23,
        -1,0,227,228,5,4,0,0,228,230,6,23,-1,0,229,225,1,0,0,0,229,227,1,
        0,0,0,230,47,1,0,0,0,231,232,5,9,0,0,232,233,5,18,0,0,233,234,3,
        24,12,0,234,235,5,19,0,0,235,236,6,24,-1,0,236,237,5,17,0,0,237,
        238,3,16,8,0,238,239,3,50,25,0,239,240,5,23,0,0,240,241,6,24,-1,
        0,241,49,1,0,0,0,242,243,5,10,0,0,243,244,6,25,-1,0,244,246,3,16,
        8,0,245,242,1,0,0,0,245,246,1,0,0,0,246,51,1,0,0,0,247,248,5,8,0,
        0,248,249,5,18,0,0,249,250,6,26,-1,0,250,251,3,24,12,0,251,252,5,
        19,0,0,252,253,5,17,0,0,253,254,6,26,-1,0,254,255,3,16,8,0,255,256,
        5,23,0,0,256,257,6,26,-1,0,257,53,1,0,0,0,258,259,5,1,0,0,259,260,
        5,18,0,0,260,261,3,56,28,0,261,262,5,19,0,0,262,263,5,23,0,0,263,
        55,1,0,0,0,264,266,3,58,29,0,265,264,1,0,0,0,265,266,1,0,0,0,266,
        57,1,0,0,0,267,273,3,24,12,0,268,269,3,24,12,0,269,270,5,22,0,0,
        270,271,3,58,29,0,271,273,1,0,0,0,272,267,1,0,0,0,272,268,1,0,0,
        0,273,59,1,0,0,0,274,275,5,13,0,0,275,276,5,18,0,0,276,277,3,62,
        31,0,277,278,5,19,0,0,278,279,5,23,0,0,279,61,1,0,0,0,280,281,3,
        24,12,0,281,282,6,31,-1,0,282,283,3,64,32,0,283,288,1,0,0,0,284,
        285,5,2,0,0,285,286,6,31,-1,0,286,288,3,64,32,0,287,280,1,0,0,0,
        287,284,1,0,0,0,288,63,1,0,0,0,289,290,5,22,0,0,290,292,3,62,31,
        0,291,289,1,0,0,0,292,295,1,0,0,0,293,291,1,0,0,0,293,294,1,0,0,
        0,294,65,1,0,0,0,295,293,1,0,0,0,22,78,83,93,100,124,132,134,143,
        150,165,175,185,198,210,213,223,229,245,265,272,287,293
    ]

class PatitoParserParser ( Parser ):

    grammarFileName = "PatitoParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'programa'", "'nula'", "'inicio'", "'mientras'", 
                     "'si'", "'sino'", "'entero'", "'flotante'", "'escribe'", 
                     "'imprime'", "'fin'", "'vars'", "'haz'", "'('", "')'", 
                     "'{'", "'}'", "','", "';'", "':'", "'+'", "'-'", "'*'", 
                     "'/'", "'='", "'!='", "'=='", "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>", "ID", "CTE_LETRERO", "CTE_ENTERO", "CTE_FLOTANTE", 
                      "PROGRAM", "NULA", "INICIO", "MIENTRAS", "SI", "SINO", 
                      "ENTERO", "FLOTANTE", "ESCRIBE", "IMPRIME", "FIN", 
                      "VARS", "HAZ", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "COMMA", "SEMI", "COLON", "PLUS", "MINUS", "MUL", 
                      "DIV", "EQUAL", "NEQ", "DEQ", "LT", "GT", "WS" ]

    RULE_programa = 0
    RULE_tiene_variables = 1
    RULE_tiene_funciones = 2
    RULE_vars = 3
    RULE_complemento_vars = 4
    RULE_tipo = 5
    RULE_funcs = 6
    RULE_complemento_funcs = 7
    RULE_cuerpo = 8
    RULE_tiene_estatuto = 9
    RULE_estatuto = 10
    RULE_asigna = 11
    RULE_expresion = 12
    RULE_complemento_expresion = 13
    RULE_exp_logicas = 14
    RULE_exp = 15
    RULE_exp_signo = 16
    RULE_termino = 17
    RULE_term_signo = 18
    RULE_factor = 19
    RULE_factor_operaciones = 20
    RULE_tiene_signo = 21
    RULE_tiene_var = 22
    RULE_cte = 23
    RULE_condicion = 24
    RULE_complemento_cond = 25
    RULE_ciclo = 26
    RULE_llamada = 27
    RULE_complemento_llamada = 28
    RULE_tiene_expresion = 29
    RULE_imprime = 30
    RULE_complemento_imprime = 31
    RULE_complemento_imprime_aux = 32

    ruleNames =  [ "programa", "tiene_variables", "tiene_funciones", "vars", 
                   "complemento_vars", "tipo", "funcs", "complemento_funcs", 
                   "cuerpo", "tiene_estatuto", "estatuto", "asigna", "expresion", 
                   "complemento_expresion", "exp_logicas", "exp", "exp_signo", 
                   "termino", "term_signo", "factor", "factor_operaciones", 
                   "tiene_signo", "tiene_var", "cte", "condicion", "complemento_cond", 
                   "ciclo", "llamada", "complemento_llamada", "tiene_expresion", 
                   "imprime", "complemento_imprime", "complemento_imprime_aux" ]

    EOF = Token.EOF
    ID=1
    CTE_LETRERO=2
    CTE_ENTERO=3
    CTE_FLOTANTE=4
    PROGRAM=5
    NULA=6
    INICIO=7
    MIENTRAS=8
    SI=9
    SINO=10
    ENTERO=11
    FLOTANTE=12
    ESCRIBE=13
    IMPRIME=14
    FIN=15
    VARS=16
    HAZ=17
    LPAREN=18
    RPAREN=19
    LBRACE=20
    RBRACE=21
    COMMA=22
    SEMI=23
    COLON=24
    PLUS=25
    MINUS=26
    MUL=27
    DIV=28
    EQUAL=29
    NEQ=30
    DEQ=31
    LT=32
    GT=33
    WS=34

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    contadorenteroglobal = 1000
    contadorflotanteglobal = 3000

    contadorenterotemporal = 5000
    contadorflotantetemporal = 7500

    contadorenterolocal = 10000
    contadorflotantelocal = 12500

    contadorenteroconstante = 15000
    contadorflotanteconstante = 20000
    contadorletreroconstante = 25000




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def PROGRAM(self):
            return self.getToken(PatitoParserParser.PROGRAM, 0)

        def ID(self):
            return self.getToken(PatitoParserParser.ID, 0)

        def SEMI(self):
            return self.getToken(PatitoParserParser.SEMI, 0)

        def tiene_variables(self):
            return self.getTypedRuleContext(PatitoParserParser.Tiene_variablesContext,0)


        def tiene_funciones(self):
            return self.getTypedRuleContext(PatitoParserParser.Tiene_funcionesContext,0)


        def INICIO(self):
            return self.getToken(PatitoParserParser.INICIO, 0)

        def cuerpo(self):
            return self.getTypedRuleContext(PatitoParserParser.CuerpoContext,0)


        def FIN(self):
            return self.getToken(PatitoParserParser.FIN, 0)

        def getRuleIndex(self):
            return PatitoParserParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = PatitoParserParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(PatitoParserParser.PROGRAM)
            self.state = 67
            localctx._ID = self.match(PatitoParserParser.ID)

            self.nombrefuncion = (None if localctx._ID is None else localctx._ID.text)
            self.funcdir.add_funcion((None if localctx._ID is None else localctx._ID.text),"programa")

            self.state = 69
            self.match(PatitoParserParser.SEMI)
            self.state = 70
            self.tiene_variables()
            self.state = 71
            self.tiene_funciones()
            self.state = 72
            self.match(PatitoParserParser.INICIO)
            self.state = 73
            self.cuerpo()
            self.state = 74
            self.match(PatitoParserParser.FIN)

            self.cuadruplo.add_end_Cuadruplo()
            tablaconst = self.constantes.get_tabla()
            self.cuadruplo.generate_document(self.nombrefuncion,tablaconst,)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tiene_variablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vars_(self):
            return self.getTypedRuleContext(PatitoParserParser.VarsContext,0)


        def getRuleIndex(self):
            return PatitoParserParser.RULE_tiene_variables

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTiene_variables" ):
                listener.enterTiene_variables(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTiene_variables" ):
                listener.exitTiene_variables(self)




    def tiene_variables(self):

        localctx = PatitoParserParser.Tiene_variablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_tiene_variables)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 77
                self.vars_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tiene_funcionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PatitoParserParser.FuncsContext)
            else:
                return self.getTypedRuleContext(PatitoParserParser.FuncsContext,i)


        def getRuleIndex(self):
            return PatitoParserParser.RULE_tiene_funciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTiene_funciones" ):
                listener.enterTiene_funciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTiene_funciones" ):
                listener.exitTiene_funciones(self)




    def tiene_funciones(self):

        localctx = PatitoParserParser.Tiene_funcionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_tiene_funciones)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 80
                self.funcs()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._complemento_vars = None # Complemento_varsContext

        def VARS(self):
            return self.getToken(PatitoParserParser.VARS, 0)

        def complemento_vars(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PatitoParserParser.Complemento_varsContext)
            else:
                return self.getTypedRuleContext(PatitoParserParser.Complemento_varsContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(PatitoParserParser.SEMI)
            else:
                return self.getToken(PatitoParserParser.SEMI, i)

        def getRuleIndex(self):
            return PatitoParserParser.RULE_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars" ):
                listener.enterVars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars" ):
                listener.exitVars(self)




    def vars_(self):

        localctx = PatitoParserParser.VarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(PatitoParserParser.VARS)
            self.state = 91 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 87
                localctx._complemento_vars = self.complemento_vars()

                partes = (None if localctx._complemento_vars is None else self._input.getText(localctx._complemento_vars.start,localctx._complemento_vars.stop)).split(":")  
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
                        self.contadorflotanteglobal = self.contadorflotanteglobal + 1
                    else:
                        raise ValueError(f"Variable no identificada")

                self.state = 89
                self.match(PatitoParserParser.SEMI)
                self.state = 93 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Complemento_varsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PatitoParserParser.ID)
            else:
                return self.getToken(PatitoParserParser.ID, i)

        def COLON(self):
            return self.getToken(PatitoParserParser.COLON, 0)

        def tipo(self):
            return self.getTypedRuleContext(PatitoParserParser.TipoContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PatitoParserParser.COMMA)
            else:
                return self.getToken(PatitoParserParser.COMMA, i)

        def getRuleIndex(self):
            return PatitoParserParser.RULE_complemento_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplemento_vars" ):
                listener.enterComplemento_vars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplemento_vars" ):
                listener.exitComplemento_vars(self)




    def complemento_vars(self):

        localctx = PatitoParserParser.Complemento_varsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_complemento_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(PatitoParserParser.ID)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 96
                self.match(PatitoParserParser.COMMA)
                self.state = 97
                self.match(PatitoParserParser.ID)
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 103
            self.match(PatitoParserParser.COLON)
            self.state = 104
            self.tipo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTERO(self):
            return self.getToken(PatitoParserParser.ENTERO, 0)

        def FLOTANTE(self):
            return self.getToken(PatitoParserParser.FLOTANTE, 0)

        def getRuleIndex(self):
            return PatitoParserParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = PatitoParserParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self._complemento_funcs = None # Complemento_funcsContext

        def NULA(self):
            return self.getToken(PatitoParserParser.NULA, 0)

        def ID(self):
            return self.getToken(PatitoParserParser.ID, 0)

        def LPAREN(self):
            return self.getToken(PatitoParserParser.LPAREN, 0)

        def complemento_funcs(self):
            return self.getTypedRuleContext(PatitoParserParser.Complemento_funcsContext,0)


        def RPAREN(self):
            return self.getToken(PatitoParserParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(PatitoParserParser.LBRACE, 0)

        def tiene_variables(self):
            return self.getTypedRuleContext(PatitoParserParser.Tiene_variablesContext,0)


        def cuerpo(self):
            return self.getTypedRuleContext(PatitoParserParser.CuerpoContext,0)


        def RBRACE(self):
            return self.getToken(PatitoParserParser.RBRACE, 0)

        def SEMI(self):
            return self.getToken(PatitoParserParser.SEMI, 0)

        def getRuleIndex(self):
            return PatitoParserParser.RULE_funcs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncs" ):
                listener.enterFuncs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncs" ):
                listener.exitFuncs(self)




    def funcs(self):

        localctx = PatitoParserParser.FuncsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(PatitoParserParser.NULA)
            self.state = 109
            localctx._ID = self.match(PatitoParserParser.ID)

            self.nombrefuncion = (None if localctx._ID is None else localctx._ID.text)
            self.funcdir.add_funcion((None if localctx._ID is None else localctx._ID.text),"nula")

            self.state = 111
            self.match(PatitoParserParser.LPAREN)
            self.state = 112
            localctx._complemento_funcs = self.complemento_funcs()

            argumentos = (None if localctx._complemento_funcs is None else self._input.getText(localctx._complemento_funcs.start,localctx._complemento_funcs.stop)).split(",")  
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

            self.state = 114
            self.match(PatitoParserParser.RPAREN)
            self.state = 115
            self.match(PatitoParserParser.LBRACE)
            self.state = 116
            self.tiene_variables()
            self.state = 117
            self.cuerpo()
            self.state = 118
            self.match(PatitoParserParser.RBRACE)
            self.state = 119
            self.match(PatitoParserParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Complemento_funcsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PatitoParserParser.ID, 0)

        def COLON(self):
            return self.getToken(PatitoParserParser.COLON, 0)

        def tipo(self):
            return self.getTypedRuleContext(PatitoParserParser.TipoContext,0)


        def COMMA(self):
            return self.getToken(PatitoParserParser.COMMA, 0)

        def complemento_funcs(self):
            return self.getTypedRuleContext(PatitoParserParser.Complemento_funcsContext,0)


        def getRuleIndex(self):
            return PatitoParserParser.RULE_complemento_funcs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplemento_funcs" ):
                listener.enterComplemento_funcs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplemento_funcs" ):
                listener.exitComplemento_funcs(self)




    def complemento_funcs(self):

        localctx = PatitoParserParser.Complemento_funcsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_complemento_funcs)
        self._la = 0 # Token type
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 121
                    self.match(PatitoParserParser.ID)
                    self.state = 122
                    self.match(PatitoParserParser.COLON)
                    self.state = 123
                    self.tipo()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 126
                    self.match(PatitoParserParser.ID)
                    self.state = 127
                    self.match(PatitoParserParser.COLON)
                    self.state = 128
                    self.tipo()
                    self.state = 129
                    self.match(PatitoParserParser.COMMA)
                    self.state = 130
                    self.complemento_funcs()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CuerpoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(PatitoParserParser.LBRACE, 0)

        def tiene_estatuto(self):
            return self.getTypedRuleContext(PatitoParserParser.Tiene_estatutoContext,0)


        def RBRACE(self):
            return self.getToken(PatitoParserParser.RBRACE, 0)

        def getRuleIndex(self):
            return PatitoParserParser.RULE_cuerpo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCuerpo" ):
                listener.enterCuerpo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCuerpo" ):
                listener.exitCuerpo(self)




    def cuerpo(self):

        localctx = PatitoParserParser.CuerpoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_cuerpo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(PatitoParserParser.LBRACE)
            self.state = 137
            self.tiene_estatuto()
            self.state = 138
            self.match(PatitoParserParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tiene_estatutoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def estatuto(self):
            return self.getTypedRuleContext(PatitoParserParser.EstatutoContext,0)


        def tiene_estatuto(self):
            return self.getTypedRuleContext(PatitoParserParser.Tiene_estatutoContext,0)


        def getRuleIndex(self):
            return PatitoParserParser.RULE_tiene_estatuto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTiene_estatuto" ):
                listener.enterTiene_estatuto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTiene_estatuto" ):
                listener.exitTiene_estatuto(self)




    def tiene_estatuto(self):

        localctx = PatitoParserParser.Tiene_estatutoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_tiene_estatuto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8962) != 0):
                self.state = 140
                self.estatuto()
                self.state = 141
                self.tiene_estatuto()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EstatutoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asigna(self):
            return self.getTypedRuleContext(PatitoParserParser.AsignaContext,0)


        def condicion(self):
            return self.getTypedRuleContext(PatitoParserParser.CondicionContext,0)


        def ciclo(self):
            return self.getTypedRuleContext(PatitoParserParser.CicloContext,0)


        def llamada(self):
            return self.getTypedRuleContext(PatitoParserParser.LlamadaContext,0)


        def imprime(self):
            return self.getTypedRuleContext(PatitoParserParser.ImprimeContext,0)


        def getRuleIndex(self):
            return PatitoParserParser.RULE_estatuto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEstatuto" ):
                listener.enterEstatuto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEstatuto" ):
                listener.exitEstatuto(self)




    def estatuto(self):

        localctx = PatitoParserParser.EstatutoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_estatuto)
        try:
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.asigna()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.condicion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                self.ciclo()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 148
                self.llamada()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 149
                self.imprime()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(PatitoParserParser.ID, 0)

        def EQUAL(self):
            return self.getToken(PatitoParserParser.EQUAL, 0)

        def expresion(self):
            return self.getTypedRuleContext(PatitoParserParser.ExpresionContext,0)


        def SEMI(self):
            return self.getToken(PatitoParserParser.SEMI, 0)

        def getRuleIndex(self):
            return PatitoParserParser.RULE_asigna

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsigna" ):
                listener.enterAsigna(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsigna" ):
                listener.exitAsigna(self)




    def asigna(self):

        localctx = PatitoParserParser.AsignaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_asigna)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            localctx._ID = self.match(PatitoParserParser.ID)
            self.state = 153
            self.match(PatitoParserParser.EQUAL)
            self.state = 154
            self.expresion()

            asignar = (None if localctx._ID is None else localctx._ID.text)
            asignar_dir = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(asignar)
            op = self.cuadruplo.peek_operating()
            op_dir = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(op)
            if not op_dir:
                op_dir = self.constantes.get_direccion(op)
                if not op_dir:
                    if '.' in op:
                        op_dir = self.contadorflotanteconstante
                        self.contadorflotanteconstante = op_dir + 1
                        op = self.constantes.add_constante(op,"flotante",op_dir)
                    else:
                        op_dir = self.contadorenteroconstante
                        self.contadorenteroconstante = op_dir + 1
                        op = self.constantes.add_constante(op,"entero",op_dir)
            self.cuadruplo.add_assign_Cuadruplo(self.semantic["="]["codigo"],op_dir,asignar_dir)

            self.state = 156
            self.match(PatitoParserParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(PatitoParserParser.ExpContext,0)


        def complemento_expresion(self):
            return self.getTypedRuleContext(PatitoParserParser.Complemento_expresionContext,0)


        def getRuleIndex(self):
            return PatitoParserParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)




    def expresion(self):

        localctx = PatitoParserParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.exp()
            self.state = 159
            self.complemento_expresion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Complemento_expresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_logicas(self):
            return self.getTypedRuleContext(PatitoParserParser.Exp_logicasContext,0)


        def exp(self):
            return self.getTypedRuleContext(PatitoParserParser.ExpContext,0)


        def getRuleIndex(self):
            return PatitoParserParser.RULE_complemento_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplemento_expresion" ):
                listener.enterComplemento_expresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplemento_expresion" ):
                listener.exitComplemento_expresion(self)




    def complemento_expresion(self):

        localctx = PatitoParserParser.Complemento_expresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_complemento_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 16106127360) != 0):
                self.state = 161
                self.exp_logicas()
                self.state = 162
                self.exp()

                temp = self.cuadruplo.nuevo_temp()
                operador = self.cuadruplo.pop_operator()

                op2 = self.cuadruplo.pop_operating()
                op2_tipo = self.cuadruplo.pop_type()
                op2_dir = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(op2)
                if not op2_dir:
                    op2_dir = self.constantes.get_direccion(op2)
                    if not op2_dir:
                        if '.' in op2:
                            op2_dir = self.contadorflotanteconstante
                            self.contadorflotanteconstante = op2_dir + 1
                            op2 = self.constantes.add_constante(op2,"flotante",op2_dir)
                        else:
                            op2_dir = self.contadorenteroconstante
                            self.contadorenteroconstante = op2_dir + 1
                            op2 = self.constantes.add_constante(op2,"entero",op2_dir)

                op1 = self.cuadruplo.pop_operating()
                op1_tipo = self.cuadruplo.pop_type()
                op1_dir = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(op1)
                if not op1_dir:
                    op1_dir = self.constantes.get_direccion(op1)
                    if not op1_dir:
                        if '.' in op1:
                            op1_dir = self.contadorflotanteconstante
                            self.contadorflotanteconstante = op1_dir + 1
                            op1 = self.constantes.add_constante(op1,"flotante",op1_dir)
                        else:
                            op1_dir = self.contadorenteroconstante
                            self.contadorenteroconstante = op1_dir + 1
                            op1 = self.constantes.add_constante(op2,"entero",op1_dir)

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



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_logicasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(PatitoParserParser.GT, 0)

        def LT(self):
            return self.getToken(PatitoParserParser.LT, 0)

        def NEQ(self):
            return self.getToken(PatitoParserParser.NEQ, 0)

        def DEQ(self):
            return self.getToken(PatitoParserParser.DEQ, 0)

        def getRuleIndex(self):
            return PatitoParserParser.RULE_exp_logicas

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp_logicas" ):
                listener.enterExp_logicas(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp_logicas" ):
                listener.exitExp_logicas(self)




    def exp_logicas(self):

        localctx = PatitoParserParser.Exp_logicasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_exp_logicas)
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.match(PatitoParserParser.GT)

                self.cuadruplo.push_operator('>')

                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.match(PatitoParserParser.LT)

                self.cuadruplo.push_operator('<')

                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 171
                self.match(PatitoParserParser.NEQ)

                self.cuadruplo.push_operator('!=')

                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 4)
                self.state = 173
                self.match(PatitoParserParser.DEQ)

                self.cuadruplo.push_operator('==')

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


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._exp_signo = None # Exp_signoContext

        def termino(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PatitoParserParser.TerminoContext)
            else:
                return self.getTypedRuleContext(PatitoParserParser.TerminoContext,i)


        def exp_signo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PatitoParserParser.Exp_signoContext)
            else:
                return self.getTypedRuleContext(PatitoParserParser.Exp_signoContext,i)


        def getRuleIndex(self):
            return PatitoParserParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)




    def exp(self):

        localctx = PatitoParserParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.termino()
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25 or _la==26:
                self.state = 178
                localctx._exp_signo = self.exp_signo()

                self.cuadruplo.push_operator((None if localctx._exp_signo is None else self._input.getText(localctx._exp_signo.start,localctx._exp_signo.stop)));

                self.state = 180
                self.termino()

                temp = self.cuadruplo.nuevo_temp()
                operador = self.cuadruplo.pop_operator()

                op2 = self.cuadruplo.pop_operating()
                op2_tipo = self.cuadruplo.pop_type()
                op2_dir = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(op2)
                if not op2_dir:
                    op2_dir = self.constantes.get_direccion(op2)
                    if not op2_dir:
                        if '.' in op2:
                            op2_dir = self.contadorflotanteconstante
                            self.contadorflotanteconstante = op2_dir + 1
                            op2 = self.constantes.add_constante(op2,"flotante",op2_dir)
                        else:
                            op2_dir = self.contadorenteroconstante
                            self.contadorenteroconstante = op2_dir + 1
                            op2 = self.constantes.add_constante(op2,"entero",op2_dir)

                op1 = self.cuadruplo.pop_operating()
                op1_tipo = self.cuadruplo.pop_type()
                op1_dir = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(op1)
                if not op1_dir:
                    op1_dir = self.constantes.get_direccion(op1)
                    if not op1_dir:
                        if '.' in op1:
                            op1_dir = self.contadorflotanteconstante
                            self.contadorflotanteconstante = op1_dir + 1
                            op1 = self.constantes.add_constante(op1,"flotante",op1_dir)
                        else:
                            op1_dir = self.contadorenteroconstante
                            self.contadorenteroconstante = op1_dir + 1
                            op1 = self.constantes.add_constante(op2,"entero",op1_dir)


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

                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_signoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(PatitoParserParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(PatitoParserParser.MINUS, 0)

        def getRuleIndex(self):
            return PatitoParserParser.RULE_exp_signo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp_signo" ):
                listener.enterExp_signo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp_signo" ):
                listener.exitExp_signo(self)




    def exp_signo(self):

        localctx = PatitoParserParser.Exp_signoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_exp_signo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            _la = self._input.LA(1)
            if not(_la==25 or _la==26):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._term_signo = None # Term_signoContext

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PatitoParserParser.FactorContext)
            else:
                return self.getTypedRuleContext(PatitoParserParser.FactorContext,i)


        def term_signo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PatitoParserParser.Term_signoContext)
            else:
                return self.getTypedRuleContext(PatitoParserParser.Term_signoContext,i)


        def getRuleIndex(self):
            return PatitoParserParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)




    def termino(self):

        localctx = PatitoParserParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.factor()
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27 or _la==28:
                self.state = 191
                localctx._term_signo = self.term_signo()

                self.cuadruplo.push_operator((None if localctx._term_signo is None else self._input.getText(localctx._term_signo.start,localctx._term_signo.stop)));

                self.state = 193
                self.factor()

                temp = self.cuadruplo.nuevo_temp()
                operador = self.cuadruplo.pop_operator()

                op2 = self.cuadruplo.pop_operating()
                op2_tipo = self.cuadruplo.pop_type()
                op2_dir = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(op2)
                if not op2_dir:
                    op2_dir = self.constantes.get_direccion(op2)
                    if not op2_dir:
                        if '.' in op2:
                            op2_dir = self.contadorflotanteconstante
                            self.contadorflotanteconstante = op2_dir + 1
                            op2 = self.constantes.add_constante(op2,"flotante",op2_dir)
                        else:
                            op2_dir = self.contadorenteroconstante
                            self.contadorenteroconstante = op2_dir + 1
                            op2 = self.constantes.add_constante(op2,"entero",op2_dir)

                op1 = self.cuadruplo.pop_operating()
                op1_tipo = self.cuadruplo.pop_type()
                op1_dir = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(op1)
                if not op1_dir:
                    op1_dir = self.constantes.get_direccion(op1)
                    if not op1_dir:
                        if '.' in op1:
                            op1_dir = self.contadorflotanteconstante
                            self.contadorflotanteconstante = op1_dir + 1
                            op1 = self.constantes.add_constante(op1,"flotante",op1_dir)
                        else:
                            op1_dir = self.contadorenteroconstante
                            self.contadorenteroconstante = op1_dir + 1
                            op1 = self.constantes.add_constante(op2,"entero",op1_dir)


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

                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term_signoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUL(self):
            return self.getToken(PatitoParserParser.MUL, 0)

        def DIV(self):
            return self.getToken(PatitoParserParser.DIV, 0)

        def getRuleIndex(self):
            return PatitoParserParser.RULE_term_signo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm_signo" ):
                listener.enterTerm_signo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm_signo" ):
                listener.exitTerm_signo(self)




    def term_signo(self):

        localctx = PatitoParserParser.Term_signoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_term_signo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            _la = self._input.LA(1)
            if not(_la==27 or _la==28):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._factor_operaciones = None # Factor_operacionesContext

        def LPAREN(self):
            return self.getToken(PatitoParserParser.LPAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(PatitoParserParser.ExpresionContext,0)


        def RPAREN(self):
            return self.getToken(PatitoParserParser.RPAREN, 0)

        def factor_operaciones(self):
            return self.getTypedRuleContext(PatitoParserParser.Factor_operacionesContext,0)


        def getRuleIndex(self):
            return PatitoParserParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = PatitoParserParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_factor)
        try:
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.match(PatitoParserParser.LPAREN)
                self.state = 204
                self.expresion()
                self.state = 205
                self.match(PatitoParserParser.RPAREN)
                pass
            elif token in [1, 3, 4, 25, 26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                localctx._factor_operaciones = self.factor_operaciones()

                self.cuadruplo.push_operating((None if localctx._factor_operaciones is None else self._input.getText(localctx._factor_operaciones.start,localctx._factor_operaciones.stop)))

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


    class Factor_operacionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._tiene_signo = None # Tiene_signoContext
            self._tiene_var = None # Tiene_varContext

        def tiene_var(self):
            return self.getTypedRuleContext(PatitoParserParser.Tiene_varContext,0)


        def tiene_signo(self):
            return self.getTypedRuleContext(PatitoParserParser.Tiene_signoContext,0)


        def getRuleIndex(self):
            return PatitoParserParser.RULE_factor_operaciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_operaciones" ):
                listener.enterFactor_operaciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_operaciones" ):
                listener.exitFactor_operaciones(self)




    def factor_operaciones(self):

        localctx = PatitoParserParser.Factor_operacionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_factor_operaciones)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25 or _la==26:
                self.state = 212
                localctx._tiene_signo = self.tiene_signo()


            self.state = 215
            localctx._tiene_var = self.tiene_var()

            val = (None if localctx._tiene_var is None else self._input.getText(localctx._tiene_var.start,localctx._tiene_var.stop))
            signo = (None if localctx._tiene_signo is None else self._input.getText(localctx._tiene_signo.start,localctx._tiene_signo.stop))

            if not val.startswith("&"):
                val_tipo = self.cuadruplo.pop_type()
                if val_tipo == "entero":
                    val_dir = self.contadorenteroconstante
                    self.contadorenteroconstante = val_dir +1
                else:
                    val_dir = self.contadorflotanteconstante
                    self.contadorflotanteconstante = val_dir +1
                if signo:
                    if signo == "-":
                        val = "-" + val
                        self.constantes.add_constante(val,val_tipo,val_dir)
                    else: 
                        val = "+" + val
                        self.constantes.add_constante(val,val_tipo,val_dir)
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

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tiene_signoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(PatitoParserParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(PatitoParserParser.MINUS, 0)

        def getRuleIndex(self):
            return PatitoParserParser.RULE_tiene_signo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTiene_signo" ):
                listener.enterTiene_signo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTiene_signo" ):
                listener.exitTiene_signo(self)




    def tiene_signo(self):

        localctx = PatitoParserParser.Tiene_signoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_tiene_signo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            _la = self._input.LA(1)
            if not(_la==25 or _la==26):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tiene_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(PatitoParserParser.ID, 0)

        def cte(self):
            return self.getTypedRuleContext(PatitoParserParser.CteContext,0)


        def getRuleIndex(self):
            return PatitoParserParser.RULE_tiene_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTiene_var" ):
                listener.enterTiene_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTiene_var" ):
                listener.exitTiene_var(self)




    def tiene_var(self):

        localctx = PatitoParserParser.Tiene_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_tiene_var)
        try:
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                localctx._ID = self.match(PatitoParserParser.ID)

                if not self.funcdir.funciones[self.nombrefuncion]["tabla"].buscar_var((None if localctx._ID is None else localctx._ID.text)):
                    raise Exception(f"Varible {(None if localctx._ID is None else localctx._ID.text)} no declarada")

                pass
            elif token in [3, 4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.cte()
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


    class CteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._CTE_ENTERO = None # Token
            self._CTE_FLOTANTE = None # Token

        def CTE_ENTERO(self):
            return self.getToken(PatitoParserParser.CTE_ENTERO, 0)

        def CTE_FLOTANTE(self):
            return self.getToken(PatitoParserParser.CTE_FLOTANTE, 0)

        def getRuleIndex(self):
            return PatitoParserParser.RULE_cte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCte" ):
                listener.enterCte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCte" ):
                listener.exitCte(self)




    def cte(self):

        localctx = PatitoParserParser.CteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_cte)
        try:
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                localctx._CTE_ENTERO = self.match(PatitoParserParser.CTE_ENTERO)

                direccion = self.contadorenteroconstante
                self.contadorenteroconstante = direccion + 1
                self.constantes.add_constante((None if localctx._CTE_ENTERO is None else localctx._CTE_ENTERO.text),"entero",direccion)
                self.cuadruplo.push_type("entero")

                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                localctx._CTE_FLOTANTE = self.match(PatitoParserParser.CTE_FLOTANTE)

                direccion = self.contadorflotanteconstante
                self.contadorflotanteconstante = direccion + 1
                self.constantes.add_constante((None if localctx._CTE_FLOTANTE is None else localctx._CTE_FLOTANTE.text),"flotante",direccion)
                self.cuadruplo.push_type("flotante")

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


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(PatitoParserParser.SI, 0)

        def LPAREN(self):
            return self.getToken(PatitoParserParser.LPAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(PatitoParserParser.ExpresionContext,0)


        def RPAREN(self):
            return self.getToken(PatitoParserParser.RPAREN, 0)

        def HAZ(self):
            return self.getToken(PatitoParserParser.HAZ, 0)

        def cuerpo(self):
            return self.getTypedRuleContext(PatitoParserParser.CuerpoContext,0)


        def complemento_cond(self):
            return self.getTypedRuleContext(PatitoParserParser.Complemento_condContext,0)


        def SEMI(self):
            return self.getToken(PatitoParserParser.SEMI, 0)

        def getRuleIndex(self):
            return PatitoParserParser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)




    def condicion(self):

        localctx = PatitoParserParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(PatitoParserParser.SI)
            self.state = 232
            self.match(PatitoParserParser.LPAREN)
            self.state = 233
            self.expresion()
            self.state = 234
            self.match(PatitoParserParser.RPAREN)

            falso = self.cuadruplo.nuevo_label()
            op =self.cuadruplo.pop_operating()
            self.cuadruplo.add_conditional_jump(op,falso)
            self.cuadruplo.push_jump(falso)

            self.state = 236
            self.match(PatitoParserParser.HAZ)
            self.state = 237
            self.cuerpo()
            self.state = 238
            self.complemento_cond()
            self.state = 239
            self.match(PatitoParserParser.SEMI)

            final = self.cuadruplo.pop_jump()
            cuentafinal = self.cuadruplo.get_current_count()
            self.cuadruplo.edit_Cuadruplo_by_label(final,cuentafinal) 

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Complemento_condContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINO(self):
            return self.getToken(PatitoParserParser.SINO, 0)

        def cuerpo(self):
            return self.getTypedRuleContext(PatitoParserParser.CuerpoContext,0)


        def getRuleIndex(self):
            return PatitoParserParser.RULE_complemento_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplemento_cond" ):
                listener.enterComplemento_cond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplemento_cond" ):
                listener.exitComplemento_cond(self)




    def complemento_cond(self):

        localctx = PatitoParserParser.Complemento_condContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_complemento_cond)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 242
                self.match(PatitoParserParser.SINO)

                bypass = self.cuadruplo.nuevo_label()
                self.cuadruplo.add_by_pass_jump(bypass)
                salto = self.cuadruplo.pop_jump()
                self.cuadruplo.push_jump(bypass)
                cuentaelse = self.cuadruplo.get_current_count()
                self.cuadruplo.edit_Cuadruplo_by_label(salto,cuentaelse)

                self.state = 244
                self.cuerpo()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CicloContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIENTRAS(self):
            return self.getToken(PatitoParserParser.MIENTRAS, 0)

        def LPAREN(self):
            return self.getToken(PatitoParserParser.LPAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(PatitoParserParser.ExpresionContext,0)


        def RPAREN(self):
            return self.getToken(PatitoParserParser.RPAREN, 0)

        def HAZ(self):
            return self.getToken(PatitoParserParser.HAZ, 0)

        def cuerpo(self):
            return self.getTypedRuleContext(PatitoParserParser.CuerpoContext,0)


        def SEMI(self):
            return self.getToken(PatitoParserParser.SEMI, 0)

        def getRuleIndex(self):
            return PatitoParserParser.RULE_ciclo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCiclo" ):
                listener.enterCiclo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCiclo" ):
                listener.exitCiclo(self)




    def ciclo(self):

        localctx = PatitoParserParser.CicloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_ciclo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(PatitoParserParser.MIENTRAS)
            self.state = 248
            self.match(PatitoParserParser.LPAREN)

            inicioCiclo = self.cuadruplo.get_current_count();
            self.cuadruplo.push_jump(inicioCiclo);

            self.state = 250
            self.expresion()
            self.state = 251
            self.match(PatitoParserParser.RPAREN)
            self.state = 252
            self.match(PatitoParserParser.HAZ)

            falso = self.cuadruplo.nuevo_label();
            op = self.cuadruplo.peek_operating();
            self.cuadruplo.add_conditional_jump(op, falso);
            self.cuadruplo.push_jump(falso);

            self.state = 254
            self.cuerpo()
            self.state = 255
            self.match(PatitoParserParser.SEMI)

            saltoFalso = self.cuadruplo.pop_jump();
            inicioCiclo = self.cuadruplo.pop_jump();
            self.cuadruplo.add_by_pass_jump(inicioCiclo);
            cuentafinal = self.cuadruplo.get_current_count();
            self.cuadruplo.edit_Cuadruplo_by_label(saltoFalso, cuentafinal);

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlamadaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PatitoParserParser.ID, 0)

        def LPAREN(self):
            return self.getToken(PatitoParserParser.LPAREN, 0)

        def complemento_llamada(self):
            return self.getTypedRuleContext(PatitoParserParser.Complemento_llamadaContext,0)


        def RPAREN(self):
            return self.getToken(PatitoParserParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(PatitoParserParser.SEMI, 0)

        def getRuleIndex(self):
            return PatitoParserParser.RULE_llamada

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamada" ):
                listener.enterLlamada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamada" ):
                listener.exitLlamada(self)




    def llamada(self):

        localctx = PatitoParserParser.LlamadaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_llamada)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(PatitoParserParser.ID)
            self.state = 259
            self.match(PatitoParserParser.LPAREN)
            self.state = 260
            self.complemento_llamada()
            self.state = 261
            self.match(PatitoParserParser.RPAREN)
            self.state = 262
            self.match(PatitoParserParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Complemento_llamadaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tiene_expresion(self):
            return self.getTypedRuleContext(PatitoParserParser.Tiene_expresionContext,0)


        def getRuleIndex(self):
            return PatitoParserParser.RULE_complemento_llamada

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplemento_llamada" ):
                listener.enterComplemento_llamada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplemento_llamada" ):
                listener.exitComplemento_llamada(self)




    def complemento_llamada(self):

        localctx = PatitoParserParser.Complemento_llamadaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_complemento_llamada)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 100925466) != 0):
                self.state = 264
                self.tiene_expresion()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tiene_expresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(PatitoParserParser.ExpresionContext,0)


        def COMMA(self):
            return self.getToken(PatitoParserParser.COMMA, 0)

        def tiene_expresion(self):
            return self.getTypedRuleContext(PatitoParserParser.Tiene_expresionContext,0)


        def getRuleIndex(self):
            return PatitoParserParser.RULE_tiene_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTiene_expresion" ):
                listener.enterTiene_expresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTiene_expresion" ):
                listener.exitTiene_expresion(self)




    def tiene_expresion(self):

        localctx = PatitoParserParser.Tiene_expresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_tiene_expresion)
        try:
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.expresion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.expresion()
                self.state = 269
                self.match(PatitoParserParser.COMMA)
                self.state = 270
                self.tiene_expresion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESCRIBE(self):
            return self.getToken(PatitoParserParser.ESCRIBE, 0)

        def LPAREN(self):
            return self.getToken(PatitoParserParser.LPAREN, 0)

        def complemento_imprime(self):
            return self.getTypedRuleContext(PatitoParserParser.Complemento_imprimeContext,0)


        def RPAREN(self):
            return self.getToken(PatitoParserParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(PatitoParserParser.SEMI, 0)

        def getRuleIndex(self):
            return PatitoParserParser.RULE_imprime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImprime" ):
                listener.enterImprime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImprime" ):
                listener.exitImprime(self)




    def imprime(self):

        localctx = PatitoParserParser.ImprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_imprime)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(PatitoParserParser.ESCRIBE)
            self.state = 275
            self.match(PatitoParserParser.LPAREN)
            self.state = 276
            self.complemento_imprime()
            self.state = 277
            self.match(PatitoParserParser.RPAREN)
            self.state = 278
            self.match(PatitoParserParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Complemento_imprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._CTE_LETRERO = None # Token

        def expresion(self):
            return self.getTypedRuleContext(PatitoParserParser.ExpresionContext,0)


        def complemento_imprime_aux(self):
            return self.getTypedRuleContext(PatitoParserParser.Complemento_imprime_auxContext,0)


        def CTE_LETRERO(self):
            return self.getToken(PatitoParserParser.CTE_LETRERO, 0)

        def getRuleIndex(self):
            return PatitoParserParser.RULE_complemento_imprime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplemento_imprime" ):
                listener.enterComplemento_imprime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplemento_imprime" ):
                listener.exitComplemento_imprime(self)




    def complemento_imprime(self):

        localctx = PatitoParserParser.Complemento_imprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_complemento_imprime)
        try:
            self.state = 287
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 4, 18, 25, 26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.expresion()

                val = self.cuadruplo.pop_operating()
                add = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(val)
                if not add:
                    add = self.constantes.get_direccion(val)
                    if not add:
                        if '.' in val:
                            add = self.contadorflotanteconstante
                            self.contadorflotanteconstante = add + 1
                            val = self.constantes.add_constante(val,"flotante",add)
                        else:
                            add = self.contadorenteroconstante
                            self.contadorenteroconstante = add + 1
                            val = self.constantes.add_constante(val,"entero",add)
                self.cuadruplo.add_print_Cuadruplo(add)

                self.state = 282
                self.complemento_imprime_aux()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 284
                localctx._CTE_LETRERO = self.match(PatitoParserParser.CTE_LETRERO)

                direccion = self.contadorletreroconstante
                val = self.constantes.add_constante((None if localctx._CTE_LETRERO is None else localctx._CTE_LETRERO.text),"letrero",direccion)
                self.contadorletreroconstante = direccion + 1
                add = self.constantes.get_direccion(direccion)
                self.cuadruplo.add_print_Cuadruplo(add)

                self.state = 286
                self.complemento_imprime_aux()
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


    class Complemento_imprime_auxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PatitoParserParser.COMMA)
            else:
                return self.getToken(PatitoParserParser.COMMA, i)

        def complemento_imprime(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PatitoParserParser.Complemento_imprimeContext)
            else:
                return self.getTypedRuleContext(PatitoParserParser.Complemento_imprimeContext,i)


        def getRuleIndex(self):
            return PatitoParserParser.RULE_complemento_imprime_aux

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplemento_imprime_aux" ):
                listener.enterComplemento_imprime_aux(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplemento_imprime_aux" ):
                listener.exitComplemento_imprime_aux(self)




    def complemento_imprime_aux(self):

        localctx = PatitoParserParser.Complemento_imprime_auxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_complemento_imprime_aux)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 289
                    self.match(PatitoParserParser.COMMA)
                    self.state = 290
                    self.complemento_imprime() 
                self.state = 295
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





