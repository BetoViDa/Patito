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
        4,1,34,290,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,3,1,78,8,1,1,2,5,2,81,8,
        2,10,2,12,2,84,9,2,1,3,1,3,1,3,1,3,1,3,4,3,91,8,3,11,3,12,3,92,1,
        4,1,4,1,4,5,4,98,8,4,10,4,12,4,101,9,4,1,4,1,4,1,4,1,5,1,5,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,3,7,124,
        8,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,132,8,7,3,7,134,8,7,1,8,1,8,1,8,
        1,8,1,9,1,9,1,9,3,9,143,8,9,1,10,1,10,1,10,1,10,1,10,3,10,150,8,
        10,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,13,1,
        13,3,13,165,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,175,
        8,14,1,15,1,15,1,15,1,15,1,15,1,15,5,15,183,8,15,10,15,12,15,186,
        9,15,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,5,17,196,8,17,10,17,
        12,17,199,9,17,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,
        210,8,19,1,20,1,20,1,20,1,20,1,21,3,21,217,8,21,1,22,1,22,1,22,3,
        22,222,8,22,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,
        24,1,24,1,24,1,25,1,25,1,25,3,25,240,8,25,1,26,1,26,1,26,1,26,1,
        26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,1,28,3,
        28,259,8,28,1,29,1,29,1,29,1,29,1,29,3,29,266,8,29,1,30,1,30,1,30,
        1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,281,8,31,
        1,32,1,32,5,32,285,8,32,10,32,12,32,288,9,32,1,32,0,0,33,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,
        52,54,56,58,60,62,64,0,4,1,0,11,12,1,0,25,26,1,0,27,28,1,0,3,4,282,
        0,66,1,0,0,0,2,77,1,0,0,0,4,82,1,0,0,0,6,85,1,0,0,0,8,94,1,0,0,0,
        10,105,1,0,0,0,12,107,1,0,0,0,14,133,1,0,0,0,16,135,1,0,0,0,18,142,
        1,0,0,0,20,149,1,0,0,0,22,151,1,0,0,0,24,157,1,0,0,0,26,164,1,0,
        0,0,28,174,1,0,0,0,30,176,1,0,0,0,32,187,1,0,0,0,34,189,1,0,0,0,
        36,200,1,0,0,0,38,209,1,0,0,0,40,211,1,0,0,0,42,216,1,0,0,0,44,221,
        1,0,0,0,46,223,1,0,0,0,48,225,1,0,0,0,50,239,1,0,0,0,52,241,1,0,
        0,0,54,251,1,0,0,0,56,258,1,0,0,0,58,265,1,0,0,0,60,267,1,0,0,0,
        62,280,1,0,0,0,64,286,1,0,0,0,66,67,5,5,0,0,67,68,5,1,0,0,68,69,
        6,0,-1,0,69,70,5,23,0,0,70,71,3,2,1,0,71,72,3,4,2,0,72,73,5,7,0,
        0,73,74,3,16,8,0,74,75,5,15,0,0,75,1,1,0,0,0,76,78,3,6,3,0,77,76,
        1,0,0,0,77,78,1,0,0,0,78,3,1,0,0,0,79,81,3,12,6,0,80,79,1,0,0,0,
        81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,5,1,0,0,0,84,82,1,0,
        0,0,85,90,5,16,0,0,86,87,3,8,4,0,87,88,6,3,-1,0,88,89,5,23,0,0,89,
        91,1,0,0,0,90,86,1,0,0,0,91,92,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,
        0,93,7,1,0,0,0,94,99,5,1,0,0,95,96,5,22,0,0,96,98,5,1,0,0,97,95,
        1,0,0,0,98,101,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,102,1,0,
        0,0,101,99,1,0,0,0,102,103,5,24,0,0,103,104,3,10,5,0,104,9,1,0,0,
        0,105,106,7,0,0,0,106,11,1,0,0,0,107,108,5,6,0,0,108,109,5,1,0,0,
        109,110,6,6,-1,0,110,111,5,18,0,0,111,112,3,14,7,0,112,113,6,6,-1,
        0,113,114,5,19,0,0,114,115,5,20,0,0,115,116,3,2,1,0,116,117,3,16,
        8,0,117,118,5,21,0,0,118,119,5,23,0,0,119,13,1,0,0,0,120,121,5,1,
        0,0,121,122,5,24,0,0,122,124,3,10,5,0,123,120,1,0,0,0,123,124,1,
        0,0,0,124,134,1,0,0,0,125,126,5,1,0,0,126,127,5,24,0,0,127,128,3,
        10,5,0,128,129,5,22,0,0,129,130,3,14,7,0,130,132,1,0,0,0,131,125,
        1,0,0,0,131,132,1,0,0,0,132,134,1,0,0,0,133,123,1,0,0,0,133,131,
        1,0,0,0,134,15,1,0,0,0,135,136,5,20,0,0,136,137,3,18,9,0,137,138,
        5,21,0,0,138,17,1,0,0,0,139,140,3,20,10,0,140,141,3,18,9,0,141,143,
        1,0,0,0,142,139,1,0,0,0,142,143,1,0,0,0,143,19,1,0,0,0,144,150,3,
        22,11,0,145,150,3,48,24,0,146,150,3,52,26,0,147,150,3,54,27,0,148,
        150,3,60,30,0,149,144,1,0,0,0,149,145,1,0,0,0,149,146,1,0,0,0,149,
        147,1,0,0,0,149,148,1,0,0,0,150,21,1,0,0,0,151,152,5,1,0,0,152,153,
        5,29,0,0,153,154,3,24,12,0,154,155,6,11,-1,0,155,156,5,23,0,0,156,
        23,1,0,0,0,157,158,3,30,15,0,158,159,3,26,13,0,159,25,1,0,0,0,160,
        161,3,28,14,0,161,162,3,30,15,0,162,163,6,13,-1,0,163,165,1,0,0,
        0,164,160,1,0,0,0,164,165,1,0,0,0,165,27,1,0,0,0,166,167,5,33,0,
        0,167,175,6,14,-1,0,168,169,5,32,0,0,169,175,6,14,-1,0,170,171,5,
        30,0,0,171,175,6,14,-1,0,172,173,5,31,0,0,173,175,6,14,-1,0,174,
        166,1,0,0,0,174,168,1,0,0,0,174,170,1,0,0,0,174,172,1,0,0,0,175,
        29,1,0,0,0,176,184,3,34,17,0,177,178,3,32,16,0,178,179,6,15,-1,0,
        179,180,3,34,17,0,180,181,6,15,-1,0,181,183,1,0,0,0,182,177,1,0,
        0,0,183,186,1,0,0,0,184,182,1,0,0,0,184,185,1,0,0,0,185,31,1,0,0,
        0,186,184,1,0,0,0,187,188,7,1,0,0,188,33,1,0,0,0,189,197,3,38,19,
        0,190,191,3,36,18,0,191,192,6,17,-1,0,192,193,3,38,19,0,193,194,
        6,17,-1,0,194,196,1,0,0,0,195,190,1,0,0,0,196,199,1,0,0,0,197,195,
        1,0,0,0,197,198,1,0,0,0,198,35,1,0,0,0,199,197,1,0,0,0,200,201,7,
        2,0,0,201,37,1,0,0,0,202,203,5,18,0,0,203,204,3,24,12,0,204,205,
        5,19,0,0,205,210,1,0,0,0,206,207,3,40,20,0,207,208,6,19,-1,0,208,
        210,1,0,0,0,209,202,1,0,0,0,209,206,1,0,0,0,210,39,1,0,0,0,211,212,
        3,42,21,0,212,213,3,44,22,0,213,214,6,20,-1,0,214,41,1,0,0,0,215,
        217,7,1,0,0,216,215,1,0,0,0,216,217,1,0,0,0,217,43,1,0,0,0,218,219,
        5,1,0,0,219,222,6,22,-1,0,220,222,3,46,23,0,221,218,1,0,0,0,221,
        220,1,0,0,0,222,45,1,0,0,0,223,224,7,3,0,0,224,47,1,0,0,0,225,226,
        5,9,0,0,226,227,5,18,0,0,227,228,3,24,12,0,228,229,5,19,0,0,229,
        230,6,24,-1,0,230,231,5,17,0,0,231,232,3,16,8,0,232,233,3,50,25,
        0,233,234,5,23,0,0,234,235,6,24,-1,0,235,49,1,0,0,0,236,237,5,10,
        0,0,237,238,6,25,-1,0,238,240,3,16,8,0,239,236,1,0,0,0,239,240,1,
        0,0,0,240,51,1,0,0,0,241,242,5,8,0,0,242,243,5,18,0,0,243,244,3,
        24,12,0,244,245,5,19,0,0,245,246,5,17,0,0,246,247,6,26,-1,0,247,
        248,3,16,8,0,248,249,5,23,0,0,249,250,6,26,-1,0,250,53,1,0,0,0,251,
        252,5,1,0,0,252,253,5,18,0,0,253,254,3,56,28,0,254,255,5,19,0,0,
        255,256,5,23,0,0,256,55,1,0,0,0,257,259,3,58,29,0,258,257,1,0,0,
        0,258,259,1,0,0,0,259,57,1,0,0,0,260,266,3,24,12,0,261,262,3,24,
        12,0,262,263,5,22,0,0,263,264,3,58,29,0,264,266,1,0,0,0,265,260,
        1,0,0,0,265,261,1,0,0,0,266,59,1,0,0,0,267,268,5,13,0,0,268,269,
        5,18,0,0,269,270,3,62,31,0,270,271,5,19,0,0,271,272,5,23,0,0,272,
        61,1,0,0,0,273,274,3,24,12,0,274,275,6,31,-1,0,275,276,3,64,32,0,
        276,281,1,0,0,0,277,278,5,2,0,0,278,279,6,31,-1,0,279,281,3,64,32,
        0,280,273,1,0,0,0,280,277,1,0,0,0,281,63,1,0,0,0,282,283,5,22,0,
        0,283,285,3,62,31,0,284,282,1,0,0,0,285,288,1,0,0,0,286,284,1,0,
        0,0,286,287,1,0,0,0,287,65,1,0,0,0,288,286,1,0,0,0,21,77,82,92,99,
        123,131,133,142,149,164,174,184,197,209,216,221,239,258,265,280,
        286
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
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 76
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
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 79
                self.funcs()
                self.state = 84
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
            self.state = 85
            self.match(PatitoParserParser.VARS)
            self.state = 90 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 86
                localctx._complemento_vars = self.complemento_vars()

                partes = (None if localctx._complemento_vars is None else self._input.getText(localctx._complemento_vars.start,localctx._complemento_vars.stop)).split(":")  
                variables_separadas = partes[0].split(",")
                tipo = partes[1] 
                for variable in variables_separadas: 
                    self.funcdir.funciones[self.nombrefuncion]["tabla"].add_var(variable,tipo)

                self.state = 88
                self.match(PatitoParserParser.SEMI)
                self.state = 92 
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
            self.state = 94
            self.match(PatitoParserParser.ID)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 95
                self.match(PatitoParserParser.COMMA)
                self.state = 96
                self.match(PatitoParserParser.ID)
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 102
            self.match(PatitoParserParser.COLON)
            self.state = 103
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
            self.state = 105
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
            self.state = 107
            self.match(PatitoParserParser.NULA)
            self.state = 108
            localctx._ID = self.match(PatitoParserParser.ID)

            self.nombrefuncion = (None if localctx._ID is None else localctx._ID.text)
            self.funcdir.add_funcion((None if localctx._ID is None else localctx._ID.text),"nula")

            self.state = 110
            self.match(PatitoParserParser.LPAREN)
            self.state = 111
            localctx._complemento_funcs = self.complemento_funcs()

            argumentos = (None if localctx._complemento_funcs is None else self._input.getText(localctx._complemento_funcs.start,localctx._complemento_funcs.stop)).split(",")  
            for argumento in argumentos: 
                arg_div = argumento.split(":")
                variable = arg_div[0]
                tipo = arg_div[1]
                self.funcdir.funciones[self.nombrefuncion]["tabla"].add_var(variable,tipo)

            self.state = 113
            self.match(PatitoParserParser.RPAREN)
            self.state = 114
            self.match(PatitoParserParser.LBRACE)
            self.state = 115
            self.tiene_variables()
            self.state = 116
            self.cuerpo()
            self.state = 117
            self.match(PatitoParserParser.RBRACE)
            self.state = 118
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
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 120
                    self.match(PatitoParserParser.ID)
                    self.state = 121
                    self.match(PatitoParserParser.COLON)
                    self.state = 122
                    self.tipo()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 125
                    self.match(PatitoParserParser.ID)
                    self.state = 126
                    self.match(PatitoParserParser.COLON)
                    self.state = 127
                    self.tipo()
                    self.state = 128
                    self.match(PatitoParserParser.COMMA)
                    self.state = 129
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
            self.state = 135
            self.match(PatitoParserParser.LBRACE)
            self.state = 136
            self.tiene_estatuto()
            self.state = 137
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
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8962) != 0):
                self.state = 139
                self.estatuto()
                self.state = 140
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
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.asigna()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.condicion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 146
                self.ciclo()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 147
                self.llamada()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 148
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
            self.state = 151
            localctx._ID = self.match(PatitoParserParser.ID)
            self.state = 152
            self.match(PatitoParserParser.EQUAL)
            self.state = 153
            self.expresion()

            asignar = (None if localctx._ID is None else localctx._ID.text)
            op = self.cuadruplo.pop_operating()
            self.cuadruplo.add_assign_Cuadruplo("=",op,asignar)

            self.state = 155
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
            self.state = 157
            self.exp()
            self.state = 158
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
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 16106127360) != 0):
                self.state = 160
                self.exp_logicas()
                self.state = 161
                self.exp()

                temp = self.cuadruplo.nuevo_temp()
                operador = self.cuadruplo.pop_operator()
                op2 = self.cuadruplo.pop_operating()
                op1 = self.cuadruplo.pop_operating()
                tempadd = self.funcdir.funciones[self.nombrefuncion]["tabla"].add_var(temp,"temp")
                self.cuadruplo.add_Cuadruplo(operador,op1,op2,temp)
                self.cuadruplo.push_operating(temp)



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
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.match(PatitoParserParser.GT)

                self.cuadruplo.push_operator('>')

                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.match(PatitoParserParser.LT)

                self.cuadruplo.push_operator('<')

                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 170
                self.match(PatitoParserParser.NEQ)

                self.cuadruplo.push_operator('!=')

                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 4)
                self.state = 172
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
            self.state = 176
            self.termino()
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25 or _la==26:
                self.state = 177
                localctx._exp_signo = self.exp_signo()

                self.cuadruplo.push_operator((None if localctx._exp_signo is None else self._input.getText(localctx._exp_signo.start,localctx._exp_signo.stop)));

                self.state = 179
                self.termino()

                temp = self.cuadruplo.nuevo_temp();
                operador = self.cuadruplo.pop_operator();
                op2 = self.cuadruplo.pop_operating();
                op1 = self.cuadruplo.pop_operating();
                tempadd = self.funcdir.funciones[self.nombrefuncion]["tabla"].add_var(temp, "temp");
                self.cuadruplo.add_Cuadruplo(operador, op1, op2, temp);
                self.cuadruplo.push_operating(temp);

                self.state = 186
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
            self.state = 187
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
            self.state = 189
            self.factor()
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27 or _la==28:
                self.state = 190
                localctx._term_signo = self.term_signo()

                self.cuadruplo.push_operator((None if localctx._term_signo is None else self._input.getText(localctx._term_signo.start,localctx._term_signo.stop)));

                self.state = 192
                self.factor()

                temp = self.cuadruplo.nuevo_temp();
                operador = self.cuadruplo.pop_operator();
                op2 = self.cuadruplo.pop_operating();
                op1 = self.cuadruplo.pop_operating();
                tempadd = self.funcdir.funciones[self.nombrefuncion]["tabla"].add_var(temp, "temp");
                self.cuadruplo.add_Cuadruplo(operador, op1, op2, temp);
                self.cuadruplo.push_operating(temp);

                self.state = 199
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
            self.state = 200
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
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.match(PatitoParserParser.LPAREN)
                self.state = 203
                self.expresion()
                self.state = 204
                self.match(PatitoParserParser.RPAREN)
                pass
            elif token in [1, 3, 4, 25, 26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
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
            self._tiene_var = None # Tiene_varContext

        def tiene_signo(self):
            return self.getTypedRuleContext(PatitoParserParser.Tiene_signoContext,0)


        def tiene_var(self):
            return self.getTypedRuleContext(PatitoParserParser.Tiene_varContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.tiene_signo()
            self.state = 212
            localctx._tiene_var = self.tiene_var()

            val = (None if localctx._tiene_var is None else self._input.getText(localctx._tiene_var.start,localctx._tiene_var.stop))
            llave = self.funcdir.funciones[self.nombrefuncion]["tabla"].buscar_var(val)

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
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25 or _la==26:
                self.state = 215
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
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                localctx._ID = self.match(PatitoParserParser.ID)

                if not self.funcdir.funciones[self.nombrefuncion]["tabla"].buscar_var((None if localctx._ID is None else localctx._ID.text)):
                    raise Exception(f"Varible {(None if localctx._ID is None else localctx._ID.text)} no declarada")

                pass
            elif token in [3, 4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
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
            self.state = 225
            self.match(PatitoParserParser.SI)
            self.state = 226
            self.match(PatitoParserParser.LPAREN)
            self.state = 227
            self.expresion()
            self.state = 228
            self.match(PatitoParserParser.RPAREN)

            falso = self.cuadruplo.nuevo_label()
            op =self.cuadruplo.pop_operating()
            self.cuadruplo.add_conditional_jump(op,falso)
            self.cuadruplo.push_jump(falso)

            self.state = 230
            self.match(PatitoParserParser.HAZ)
            self.state = 231
            self.cuerpo()
            self.state = 232
            self.complemento_cond()
            self.state = 233
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
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 236
                self.match(PatitoParserParser.SINO)

                bypass = self.cuadruplo.nuevo_label()
                self.cuadruplo.add_by_pass_jump(bypass)
                salto = self.cuadruplo.pop_jump()
                self.cuadruplo.push_jump(bypass)
                cuentaelse = self.cuadruplo.get_current_count()
                self.cuadruplo.edit_Cuadruplo_by_label(salto,cuentaelse)

                self.state = 238
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
            self.state = 241
            self.match(PatitoParserParser.MIENTRAS)
            self.state = 242
            self.match(PatitoParserParser.LPAREN)
            self.state = 243
            self.expresion()
            self.state = 244
            self.match(PatitoParserParser.RPAREN)
            self.state = 245
            self.match(PatitoParserParser.HAZ)

            falso = self.cuadruplo.nuevo_label()
            op = self.cuadruplo.peek_operating()
            cicloInd = self.cuadruplo.get_current_count()
            self.cuadruplo.add_conditional_jump(op,falso)
            self.cuadruplo.push_jump(falso)
            self.cuadruplo.push_jump(cicloInd)

            self.state = 247
            self.cuerpo()
            self.state = 248
            self.match(PatitoParserParser.SEMI)

            op = self.cuadruplo.pop_operating()
            salto = self.cuadruplo.pop_jump()
            self.cuadruplo.add_cycle_jump(op,salto)
            cuentafinal = self.cuadruplo.get_current_count()
            salto = self.cuadruplo.pop_jump()
            self.cuadruplo.edit_Cuadruplo_by_label(salto,cuentafinal) 

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
            self.state = 251
            self.match(PatitoParserParser.ID)
            self.state = 252
            self.match(PatitoParserParser.LPAREN)
            self.state = 253
            self.complemento_llamada()
            self.state = 254
            self.match(PatitoParserParser.RPAREN)
            self.state = 255
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
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 100925466) != 0):
                self.state = 257
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
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.expresion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.expresion()
                self.state = 262
                self.match(PatitoParserParser.COMMA)
                self.state = 263
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
            self.state = 267
            self.match(PatitoParserParser.ESCRIBE)
            self.state = 268
            self.match(PatitoParserParser.LPAREN)
            self.state = 269
            self.complemento_imprime()
            self.state = 270
            self.match(PatitoParserParser.RPAREN)
            self.state = 271
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
            self.state = 280
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 4, 18, 25, 26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.expresion()

                val = self.cuadruplo.pop_operating()
                add = self.funcdir.funciones[self.nombrefuncion].tabla.get_dir(val)
                self.cuadruplo.add_print_Cuadruplo(add)

                self.state = 275
                self.complemento_imprime_aux()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                localctx._CTE_LETRERO = self.match(PatitoParserParser.CTE_LETRERO)

                val = self.funcdir.funciones[self.nombrefuncion].tabla.add_constant(localctx._CTE_LETRERO,"letrero")
                add = self.funcdir.funciones[self.nombrefuncion].tabla.get_dir(val)
                self.cuadruplo.add_print_Cuadruplo(add)

                self.state = 279
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
            self.state = 286
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 282
                    self.match(PatitoParserParser.COMMA)
                    self.state = 283
                    self.complemento_imprime() 
                self.state = 288
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





