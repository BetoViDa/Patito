// Generated from d:/Mty/Compis/patito/PatitoParser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class PatitoParserParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ID=1, CTE_LETRERO=2, CTE_ENTERO=3, CTE_FLOTANTE=4, PROGRAM=5, NULA=6, 
		INICIO=7, MIENTRAS=8, SI=9, SINO=10, ENTERO=11, FLOTANTE=12, ESCRIBE=13, 
		IMPRIME=14, FIN=15, VARS=16, HAZ=17, LPAREN=18, RPAREN=19, LBRACE=20, 
		RBRACE=21, COMMA=22, SEMI=23, COLON=24, PLUS=25, MINUS=26, MUL=27, DIV=28, 
		EQUAL=29, NEQ=30, DEQ=31, LT=32, GT=33, WS=34;
	public static final int
		RULE_programa = 0, RULE_tiene_variables = 1, RULE_tiene_funciones = 2, 
		RULE_vars = 3, RULE_complemento_vars = 4, RULE_tipo = 5, RULE_funcs = 6, 
		RULE_complemento_funcs = 7, RULE_cuerpo = 8, RULE_tiene_estatuto = 9, 
		RULE_estatuto = 10, RULE_asigna = 11, RULE_expresion = 12, RULE_complemento_expresion = 13, 
		RULE_exp_logicas = 14, RULE_exp = 15, RULE_exp_signo = 16, RULE_termino = 17, 
		RULE_term_signo = 18, RULE_factor = 19, RULE_factor_operaciones = 20, 
		RULE_tiene_signo = 21, RULE_tiene_var = 22, RULE_cte = 23, RULE_condicion = 24, 
		RULE_complemento_cond = 25, RULE_ciclo = 26, RULE_llamada = 27, RULE_complemento_llamada = 28, 
		RULE_tiene_expresion = 29, RULE_imprime = 30, RULE_complemento_imprime = 31, 
		RULE_complemento_imprime_aux = 32;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "tiene_variables", "tiene_funciones", "vars", "complemento_vars", 
			"tipo", "funcs", "complemento_funcs", "cuerpo", "tiene_estatuto", "estatuto", 
			"asigna", "expresion", "complemento_expresion", "exp_logicas", "exp", 
			"exp_signo", "termino", "term_signo", "factor", "factor_operaciones", 
			"tiene_signo", "tiene_var", "cte", "condicion", "complemento_cond", "ciclo", 
			"llamada", "complemento_llamada", "tiene_expresion", "imprime", "complemento_imprime", 
			"complemento_imprime_aux"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, "'programa'", "'nula'", "'inicio'", "'mientras'", 
			"'si'", "'sino'", "'entero'", "'flotante'", "'escribe'", "'imprime'", 
			"'fin'", "'vars'", "'haz'", "'('", "')'", "'{'", "'}'", "','", "';'", 
			"':'", "'+'", "'-'", "'*'", "'/'", "'='", "'!='", "'=='", "'<'", "'>'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "ID", "CTE_LETRERO", "CTE_ENTERO", "CTE_FLOTANTE", "PROGRAM", "NULA", 
			"INICIO", "MIENTRAS", "SI", "SINO", "ENTERO", "FLOTANTE", "ESCRIBE", 
			"IMPRIME", "FIN", "VARS", "HAZ", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
			"COMMA", "SEMI", "COLON", "PLUS", "MINUS", "MUL", "DIV", "EQUAL", "NEQ", 
			"DEQ", "LT", "GT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "PatitoParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }


	contadorenteroglobal = 1000
	contadorflotanteglobal = 3000

	contadorenterotemporal = 5000
	contadorflotantetemporal = 7500

	contadorenterolocal = 10000
	contadorflotantelocal = 12500

	contadorenteroconstante = 15000
	contadorflotanteconstante = 20000
	contadorletreroconstante = 25000


	public PatitoParserParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramaContext extends ParserRuleContext {
		public Token ID;
		public TerminalNode PROGRAM() { return getToken(PatitoParserParser.PROGRAM, 0); }
		public TerminalNode ID() { return getToken(PatitoParserParser.ID, 0); }
		public TerminalNode SEMI() { return getToken(PatitoParserParser.SEMI, 0); }
		public Tiene_variablesContext tiene_variables() {
			return getRuleContext(Tiene_variablesContext.class,0);
		}
		public Tiene_funcionesContext tiene_funciones() {
			return getRuleContext(Tiene_funcionesContext.class,0);
		}
		public TerminalNode INICIO() { return getToken(PatitoParserParser.INICIO, 0); }
		public CuerpoContext cuerpo() {
			return getRuleContext(CuerpoContext.class,0);
		}
		public TerminalNode FIN() { return getToken(PatitoParserParser.FIN, 0); }
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_programa);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			match(PROGRAM);
			setState(67);
			((ProgramaContext)_localctx).ID = match(ID);

			self.nombrefuncion = (((ProgramaContext)_localctx).ID!=null?((ProgramaContext)_localctx).ID.getText():null)
			self.funcdir.add_funcion((((ProgramaContext)_localctx).ID!=null?((ProgramaContext)_localctx).ID.getText():null),"programa")

			setState(69);
			match(SEMI);
			setState(70);
			tiene_variables();
			setState(71);
			tiene_funciones();
			setState(72);
			match(INICIO);
			setState(73);
			cuerpo();
			setState(74);
			match(FIN);

			self.cuadruplo.add_end_Cuadruplo()

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Tiene_variablesContext extends ParserRuleContext {
		public VarsContext vars() {
			return getRuleContext(VarsContext.class,0);
		}
		public Tiene_variablesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tiene_variables; }
	}

	public final Tiene_variablesContext tiene_variables() throws RecognitionException {
		Tiene_variablesContext _localctx = new Tiene_variablesContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_tiene_variables);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VARS) {
				{
				setState(77);
				vars();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Tiene_funcionesContext extends ParserRuleContext {
		public List<FuncsContext> funcs() {
			return getRuleContexts(FuncsContext.class);
		}
		public FuncsContext funcs(int i) {
			return getRuleContext(FuncsContext.class,i);
		}
		public Tiene_funcionesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tiene_funciones; }
	}

	public final Tiene_funcionesContext tiene_funciones() throws RecognitionException {
		Tiene_funcionesContext _localctx = new Tiene_funcionesContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_tiene_funciones);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NULA) {
				{
				{
				setState(80);
				funcs();
				}
				}
				setState(85);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarsContext extends ParserRuleContext {
		public Complemento_varsContext complemento_vars;
		public TerminalNode VARS() { return getToken(PatitoParserParser.VARS, 0); }
		public List<Complemento_varsContext> complemento_vars() {
			return getRuleContexts(Complemento_varsContext.class);
		}
		public Complemento_varsContext complemento_vars(int i) {
			return getRuleContext(Complemento_varsContext.class,i);
		}
		public List<TerminalNode> SEMI() { return getTokens(PatitoParserParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(PatitoParserParser.SEMI, i);
		}
		public VarsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vars; }
	}

	public final VarsContext vars() throws RecognitionException {
		VarsContext _localctx = new VarsContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_vars);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(86);
			match(VARS);
			setState(91); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(87);
				((VarsContext)_localctx).complemento_vars = complemento_vars();

				partes = (((VarsContext)_localctx).complemento_vars!=null?_input.getText(((VarsContext)_localctx).complemento_vars.start,((VarsContext)_localctx).complemento_vars.stop):null).split(":")  
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

				setState(89);
				match(SEMI);
				}
				}
				setState(93); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ID );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Complemento_varsContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(PatitoParserParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(PatitoParserParser.ID, i);
		}
		public TerminalNode COLON() { return getToken(PatitoParserParser.COLON, 0); }
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public List<TerminalNode> COMMA() { return getTokens(PatitoParserParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PatitoParserParser.COMMA, i);
		}
		public Complemento_varsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_complemento_vars; }
	}

	public final Complemento_varsContext complemento_vars() throws RecognitionException {
		Complemento_varsContext _localctx = new Complemento_varsContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_complemento_vars);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			match(ID);
			setState(100);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(96);
				match(COMMA);
				setState(97);
				match(ID);
				}
				}
				setState(102);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(103);
			match(COLON);
			setState(104);
			tipo();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TipoContext extends ParserRuleContext {
		public TerminalNode ENTERO() { return getToken(PatitoParserParser.ENTERO, 0); }
		public TerminalNode FLOTANTE() { return getToken(PatitoParserParser.FLOTANTE, 0); }
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(106);
			_la = _input.LA(1);
			if ( !(_la==ENTERO || _la==FLOTANTE) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FuncsContext extends ParserRuleContext {
		public Token ID;
		public Complemento_funcsContext complemento_funcs;
		public TerminalNode NULA() { return getToken(PatitoParserParser.NULA, 0); }
		public TerminalNode ID() { return getToken(PatitoParserParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(PatitoParserParser.LPAREN, 0); }
		public Complemento_funcsContext complemento_funcs() {
			return getRuleContext(Complemento_funcsContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(PatitoParserParser.RPAREN, 0); }
		public TerminalNode LBRACE() { return getToken(PatitoParserParser.LBRACE, 0); }
		public Tiene_variablesContext tiene_variables() {
			return getRuleContext(Tiene_variablesContext.class,0);
		}
		public CuerpoContext cuerpo() {
			return getRuleContext(CuerpoContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(PatitoParserParser.RBRACE, 0); }
		public TerminalNode SEMI() { return getToken(PatitoParserParser.SEMI, 0); }
		public FuncsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcs; }
	}

	public final FuncsContext funcs() throws RecognitionException {
		FuncsContext _localctx = new FuncsContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_funcs);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			match(NULA);
			setState(109);
			((FuncsContext)_localctx).ID = match(ID);

			self.nombrefuncion = (((FuncsContext)_localctx).ID!=null?((FuncsContext)_localctx).ID.getText():null)
			self.funcdir.add_funcion((((FuncsContext)_localctx).ID!=null?((FuncsContext)_localctx).ID.getText():null),"nula")

			setState(111);
			match(LPAREN);
			setState(112);
			((FuncsContext)_localctx).complemento_funcs = complemento_funcs();

			argumentos = (((FuncsContext)_localctx).complemento_funcs!=null?_input.getText(((FuncsContext)_localctx).complemento_funcs.start,((FuncsContext)_localctx).complemento_funcs.stop):null).split(",")  
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

			setState(114);
			match(RPAREN);
			setState(115);
			match(LBRACE);
			setState(116);
			tiene_variables();
			setState(117);
			cuerpo();
			setState(118);
			match(RBRACE);
			setState(119);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Complemento_funcsContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(PatitoParserParser.ID, 0); }
		public TerminalNode COLON() { return getToken(PatitoParserParser.COLON, 0); }
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(PatitoParserParser.COMMA, 0); }
		public Complemento_funcsContext complemento_funcs() {
			return getRuleContext(Complemento_funcsContext.class,0);
		}
		public Complemento_funcsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_complemento_funcs; }
	}

	public final Complemento_funcsContext complemento_funcs() throws RecognitionException {
		Complemento_funcsContext _localctx = new Complemento_funcsContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_complemento_funcs);
		int _la;
		try {
			setState(134);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(124);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ID) {
					{
					setState(121);
					match(ID);
					setState(122);
					match(COLON);
					setState(123);
					tipo();
					}
				}

				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(132);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ID) {
					{
					setState(126);
					match(ID);
					setState(127);
					match(COLON);
					setState(128);
					tipo();
					setState(129);
					match(COMMA);
					setState(130);
					complemento_funcs();
					}
				}

				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CuerpoContext extends ParserRuleContext {
		public TerminalNode LBRACE() { return getToken(PatitoParserParser.LBRACE, 0); }
		public Tiene_estatutoContext tiene_estatuto() {
			return getRuleContext(Tiene_estatutoContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(PatitoParserParser.RBRACE, 0); }
		public CuerpoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cuerpo; }
	}

	public final CuerpoContext cuerpo() throws RecognitionException {
		CuerpoContext _localctx = new CuerpoContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_cuerpo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(136);
			match(LBRACE);
			setState(137);
			tiene_estatuto();
			setState(138);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Tiene_estatutoContext extends ParserRuleContext {
		public EstatutoContext estatuto() {
			return getRuleContext(EstatutoContext.class,0);
		}
		public Tiene_estatutoContext tiene_estatuto() {
			return getRuleContext(Tiene_estatutoContext.class,0);
		}
		public Tiene_estatutoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tiene_estatuto; }
	}

	public final Tiene_estatutoContext tiene_estatuto() throws RecognitionException {
		Tiene_estatutoContext _localctx = new Tiene_estatutoContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_tiene_estatuto);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8962L) != 0)) {
				{
				setState(140);
				estatuto();
				setState(141);
				tiene_estatuto();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EstatutoContext extends ParserRuleContext {
		public AsignaContext asigna() {
			return getRuleContext(AsignaContext.class,0);
		}
		public CondicionContext condicion() {
			return getRuleContext(CondicionContext.class,0);
		}
		public CicloContext ciclo() {
			return getRuleContext(CicloContext.class,0);
		}
		public LlamadaContext llamada() {
			return getRuleContext(LlamadaContext.class,0);
		}
		public ImprimeContext imprime() {
			return getRuleContext(ImprimeContext.class,0);
		}
		public EstatutoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_estatuto; }
	}

	public final EstatutoContext estatuto() throws RecognitionException {
		EstatutoContext _localctx = new EstatutoContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_estatuto);
		try {
			setState(150);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(145);
				asigna();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(146);
				condicion();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(147);
				ciclo();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(148);
				llamada();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(149);
				imprime();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AsignaContext extends ParserRuleContext {
		public Token ID;
		public TerminalNode ID() { return getToken(PatitoParserParser.ID, 0); }
		public TerminalNode EQUAL() { return getToken(PatitoParserParser.EQUAL, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(PatitoParserParser.SEMI, 0); }
		public AsignaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asigna; }
	}

	public final AsignaContext asigna() throws RecognitionException {
		AsignaContext _localctx = new AsignaContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_asigna);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(152);
			((AsignaContext)_localctx).ID = match(ID);
			setState(153);
			match(EQUAL);
			setState(154);
			expresion();

			asignar = (((AsignaContext)_localctx).ID!=null?((AsignaContext)_localctx).ID.getText():null)
			asignar_dir = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(asignar)
			op = self.cuadruplo.peek_operating()
			op_dir = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(op)
			if not op_dir:
			    op_dir = self.constantes.get_direccion(op)
			self.cuadruplo.add_assign_Cuadruplo(self.semantic["="]["codigo"],op_dir,asignar_dir)

			setState(156);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpresionContext extends ParserRuleContext {
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public Complemento_expresionContext complemento_expresion() {
			return getRuleContext(Complemento_expresionContext.class,0);
		}
		public ExpresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion; }
	}

	public final ExpresionContext expresion() throws RecognitionException {
		ExpresionContext _localctx = new ExpresionContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_expresion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(158);
			exp();
			setState(159);
			complemento_expresion();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Complemento_expresionContext extends ParserRuleContext {
		public Exp_logicasContext exp_logicas() {
			return getRuleContext(Exp_logicasContext.class,0);
		}
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public Complemento_expresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_complemento_expresion; }
	}

	public final Complemento_expresionContext complemento_expresion() throws RecognitionException {
		Complemento_expresionContext _localctx = new Complemento_expresionContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_complemento_expresion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(165);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 16106127360L) != 0)) {
				{
				setState(161);
				exp_logicas();
				setState(162);
				exp();

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
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Exp_logicasContext extends ParserRuleContext {
		public TerminalNode GT() { return getToken(PatitoParserParser.GT, 0); }
		public TerminalNode LT() { return getToken(PatitoParserParser.LT, 0); }
		public TerminalNode NEQ() { return getToken(PatitoParserParser.NEQ, 0); }
		public TerminalNode DEQ() { return getToken(PatitoParserParser.DEQ, 0); }
		public Exp_logicasContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp_logicas; }
	}

	public final Exp_logicasContext exp_logicas() throws RecognitionException {
		Exp_logicasContext _localctx = new Exp_logicasContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_exp_logicas);
		try {
			setState(175);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case GT:
				enterOuterAlt(_localctx, 1);
				{
				setState(167);
				match(GT);

				self.cuadruplo.push_operator('>')

				}
				break;
			case LT:
				enterOuterAlt(_localctx, 2);
				{
				setState(169);
				match(LT);

				self.cuadruplo.push_operator('<')

				}
				break;
			case NEQ:
				enterOuterAlt(_localctx, 3);
				{
				setState(171);
				match(NEQ);

				self.cuadruplo.push_operator('!=')

				}
				break;
			case DEQ:
				enterOuterAlt(_localctx, 4);
				{
				setState(173);
				match(DEQ);

				self.cuadruplo.push_operator('==')

				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpContext extends ParserRuleContext {
		public Exp_signoContext exp_signo;
		public List<TerminoContext> termino() {
			return getRuleContexts(TerminoContext.class);
		}
		public TerminoContext termino(int i) {
			return getRuleContext(TerminoContext.class,i);
		}
		public List<Exp_signoContext> exp_signo() {
			return getRuleContexts(Exp_signoContext.class);
		}
		public Exp_signoContext exp_signo(int i) {
			return getRuleContext(Exp_signoContext.class,i);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_exp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(177);
			termino();
			setState(185);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(178);
				((ExpContext)_localctx).exp_signo = exp_signo();

				self.cuadruplo.push_operator((((ExpContext)_localctx).exp_signo!=null?_input.getText(((ExpContext)_localctx).exp_signo.start,((ExpContext)_localctx).exp_signo.stop):null));

				setState(180);
				termino();

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
				}
				setState(187);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Exp_signoContext extends ParserRuleContext {
		public TerminalNode PLUS() { return getToken(PatitoParserParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(PatitoParserParser.MINUS, 0); }
		public Exp_signoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp_signo; }
	}

	public final Exp_signoContext exp_signo() throws RecognitionException {
		Exp_signoContext _localctx = new Exp_signoContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_exp_signo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(188);
			_la = _input.LA(1);
			if ( !(_la==PLUS || _la==MINUS) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TerminoContext extends ParserRuleContext {
		public Term_signoContext term_signo;
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public List<Term_signoContext> term_signo() {
			return getRuleContexts(Term_signoContext.class);
		}
		public Term_signoContext term_signo(int i) {
			return getRuleContext(Term_signoContext.class,i);
		}
		public TerminoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termino; }
	}

	public final TerminoContext termino() throws RecognitionException {
		TerminoContext _localctx = new TerminoContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_termino);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(190);
			factor();
			setState(198);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==MUL || _la==DIV) {
				{
				{
				setState(191);
				((TerminoContext)_localctx).term_signo = term_signo();

				self.cuadruplo.push_operator((((TerminoContext)_localctx).term_signo!=null?_input.getText(((TerminoContext)_localctx).term_signo.start,((TerminoContext)_localctx).term_signo.stop):null));

				setState(193);
				factor();

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
				}
				setState(200);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Term_signoContext extends ParserRuleContext {
		public TerminalNode MUL() { return getToken(PatitoParserParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(PatitoParserParser.DIV, 0); }
		public Term_signoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term_signo; }
	}

	public final Term_signoContext term_signo() throws RecognitionException {
		Term_signoContext _localctx = new Term_signoContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_term_signo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(201);
			_la = _input.LA(1);
			if ( !(_la==MUL || _la==DIV) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public Factor_operacionesContext factor_operaciones;
		public TerminalNode LPAREN() { return getToken(PatitoParserParser.LPAREN, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(PatitoParserParser.RPAREN, 0); }
		public Factor_operacionesContext factor_operaciones() {
			return getRuleContext(Factor_operacionesContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_factor);
		try {
			setState(210);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LPAREN:
				enterOuterAlt(_localctx, 1);
				{
				setState(203);
				match(LPAREN);
				setState(204);
				expresion();
				setState(205);
				match(RPAREN);
				}
				break;
			case ID:
			case CTE_ENTERO:
			case CTE_FLOTANTE:
			case PLUS:
			case MINUS:
				enterOuterAlt(_localctx, 2);
				{
				setState(207);
				((FactorContext)_localctx).factor_operaciones = factor_operaciones();

				self.cuadruplo.push_operating((((FactorContext)_localctx).factor_operaciones!=null?_input.getText(((FactorContext)_localctx).factor_operaciones.start,((FactorContext)_localctx).factor_operaciones.stop):null))

				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Factor_operacionesContext extends ParserRuleContext {
		public Tiene_signoContext tiene_signo;
		public Tiene_varContext tiene_var;
		public Tiene_varContext tiene_var() {
			return getRuleContext(Tiene_varContext.class,0);
		}
		public Tiene_signoContext tiene_signo() {
			return getRuleContext(Tiene_signoContext.class,0);
		}
		public Factor_operacionesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor_operaciones; }
	}

	public final Factor_operacionesContext factor_operaciones() throws RecognitionException {
		Factor_operacionesContext _localctx = new Factor_operacionesContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_factor_operaciones);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(213);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PLUS || _la==MINUS) {
				{
				setState(212);
				((Factor_operacionesContext)_localctx).tiene_signo = tiene_signo();
				}
			}

			setState(215);
			((Factor_operacionesContext)_localctx).tiene_var = tiene_var();

			val = (((Factor_operacionesContext)_localctx).tiene_var!=null?_input.getText(((Factor_operacionesContext)_localctx).tiene_var.start,((Factor_operacionesContext)_localctx).tiene_var.stop):null)
			signo = (((Factor_operacionesContext)_localctx).tiene_signo!=null?_input.getText(((Factor_operacionesContext)_localctx).tiene_signo.start,((Factor_operacionesContext)_localctx).tiene_signo.stop):null)

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

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Tiene_signoContext extends ParserRuleContext {
		public TerminalNode PLUS() { return getToken(PatitoParserParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(PatitoParserParser.MINUS, 0); }
		public Tiene_signoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tiene_signo; }
	}

	public final Tiene_signoContext tiene_signo() throws RecognitionException {
		Tiene_signoContext _localctx = new Tiene_signoContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_tiene_signo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(218);
			_la = _input.LA(1);
			if ( !(_la==PLUS || _la==MINUS) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Tiene_varContext extends ParserRuleContext {
		public Token ID;
		public TerminalNode ID() { return getToken(PatitoParserParser.ID, 0); }
		public CteContext cte() {
			return getRuleContext(CteContext.class,0);
		}
		public Tiene_varContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tiene_var; }
	}

	public final Tiene_varContext tiene_var() throws RecognitionException {
		Tiene_varContext _localctx = new Tiene_varContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_tiene_var);
		try {
			setState(223);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(220);
				((Tiene_varContext)_localctx).ID = match(ID);

				if not self.funcdir.funciones[self.nombrefuncion]["tabla"].buscar_var((((Tiene_varContext)_localctx).ID!=null?((Tiene_varContext)_localctx).ID.getText():null)):
				    raise Exception(f"Varible {(((Tiene_varContext)_localctx).ID!=null?((Tiene_varContext)_localctx).ID.getText():null)} no declarada")

				}
				break;
			case CTE_ENTERO:
			case CTE_FLOTANTE:
				enterOuterAlt(_localctx, 2);
				{
				setState(222);
				cte();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CteContext extends ParserRuleContext {
		public Token CTE_ENTERO;
		public Token CTE_FLOTANTE;
		public TerminalNode CTE_ENTERO() { return getToken(PatitoParserParser.CTE_ENTERO, 0); }
		public TerminalNode CTE_FLOTANTE() { return getToken(PatitoParserParser.CTE_FLOTANTE, 0); }
		public CteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cte; }
	}

	public final CteContext cte() throws RecognitionException {
		CteContext _localctx = new CteContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_cte);
		try {
			setState(229);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CTE_ENTERO:
				enterOuterAlt(_localctx, 1);
				{
				setState(225);
				((CteContext)_localctx).CTE_ENTERO = match(CTE_ENTERO);

				direccion = self.contadorenteroconstante
				self.contadorenteroconstante = direccion + 1
				self.constantes.add_constante((((CteContext)_localctx).CTE_ENTERO!=null?((CteContext)_localctx).CTE_ENTERO.getText():null),"entero",direccion)
				self.cuadruplo.push_type("entero")

				}
				break;
			case CTE_FLOTANTE:
				enterOuterAlt(_localctx, 2);
				{
				setState(227);
				((CteContext)_localctx).CTE_FLOTANTE = match(CTE_FLOTANTE);

				direccion = self.contadorflotanteconstante
				self.contadorflotanteconstante = direccion + 1
				self.constantes.add_constante((((CteContext)_localctx).CTE_FLOTANTE!=null?((CteContext)_localctx).CTE_FLOTANTE.getText():null),"flotante",direccion)
				self.cuadruplo.push_type("flotante")

				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CondicionContext extends ParserRuleContext {
		public TerminalNode SI() { return getToken(PatitoParserParser.SI, 0); }
		public TerminalNode LPAREN() { return getToken(PatitoParserParser.LPAREN, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(PatitoParserParser.RPAREN, 0); }
		public TerminalNode HAZ() { return getToken(PatitoParserParser.HAZ, 0); }
		public CuerpoContext cuerpo() {
			return getRuleContext(CuerpoContext.class,0);
		}
		public Complemento_condContext complemento_cond() {
			return getRuleContext(Complemento_condContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(PatitoParserParser.SEMI, 0); }
		public CondicionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicion; }
	}

	public final CondicionContext condicion() throws RecognitionException {
		CondicionContext _localctx = new CondicionContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_condicion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(231);
			match(SI);
			setState(232);
			match(LPAREN);
			setState(233);
			expresion();
			setState(234);
			match(RPAREN);

			falso = self.cuadruplo.nuevo_label()
			op =self.cuadruplo.pop_operating()
			self.cuadruplo.add_conditional_jump(op,falso)
			self.cuadruplo.push_jump(falso)

			setState(236);
			match(HAZ);
			setState(237);
			cuerpo();
			setState(238);
			complemento_cond();
			setState(239);
			match(SEMI);

			final = self.cuadruplo.pop_jump()
			cuentafinal = self.cuadruplo.get_current_count()
			self.cuadruplo.edit_Cuadruplo_by_label(final,cuentafinal) 

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Complemento_condContext extends ParserRuleContext {
		public TerminalNode SINO() { return getToken(PatitoParserParser.SINO, 0); }
		public CuerpoContext cuerpo() {
			return getRuleContext(CuerpoContext.class,0);
		}
		public Complemento_condContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_complemento_cond; }
	}

	public final Complemento_condContext complemento_cond() throws RecognitionException {
		Complemento_condContext _localctx = new Complemento_condContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_complemento_cond);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(245);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SINO) {
				{
				setState(242);
				match(SINO);

				bypass = self.cuadruplo.nuevo_label()
				self.cuadruplo.add_by_pass_jump(bypass)
				salto = self.cuadruplo.pop_jump()
				self.cuadruplo.push_jump(bypass)
				cuentaelse = self.cuadruplo.get_current_count()
				self.cuadruplo.edit_Cuadruplo_by_label(salto,cuentaelse)

				setState(244);
				cuerpo();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CicloContext extends ParserRuleContext {
		public TerminalNode MIENTRAS() { return getToken(PatitoParserParser.MIENTRAS, 0); }
		public TerminalNode LPAREN() { return getToken(PatitoParserParser.LPAREN, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(PatitoParserParser.RPAREN, 0); }
		public TerminalNode HAZ() { return getToken(PatitoParserParser.HAZ, 0); }
		public CuerpoContext cuerpo() {
			return getRuleContext(CuerpoContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(PatitoParserParser.SEMI, 0); }
		public CicloContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ciclo; }
	}

	public final CicloContext ciclo() throws RecognitionException {
		CicloContext _localctx = new CicloContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_ciclo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(247);
			match(MIENTRAS);
			setState(248);
			match(LPAREN);
			setState(249);
			expresion();
			setState(250);
			match(RPAREN);
			setState(251);
			match(HAZ);

			falso = self.cuadruplo.nuevo_label()
			op = self.cuadruplo.peek_operating()
			cicloInd = self.cuadruplo.get_current_count()
			self.cuadruplo.add_conditional_jump(op,falso)
			self.cuadruplo.push_jump(falso)
			self.cuadruplo.push_jump(cicloInd)

			setState(253);
			cuerpo();
			setState(254);
			match(SEMI);

			op = self.cuadruplo.pop_operating()
			salto = self.cuadruplo.pop_jump()
			self.cuadruplo.add_cycle_jump(op,salto)
			cuentafinal = self.cuadruplo.get_current_count()
			salto = self.cuadruplo.pop_jump()
			self.cuadruplo.edit_Cuadruplo_by_label(salto,cuentafinal) 

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LlamadaContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(PatitoParserParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(PatitoParserParser.LPAREN, 0); }
		public Complemento_llamadaContext complemento_llamada() {
			return getRuleContext(Complemento_llamadaContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(PatitoParserParser.RPAREN, 0); }
		public TerminalNode SEMI() { return getToken(PatitoParserParser.SEMI, 0); }
		public LlamadaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_llamada; }
	}

	public final LlamadaContext llamada() throws RecognitionException {
		LlamadaContext _localctx = new LlamadaContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_llamada);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(257);
			match(ID);
			setState(258);
			match(LPAREN);
			setState(259);
			complemento_llamada();
			setState(260);
			match(RPAREN);
			setState(261);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Complemento_llamadaContext extends ParserRuleContext {
		public Tiene_expresionContext tiene_expresion() {
			return getRuleContext(Tiene_expresionContext.class,0);
		}
		public Complemento_llamadaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_complemento_llamada; }
	}

	public final Complemento_llamadaContext complemento_llamada() throws RecognitionException {
		Complemento_llamadaContext _localctx = new Complemento_llamadaContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_complemento_llamada);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(264);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 100925466L) != 0)) {
				{
				setState(263);
				tiene_expresion();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Tiene_expresionContext extends ParserRuleContext {
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(PatitoParserParser.COMMA, 0); }
		public Tiene_expresionContext tiene_expresion() {
			return getRuleContext(Tiene_expresionContext.class,0);
		}
		public Tiene_expresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tiene_expresion; }
	}

	public final Tiene_expresionContext tiene_expresion() throws RecognitionException {
		Tiene_expresionContext _localctx = new Tiene_expresionContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_tiene_expresion);
		try {
			setState(271);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(266);
				expresion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(267);
				expresion();
				setState(268);
				match(COMMA);
				setState(269);
				tiene_expresion();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ImprimeContext extends ParserRuleContext {
		public TerminalNode ESCRIBE() { return getToken(PatitoParserParser.ESCRIBE, 0); }
		public TerminalNode LPAREN() { return getToken(PatitoParserParser.LPAREN, 0); }
		public Complemento_imprimeContext complemento_imprime() {
			return getRuleContext(Complemento_imprimeContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(PatitoParserParser.RPAREN, 0); }
		public TerminalNode SEMI() { return getToken(PatitoParserParser.SEMI, 0); }
		public ImprimeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_imprime; }
	}

	public final ImprimeContext imprime() throws RecognitionException {
		ImprimeContext _localctx = new ImprimeContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_imprime);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(273);
			match(ESCRIBE);
			setState(274);
			match(LPAREN);
			setState(275);
			complemento_imprime();
			setState(276);
			match(RPAREN);
			setState(277);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Complemento_imprimeContext extends ParserRuleContext {
		public Token CTE_LETRERO;
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public Complemento_imprime_auxContext complemento_imprime_aux() {
			return getRuleContext(Complemento_imprime_auxContext.class,0);
		}
		public TerminalNode CTE_LETRERO() { return getToken(PatitoParserParser.CTE_LETRERO, 0); }
		public Complemento_imprimeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_complemento_imprime; }
	}

	public final Complemento_imprimeContext complemento_imprime() throws RecognitionException {
		Complemento_imprimeContext _localctx = new Complemento_imprimeContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_complemento_imprime);
		try {
			setState(286);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
			case CTE_ENTERO:
			case CTE_FLOTANTE:
			case LPAREN:
			case PLUS:
			case MINUS:
				enterOuterAlt(_localctx, 1);
				{
				setState(279);
				expresion();

				val = self.cuadruplo.pop_operating()
				add = self.funcdir.funciones[self.nombrefuncion]["tabla"].get_direccion(val)
				if not add:
				    add = self.constantes.get_direccion(val)
				self.cuadruplo.add_print_Cuadruplo(add)

				setState(281);
				complemento_imprime_aux();
				}
				break;
			case CTE_LETRERO:
				enterOuterAlt(_localctx, 2);
				{
				setState(283);
				((Complemento_imprimeContext)_localctx).CTE_LETRERO = match(CTE_LETRERO);

				direccion = self.contadorletreroconstante
				val = self.constantes.add_constante((((Complemento_imprimeContext)_localctx).CTE_LETRERO!=null?((Complemento_imprimeContext)_localctx).CTE_LETRERO.getText():null),"letrero",direccion)
				self.contadorletreroconstante = direccion + 1
				add = self.constantes.get_direccion(direccion)
				self.cuadruplo.add_print_Cuadruplo(add)

				setState(285);
				complemento_imprime_aux();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Complemento_imprime_auxContext extends ParserRuleContext {
		public List<TerminalNode> COMMA() { return getTokens(PatitoParserParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PatitoParserParser.COMMA, i);
		}
		public List<Complemento_imprimeContext> complemento_imprime() {
			return getRuleContexts(Complemento_imprimeContext.class);
		}
		public Complemento_imprimeContext complemento_imprime(int i) {
			return getRuleContext(Complemento_imprimeContext.class,i);
		}
		public Complemento_imprime_auxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_complemento_imprime_aux; }
	}

	public final Complemento_imprime_auxContext complemento_imprime_aux() throws RecognitionException {
		Complemento_imprime_auxContext _localctx = new Complemento_imprime_auxContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_complemento_imprime_aux);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(292);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(288);
					match(COMMA);
					setState(289);
					complemento_imprime();
					}
					} 
				}
				setState(294);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\"\u0128\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0003\u0001O\b\u0001\u0001\u0002"+
		"\u0005\u0002R\b\u0002\n\u0002\f\u0002U\t\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0004\u0003\\\b\u0003\u000b\u0003"+
		"\f\u0003]\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004c\b\u0004\n\u0004"+
		"\f\u0004f\t\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001"+
		"\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007}\b"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0003\u0007\u0085\b\u0007\u0003\u0007\u0087\b\u0007\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0003\t\u0090\b\t\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0003\n\u0097\b\n\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0003\r\u00a6\b\r\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0003"+
		"\u000e\u00b0\b\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0005\u000f\u00b8\b\u000f\n\u000f\f\u000f\u00bb\t\u000f"+
		"\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0005\u0011\u00c5\b\u0011\n\u0011\f\u0011\u00c8"+
		"\t\u0011\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001"+
		"\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0003\u0013\u00d3\b\u0013\u0001"+
		"\u0014\u0003\u0014\u00d6\b\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001"+
		"\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0003\u0016\u00e0"+
		"\b\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0003\u0017\u00e6"+
		"\b\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001"+
		"\u0019\u0001\u0019\u0001\u0019\u0003\u0019\u00f6\b\u0019\u0001\u001a\u0001"+
		"\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001"+
		"\u001a\u0001\u001a\u0001\u001a\u0001\u001b\u0001\u001b\u0001\u001b\u0001"+
		"\u001b\u0001\u001b\u0001\u001b\u0001\u001c\u0003\u001c\u0109\b\u001c\u0001"+
		"\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0003\u001d\u0110"+
		"\b\u001d\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001"+
		"\u001f\u0001\u001f\u0003\u001f\u011f\b\u001f\u0001 \u0001 \u0005 \u0123"+
		"\b \n \f \u0126\t \u0001 \u0000\u0000!\u0000\u0002\u0004\u0006\b\n\f\u000e"+
		"\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,.02468:<>@\u0000"+
		"\u0003\u0001\u0000\u000b\f\u0001\u0000\u0019\u001a\u0001\u0000\u001b\u001c"+
		"\u0121\u0000B\u0001\u0000\u0000\u0000\u0002N\u0001\u0000\u0000\u0000\u0004"+
		"S\u0001\u0000\u0000\u0000\u0006V\u0001\u0000\u0000\u0000\b_\u0001\u0000"+
		"\u0000\u0000\nj\u0001\u0000\u0000\u0000\fl\u0001\u0000\u0000\u0000\u000e"+
		"\u0086\u0001\u0000\u0000\u0000\u0010\u0088\u0001\u0000\u0000\u0000\u0012"+
		"\u008f\u0001\u0000\u0000\u0000\u0014\u0096\u0001\u0000\u0000\u0000\u0016"+
		"\u0098\u0001\u0000\u0000\u0000\u0018\u009e\u0001\u0000\u0000\u0000\u001a"+
		"\u00a5\u0001\u0000\u0000\u0000\u001c\u00af\u0001\u0000\u0000\u0000\u001e"+
		"\u00b1\u0001\u0000\u0000\u0000 \u00bc\u0001\u0000\u0000\u0000\"\u00be"+
		"\u0001\u0000\u0000\u0000$\u00c9\u0001\u0000\u0000\u0000&\u00d2\u0001\u0000"+
		"\u0000\u0000(\u00d5\u0001\u0000\u0000\u0000*\u00da\u0001\u0000\u0000\u0000"+
		",\u00df\u0001\u0000\u0000\u0000.\u00e5\u0001\u0000\u0000\u00000\u00e7"+
		"\u0001\u0000\u0000\u00002\u00f5\u0001\u0000\u0000\u00004\u00f7\u0001\u0000"+
		"\u0000\u00006\u0101\u0001\u0000\u0000\u00008\u0108\u0001\u0000\u0000\u0000"+
		":\u010f\u0001\u0000\u0000\u0000<\u0111\u0001\u0000\u0000\u0000>\u011e"+
		"\u0001\u0000\u0000\u0000@\u0124\u0001\u0000\u0000\u0000BC\u0005\u0005"+
		"\u0000\u0000CD\u0005\u0001\u0000\u0000DE\u0006\u0000\uffff\uffff\u0000"+
		"EF\u0005\u0017\u0000\u0000FG\u0003\u0002\u0001\u0000GH\u0003\u0004\u0002"+
		"\u0000HI\u0005\u0007\u0000\u0000IJ\u0003\u0010\b\u0000JK\u0005\u000f\u0000"+
		"\u0000KL\u0006\u0000\uffff\uffff\u0000L\u0001\u0001\u0000\u0000\u0000"+
		"MO\u0003\u0006\u0003\u0000NM\u0001\u0000\u0000\u0000NO\u0001\u0000\u0000"+
		"\u0000O\u0003\u0001\u0000\u0000\u0000PR\u0003\f\u0006\u0000QP\u0001\u0000"+
		"\u0000\u0000RU\u0001\u0000\u0000\u0000SQ\u0001\u0000\u0000\u0000ST\u0001"+
		"\u0000\u0000\u0000T\u0005\u0001\u0000\u0000\u0000US\u0001\u0000\u0000"+
		"\u0000V[\u0005\u0010\u0000\u0000WX\u0003\b\u0004\u0000XY\u0006\u0003\uffff"+
		"\uffff\u0000YZ\u0005\u0017\u0000\u0000Z\\\u0001\u0000\u0000\u0000[W\u0001"+
		"\u0000\u0000\u0000\\]\u0001\u0000\u0000\u0000][\u0001\u0000\u0000\u0000"+
		"]^\u0001\u0000\u0000\u0000^\u0007\u0001\u0000\u0000\u0000_d\u0005\u0001"+
		"\u0000\u0000`a\u0005\u0016\u0000\u0000ac\u0005\u0001\u0000\u0000b`\u0001"+
		"\u0000\u0000\u0000cf\u0001\u0000\u0000\u0000db\u0001\u0000\u0000\u0000"+
		"de\u0001\u0000\u0000\u0000eg\u0001\u0000\u0000\u0000fd\u0001\u0000\u0000"+
		"\u0000gh\u0005\u0018\u0000\u0000hi\u0003\n\u0005\u0000i\t\u0001\u0000"+
		"\u0000\u0000jk\u0007\u0000\u0000\u0000k\u000b\u0001\u0000\u0000\u0000"+
		"lm\u0005\u0006\u0000\u0000mn\u0005\u0001\u0000\u0000no\u0006\u0006\uffff"+
		"\uffff\u0000op\u0005\u0012\u0000\u0000pq\u0003\u000e\u0007\u0000qr\u0006"+
		"\u0006\uffff\uffff\u0000rs\u0005\u0013\u0000\u0000st\u0005\u0014\u0000"+
		"\u0000tu\u0003\u0002\u0001\u0000uv\u0003\u0010\b\u0000vw\u0005\u0015\u0000"+
		"\u0000wx\u0005\u0017\u0000\u0000x\r\u0001\u0000\u0000\u0000yz\u0005\u0001"+
		"\u0000\u0000z{\u0005\u0018\u0000\u0000{}\u0003\n\u0005\u0000|y\u0001\u0000"+
		"\u0000\u0000|}\u0001\u0000\u0000\u0000}\u0087\u0001\u0000\u0000\u0000"+
		"~\u007f\u0005\u0001\u0000\u0000\u007f\u0080\u0005\u0018\u0000\u0000\u0080"+
		"\u0081\u0003\n\u0005\u0000\u0081\u0082\u0005\u0016\u0000\u0000\u0082\u0083"+
		"\u0003\u000e\u0007\u0000\u0083\u0085\u0001\u0000\u0000\u0000\u0084~\u0001"+
		"\u0000\u0000\u0000\u0084\u0085\u0001\u0000\u0000\u0000\u0085\u0087\u0001"+
		"\u0000\u0000\u0000\u0086|\u0001\u0000\u0000\u0000\u0086\u0084\u0001\u0000"+
		"\u0000\u0000\u0087\u000f\u0001\u0000\u0000\u0000\u0088\u0089\u0005\u0014"+
		"\u0000\u0000\u0089\u008a\u0003\u0012\t\u0000\u008a\u008b\u0005\u0015\u0000"+
		"\u0000\u008b\u0011\u0001\u0000\u0000\u0000\u008c\u008d\u0003\u0014\n\u0000"+
		"\u008d\u008e\u0003\u0012\t\u0000\u008e\u0090\u0001\u0000\u0000\u0000\u008f"+
		"\u008c\u0001\u0000\u0000\u0000\u008f\u0090\u0001\u0000\u0000\u0000\u0090"+
		"\u0013\u0001\u0000\u0000\u0000\u0091\u0097\u0003\u0016\u000b\u0000\u0092"+
		"\u0097\u00030\u0018\u0000\u0093\u0097\u00034\u001a\u0000\u0094\u0097\u0003"+
		"6\u001b\u0000\u0095\u0097\u0003<\u001e\u0000\u0096\u0091\u0001\u0000\u0000"+
		"\u0000\u0096\u0092\u0001\u0000\u0000\u0000\u0096\u0093\u0001\u0000\u0000"+
		"\u0000\u0096\u0094\u0001\u0000\u0000\u0000\u0096\u0095\u0001\u0000\u0000"+
		"\u0000\u0097\u0015\u0001\u0000\u0000\u0000\u0098\u0099\u0005\u0001\u0000"+
		"\u0000\u0099\u009a\u0005\u001d\u0000\u0000\u009a\u009b\u0003\u0018\f\u0000"+
		"\u009b\u009c\u0006\u000b\uffff\uffff\u0000\u009c\u009d\u0005\u0017\u0000"+
		"\u0000\u009d\u0017\u0001\u0000\u0000\u0000\u009e\u009f\u0003\u001e\u000f"+
		"\u0000\u009f\u00a0\u0003\u001a\r\u0000\u00a0\u0019\u0001\u0000\u0000\u0000"+
		"\u00a1\u00a2\u0003\u001c\u000e\u0000\u00a2\u00a3\u0003\u001e\u000f\u0000"+
		"\u00a3\u00a4\u0006\r\uffff\uffff\u0000\u00a4\u00a6\u0001\u0000\u0000\u0000"+
		"\u00a5\u00a1\u0001\u0000\u0000\u0000\u00a5\u00a6\u0001\u0000\u0000\u0000"+
		"\u00a6\u001b\u0001\u0000\u0000\u0000\u00a7\u00a8\u0005!\u0000\u0000\u00a8"+
		"\u00b0\u0006\u000e\uffff\uffff\u0000\u00a9\u00aa\u0005 \u0000\u0000\u00aa"+
		"\u00b0\u0006\u000e\uffff\uffff\u0000\u00ab\u00ac\u0005\u001e\u0000\u0000"+
		"\u00ac\u00b0\u0006\u000e\uffff\uffff\u0000\u00ad\u00ae\u0005\u001f\u0000"+
		"\u0000\u00ae\u00b0\u0006\u000e\uffff\uffff\u0000\u00af\u00a7\u0001\u0000"+
		"\u0000\u0000\u00af\u00a9\u0001\u0000\u0000\u0000\u00af\u00ab\u0001\u0000"+
		"\u0000\u0000\u00af\u00ad\u0001\u0000\u0000\u0000\u00b0\u001d\u0001\u0000"+
		"\u0000\u0000\u00b1\u00b9\u0003\"\u0011\u0000\u00b2\u00b3\u0003 \u0010"+
		"\u0000\u00b3\u00b4\u0006\u000f\uffff\uffff\u0000\u00b4\u00b5\u0003\"\u0011"+
		"\u0000\u00b5\u00b6\u0006\u000f\uffff\uffff\u0000\u00b6\u00b8\u0001\u0000"+
		"\u0000\u0000\u00b7\u00b2\u0001\u0000\u0000\u0000\u00b8\u00bb\u0001\u0000"+
		"\u0000\u0000\u00b9\u00b7\u0001\u0000\u0000\u0000\u00b9\u00ba\u0001\u0000"+
		"\u0000\u0000\u00ba\u001f\u0001\u0000\u0000\u0000\u00bb\u00b9\u0001\u0000"+
		"\u0000\u0000\u00bc\u00bd\u0007\u0001\u0000\u0000\u00bd!\u0001\u0000\u0000"+
		"\u0000\u00be\u00c6\u0003&\u0013\u0000\u00bf\u00c0\u0003$\u0012\u0000\u00c0"+
		"\u00c1\u0006\u0011\uffff\uffff\u0000\u00c1\u00c2\u0003&\u0013\u0000\u00c2"+
		"\u00c3\u0006\u0011\uffff\uffff\u0000\u00c3\u00c5\u0001\u0000\u0000\u0000"+
		"\u00c4\u00bf\u0001\u0000\u0000\u0000\u00c5\u00c8\u0001\u0000\u0000\u0000"+
		"\u00c6\u00c4\u0001\u0000\u0000\u0000\u00c6\u00c7\u0001\u0000\u0000\u0000"+
		"\u00c7#\u0001\u0000\u0000\u0000\u00c8\u00c6\u0001\u0000\u0000\u0000\u00c9"+
		"\u00ca\u0007\u0002\u0000\u0000\u00ca%\u0001\u0000\u0000\u0000\u00cb\u00cc"+
		"\u0005\u0012\u0000\u0000\u00cc\u00cd\u0003\u0018\f\u0000\u00cd\u00ce\u0005"+
		"\u0013\u0000\u0000\u00ce\u00d3\u0001\u0000\u0000\u0000\u00cf\u00d0\u0003"+
		"(\u0014\u0000\u00d0\u00d1\u0006\u0013\uffff\uffff\u0000\u00d1\u00d3\u0001"+
		"\u0000\u0000\u0000\u00d2\u00cb\u0001\u0000\u0000\u0000\u00d2\u00cf\u0001"+
		"\u0000\u0000\u0000\u00d3\'\u0001\u0000\u0000\u0000\u00d4\u00d6\u0003*"+
		"\u0015\u0000\u00d5\u00d4\u0001\u0000\u0000\u0000\u00d5\u00d6\u0001\u0000"+
		"\u0000\u0000\u00d6\u00d7\u0001\u0000\u0000\u0000\u00d7\u00d8\u0003,\u0016"+
		"\u0000\u00d8\u00d9\u0006\u0014\uffff\uffff\u0000\u00d9)\u0001\u0000\u0000"+
		"\u0000\u00da\u00db\u0007\u0001\u0000\u0000\u00db+\u0001\u0000\u0000\u0000"+
		"\u00dc\u00dd\u0005\u0001\u0000\u0000\u00dd\u00e0\u0006\u0016\uffff\uffff"+
		"\u0000\u00de\u00e0\u0003.\u0017\u0000\u00df\u00dc\u0001\u0000\u0000\u0000"+
		"\u00df\u00de\u0001\u0000\u0000\u0000\u00e0-\u0001\u0000\u0000\u0000\u00e1"+
		"\u00e2\u0005\u0003\u0000\u0000\u00e2\u00e6\u0006\u0017\uffff\uffff\u0000"+
		"\u00e3\u00e4\u0005\u0004\u0000\u0000\u00e4\u00e6\u0006\u0017\uffff\uffff"+
		"\u0000\u00e5\u00e1\u0001\u0000\u0000\u0000\u00e5\u00e3\u0001\u0000\u0000"+
		"\u0000\u00e6/\u0001\u0000\u0000\u0000\u00e7\u00e8\u0005\t\u0000\u0000"+
		"\u00e8\u00e9\u0005\u0012\u0000\u0000\u00e9\u00ea\u0003\u0018\f\u0000\u00ea"+
		"\u00eb\u0005\u0013\u0000\u0000\u00eb\u00ec\u0006\u0018\uffff\uffff\u0000"+
		"\u00ec\u00ed\u0005\u0011\u0000\u0000\u00ed\u00ee\u0003\u0010\b\u0000\u00ee"+
		"\u00ef\u00032\u0019\u0000\u00ef\u00f0\u0005\u0017\u0000\u0000\u00f0\u00f1"+
		"\u0006\u0018\uffff\uffff\u0000\u00f11\u0001\u0000\u0000\u0000\u00f2\u00f3"+
		"\u0005\n\u0000\u0000\u00f3\u00f4\u0006\u0019\uffff\uffff\u0000\u00f4\u00f6"+
		"\u0003\u0010\b\u0000\u00f5\u00f2\u0001\u0000\u0000\u0000\u00f5\u00f6\u0001"+
		"\u0000\u0000\u0000\u00f63\u0001\u0000\u0000\u0000\u00f7\u00f8\u0005\b"+
		"\u0000\u0000\u00f8\u00f9\u0005\u0012\u0000\u0000\u00f9\u00fa\u0003\u0018"+
		"\f\u0000\u00fa\u00fb\u0005\u0013\u0000\u0000\u00fb\u00fc\u0005\u0011\u0000"+
		"\u0000\u00fc\u00fd\u0006\u001a\uffff\uffff\u0000\u00fd\u00fe\u0003\u0010"+
		"\b\u0000\u00fe\u00ff\u0005\u0017\u0000\u0000\u00ff\u0100\u0006\u001a\uffff"+
		"\uffff\u0000\u01005\u0001\u0000\u0000\u0000\u0101\u0102\u0005\u0001\u0000"+
		"\u0000\u0102\u0103\u0005\u0012\u0000\u0000\u0103\u0104\u00038\u001c\u0000"+
		"\u0104\u0105\u0005\u0013\u0000\u0000\u0105\u0106\u0005\u0017\u0000\u0000"+
		"\u01067\u0001\u0000\u0000\u0000\u0107\u0109\u0003:\u001d\u0000\u0108\u0107"+
		"\u0001\u0000\u0000\u0000\u0108\u0109\u0001\u0000\u0000\u0000\u01099\u0001"+
		"\u0000\u0000\u0000\u010a\u0110\u0003\u0018\f\u0000\u010b\u010c\u0003\u0018"+
		"\f\u0000\u010c\u010d\u0005\u0016\u0000\u0000\u010d\u010e\u0003:\u001d"+
		"\u0000\u010e\u0110\u0001\u0000\u0000\u0000\u010f\u010a\u0001\u0000\u0000"+
		"\u0000\u010f\u010b\u0001\u0000\u0000\u0000\u0110;\u0001\u0000\u0000\u0000"+
		"\u0111\u0112\u0005\r\u0000\u0000\u0112\u0113\u0005\u0012\u0000\u0000\u0113"+
		"\u0114\u0003>\u001f\u0000\u0114\u0115\u0005\u0013\u0000\u0000\u0115\u0116"+
		"\u0005\u0017\u0000\u0000\u0116=\u0001\u0000\u0000\u0000\u0117\u0118\u0003"+
		"\u0018\f\u0000\u0118\u0119\u0006\u001f\uffff\uffff\u0000\u0119\u011a\u0003"+
		"@ \u0000\u011a\u011f\u0001\u0000\u0000\u0000\u011b\u011c\u0005\u0002\u0000"+
		"\u0000\u011c\u011d\u0006\u001f\uffff\uffff\u0000\u011d\u011f\u0003@ \u0000"+
		"\u011e\u0117\u0001\u0000\u0000\u0000\u011e\u011b\u0001\u0000\u0000\u0000"+
		"\u011f?\u0001\u0000\u0000\u0000\u0120\u0121\u0005\u0016\u0000\u0000\u0121"+
		"\u0123\u0003>\u001f\u0000\u0122\u0120\u0001\u0000\u0000\u0000\u0123\u0126"+
		"\u0001\u0000\u0000\u0000\u0124\u0122\u0001\u0000\u0000\u0000\u0124\u0125"+
		"\u0001\u0000\u0000\u0000\u0125A\u0001\u0000\u0000\u0000\u0126\u0124\u0001"+
		"\u0000\u0000\u0000\u0016NS]d|\u0084\u0086\u008f\u0096\u00a5\u00af\u00b9"+
		"\u00c6\u00d2\u00d5\u00df\u00e5\u00f5\u0108\u010f\u011e\u0124";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}