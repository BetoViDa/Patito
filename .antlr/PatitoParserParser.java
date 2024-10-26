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
		RULE_exp = 14, RULE_complemento_exp = 15, RULE_termino = 16, RULE_complemento_termino = 17, 
		RULE_factor = 18, RULE_tiene_signo = 19, RULE_tiene_var = 20, RULE_cte = 21, 
		RULE_condicion = 22, RULE_complemento_cond = 23, RULE_ciclo = 24, RULE_llamada = 25, 
		RULE_complemento_llamada = 26, RULE_tiene_expresion = 27, RULE_imprime = 28, 
		RULE_complemento_imprime = 29;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "tiene_variables", "tiene_funciones", "vars", "complemento_vars", 
			"tipo", "funcs", "complemento_funcs", "cuerpo", "tiene_estatuto", "estatuto", 
			"asigna", "expresion", "complemento_expresion", "exp", "complemento_exp", 
			"termino", "complemento_termino", "factor", "tiene_signo", "tiene_var", 
			"cte", "condicion", "complemento_cond", "ciclo", "llamada", "complemento_llamada", 
			"tiene_expresion", "imprime", "complemento_imprime"
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

	public PatitoParserParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramaContext extends ParserRuleContext {
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
			setState(60);
			match(PROGRAM);
			setState(61);
			match(ID);
			setState(62);
			match(SEMI);
			setState(63);
			tiene_variables();
			setState(64);
			tiene_funciones();
			setState(65);
			match(INICIO);
			setState(66);
			cuerpo();
			setState(67);
			match(FIN);
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
			setState(70);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VARS) {
				{
				setState(69);
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
			setState(75);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NULA) {
				{
				{
				setState(72);
				funcs();
				}
				}
				setState(77);
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
		public TerminalNode VARS() { return getToken(PatitoParserParser.VARS, 0); }
		public Complemento_varsContext complemento_vars() {
			return getRuleContext(Complemento_varsContext.class,0);
		}
		public VarsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vars; }
	}

	public final VarsContext vars() throws RecognitionException {
		VarsContext _localctx = new VarsContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_vars);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			match(VARS);
			setState(79);
			complemento_vars();
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
		public TerminalNode ID() { return getToken(PatitoParserParser.ID, 0); }
		public TerminalNode COMMA() { return getToken(PatitoParserParser.COMMA, 0); }
		public Complemento_varsContext complemento_vars() {
			return getRuleContext(Complemento_varsContext.class,0);
		}
		public TerminalNode COLON() { return getToken(PatitoParserParser.COLON, 0); }
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(PatitoParserParser.SEMI, 0); }
		public Complemento_varsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_complemento_vars; }
	}

	public final Complemento_varsContext complemento_vars() throws RecognitionException {
		Complemento_varsContext _localctx = new Complemento_varsContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_complemento_vars);
		try {
			setState(95);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(81);
				match(ID);
				setState(82);
				match(COMMA);
				setState(83);
				complemento_vars();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(84);
				match(ID);
				setState(85);
				match(COLON);
				setState(86);
				tipo();
				setState(87);
				match(SEMI);
				setState(88);
				complemento_vars();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(90);
				match(ID);
				setState(91);
				match(COLON);
				setState(92);
				tipo();
				setState(93);
				match(SEMI);
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
			setState(97);
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
			setState(99);
			match(NULA);
			setState(100);
			match(ID);
			setState(101);
			match(LPAREN);
			setState(102);
			complemento_funcs();
			setState(103);
			match(RPAREN);
			setState(104);
			match(LBRACE);
			setState(105);
			tiene_variables();
			setState(106);
			cuerpo();
			setState(107);
			match(RBRACE);
			setState(108);
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
			setState(123);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(113);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ID) {
					{
					setState(110);
					match(ID);
					setState(111);
					match(COLON);
					setState(112);
					tipo();
					}
				}

				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(121);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ID) {
					{
					setState(115);
					match(ID);
					setState(116);
					match(COLON);
					setState(117);
					tipo();
					setState(118);
					match(COMMA);
					setState(119);
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
			setState(125);
			match(LBRACE);
			setState(126);
			tiene_estatuto();
			setState(127);
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
			setState(132);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8962L) != 0)) {
				{
				setState(129);
				estatuto();
				setState(130);
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
			setState(139);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(134);
				asigna();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(135);
				condicion();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(136);
				ciclo();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(137);
				llamada();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(138);
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
			setState(141);
			match(ID);
			setState(142);
			match(EQUAL);
			setState(143);
			expresion();
			setState(144);
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
			setState(146);
			exp();
			setState(147);
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
		public TerminalNode GT() { return getToken(PatitoParserParser.GT, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode LT() { return getToken(PatitoParserParser.LT, 0); }
		public TerminalNode MINUS() { return getToken(PatitoParserParser.MINUS, 0); }
		public TerminalNode DEQ() { return getToken(PatitoParserParser.DEQ, 0); }
		public Complemento_expresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_complemento_expresion; }
	}

	public final Complemento_expresionContext complemento_expresion() throws RecognitionException {
		Complemento_expresionContext _localctx = new Complemento_expresionContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_complemento_expresion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(157);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case GT:
				{
				setState(149);
				match(GT);
				setState(150);
				exp();
				}
				break;
			case LT:
				{
				setState(151);
				match(LT);
				setState(152);
				exp();
				}
				break;
			case MINUS:
				{
				setState(153);
				match(MINUS);
				setState(154);
				exp();
				}
				break;
			case DEQ:
				{
				setState(155);
				match(DEQ);
				setState(156);
				exp();
				}
				break;
			case RPAREN:
			case COMMA:
			case SEMI:
				break;
			default:
				break;
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
	public static class ExpContext extends ParserRuleContext {
		public TerminoContext termino() {
			return getRuleContext(TerminoContext.class,0);
		}
		public Complemento_expContext complemento_exp() {
			return getRuleContext(Complemento_expContext.class,0);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_exp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(159);
			termino();
			setState(160);
			complemento_exp();
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
	public static class Complemento_expContext extends ParserRuleContext {
		public TerminalNode PLUS() { return getToken(PatitoParserParser.PLUS, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode MINUS() { return getToken(PatitoParserParser.MINUS, 0); }
		public Complemento_expContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_complemento_exp; }
	}

	public final Complemento_expContext complemento_exp() throws RecognitionException {
		Complemento_expContext _localctx = new Complemento_expContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_complemento_exp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(166);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				{
				setState(162);
				match(PLUS);
				setState(163);
				exp();
				}
				break;
			case 2:
				{
				setState(164);
				match(MINUS);
				setState(165);
				exp();
				}
				break;
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
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public Complemento_terminoContext complemento_termino() {
			return getRuleContext(Complemento_terminoContext.class,0);
		}
		public TerminoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termino; }
	}

	public final TerminoContext termino() throws RecognitionException {
		TerminoContext _localctx = new TerminoContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_termino);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(168);
			factor();
			setState(169);
			complemento_termino();
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
	public static class Complemento_terminoContext extends ParserRuleContext {
		public TerminalNode MUL() { return getToken(PatitoParserParser.MUL, 0); }
		public TerminoContext termino() {
			return getRuleContext(TerminoContext.class,0);
		}
		public TerminalNode DIV() { return getToken(PatitoParserParser.DIV, 0); }
		public Complemento_terminoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_complemento_termino; }
	}

	public final Complemento_terminoContext complemento_termino() throws RecognitionException {
		Complemento_terminoContext _localctx = new Complemento_terminoContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_complemento_termino);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(175);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MUL:
				{
				setState(171);
				match(MUL);
				setState(172);
				termino();
				}
				break;
			case DIV:
				{
				setState(173);
				match(DIV);
				setState(174);
				termino();
				}
				break;
			case RPAREN:
			case COMMA:
			case SEMI:
			case PLUS:
			case MINUS:
			case DEQ:
			case LT:
			case GT:
				break;
			default:
				break;
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
		public TerminalNode LPAREN() { return getToken(PatitoParserParser.LPAREN, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(PatitoParserParser.RPAREN, 0); }
		public Tiene_signoContext tiene_signo() {
			return getRuleContext(Tiene_signoContext.class,0);
		}
		public Tiene_varContext tiene_var() {
			return getRuleContext(Tiene_varContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_factor);
		try {
			setState(184);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LPAREN:
				enterOuterAlt(_localctx, 1);
				{
				setState(177);
				match(LPAREN);
				setState(178);
				expresion();
				setState(179);
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
				setState(181);
				tiene_signo();
				setState(182);
				tiene_var();
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
		enterRule(_localctx, 38, RULE_tiene_signo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(187);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PLUS || _la==MINUS) {
				{
				setState(186);
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
		enterRule(_localctx, 40, RULE_tiene_var);
		try {
			setState(191);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(189);
				match(ID);
				}
				break;
			case CTE_ENTERO:
			case CTE_FLOTANTE:
				enterOuterAlt(_localctx, 2);
				{
				setState(190);
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
		public TerminalNode CTE_ENTERO() { return getToken(PatitoParserParser.CTE_ENTERO, 0); }
		public TerminalNode CTE_FLOTANTE() { return getToken(PatitoParserParser.CTE_FLOTANTE, 0); }
		public CteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cte; }
	}

	public final CteContext cte() throws RecognitionException {
		CteContext _localctx = new CteContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_cte);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(193);
			_la = _input.LA(1);
			if ( !(_la==CTE_ENTERO || _la==CTE_FLOTANTE) ) {
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
		enterRule(_localctx, 44, RULE_condicion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(195);
			match(SI);
			setState(196);
			match(LPAREN);
			setState(197);
			expresion();
			setState(198);
			match(RPAREN);
			setState(199);
			match(HAZ);
			setState(200);
			cuerpo();
			setState(201);
			complemento_cond();
			setState(202);
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
		enterRule(_localctx, 46, RULE_complemento_cond);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(206);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SINO) {
				{
				setState(204);
				match(SINO);
				setState(205);
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
		enterRule(_localctx, 48, RULE_ciclo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(208);
			match(MIENTRAS);
			setState(209);
			match(LPAREN);
			setState(210);
			expresion();
			setState(211);
			match(RPAREN);
			setState(212);
			match(HAZ);
			setState(213);
			cuerpo();
			setState(214);
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
		enterRule(_localctx, 50, RULE_llamada);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(216);
			match(ID);
			setState(217);
			match(LPAREN);
			setState(218);
			complemento_llamada();
			setState(219);
			match(RPAREN);
			setState(220);
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
		enterRule(_localctx, 52, RULE_complemento_llamada);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(223);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 100925466L) != 0)) {
				{
				setState(222);
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
		enterRule(_localctx, 54, RULE_tiene_expresion);
		try {
			setState(230);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(225);
				expresion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(226);
				expresion();
				setState(227);
				match(COMMA);
				setState(228);
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
		enterRule(_localctx, 56, RULE_imprime);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(232);
			match(ESCRIBE);
			setState(233);
			match(LPAREN);
			setState(234);
			complemento_imprime();
			setState(235);
			match(RPAREN);
			setState(236);
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
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode CTE_LETRERO() { return getToken(PatitoParserParser.CTE_LETRERO, 0); }
		public TerminalNode COMMA() { return getToken(PatitoParserParser.COMMA, 0); }
		public Complemento_imprimeContext complemento_imprime() {
			return getRuleContext(Complemento_imprimeContext.class,0);
		}
		public Complemento_imprimeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_complemento_imprime; }
	}

	public final Complemento_imprimeContext complemento_imprime() throws RecognitionException {
		Complemento_imprimeContext _localctx = new Complemento_imprimeContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_complemento_imprime);
		try {
			setState(247);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(238);
				expresion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(239);
				match(CTE_LETRERO);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(240);
				expresion();
				setState(241);
				match(COMMA);
				setState(242);
				complemento_imprime();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(244);
				match(CTE_LETRERO);
				setState(245);
				match(COMMA);
				setState(246);
				complemento_imprime();
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

	public static final String _serializedATN =
		"\u0004\u0001\"\u00fa\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0003\u0001G\b\u0001\u0001\u0002\u0005\u0002"+
		"J\b\u0002\n\u0002\f\u0002M\t\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0003\u0004`\b\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0003\u0007r\b\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007z\b\u0007"+
		"\u0003\u0007|\b\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t"+
		"\u0001\t\u0003\t\u0085\b\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003"+
		"\n\u008c\b\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0003\r\u009e\b\r\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u00a7\b\u000f"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0003\u0011\u00b0\b\u0011\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0003\u0012\u00b9\b\u0012"+
		"\u0001\u0013\u0003\u0013\u00bc\b\u0013\u0001\u0014\u0001\u0014\u0003\u0014"+
		"\u00c0\b\u0014\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0001\u0017\u0001\u0017\u0003\u0017\u00cf\b\u0017\u0001\u0018\u0001\u0018"+
		"\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018"+
		"\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019"+
		"\u0001\u001a\u0003\u001a\u00e0\b\u001a\u0001\u001b\u0001\u001b\u0001\u001b"+
		"\u0001\u001b\u0001\u001b\u0003\u001b\u00e7\b\u001b\u0001\u001c\u0001\u001c"+
		"\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001d\u0001\u001d"+
		"\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d"+
		"\u0001\u001d\u0003\u001d\u00f8\b\u001d\u0001\u001d\u0000\u0000\u001e\u0000"+
		"\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c"+
		"\u001e \"$&(*,.02468:\u0000\u0003\u0001\u0000\u000b\f\u0001\u0000\u0019"+
		"\u001a\u0001\u0000\u0003\u0004\u00f8\u0000<\u0001\u0000\u0000\u0000\u0002"+
		"F\u0001\u0000\u0000\u0000\u0004K\u0001\u0000\u0000\u0000\u0006N\u0001"+
		"\u0000\u0000\u0000\b_\u0001\u0000\u0000\u0000\na\u0001\u0000\u0000\u0000"+
		"\fc\u0001\u0000\u0000\u0000\u000e{\u0001\u0000\u0000\u0000\u0010}\u0001"+
		"\u0000\u0000\u0000\u0012\u0084\u0001\u0000\u0000\u0000\u0014\u008b\u0001"+
		"\u0000\u0000\u0000\u0016\u008d\u0001\u0000\u0000\u0000\u0018\u0092\u0001"+
		"\u0000\u0000\u0000\u001a\u009d\u0001\u0000\u0000\u0000\u001c\u009f\u0001"+
		"\u0000\u0000\u0000\u001e\u00a6\u0001\u0000\u0000\u0000 \u00a8\u0001\u0000"+
		"\u0000\u0000\"\u00af\u0001\u0000\u0000\u0000$\u00b8\u0001\u0000\u0000"+
		"\u0000&\u00bb\u0001\u0000\u0000\u0000(\u00bf\u0001\u0000\u0000\u0000*"+
		"\u00c1\u0001\u0000\u0000\u0000,\u00c3\u0001\u0000\u0000\u0000.\u00ce\u0001"+
		"\u0000\u0000\u00000\u00d0\u0001\u0000\u0000\u00002\u00d8\u0001\u0000\u0000"+
		"\u00004\u00df\u0001\u0000\u0000\u00006\u00e6\u0001\u0000\u0000\u00008"+
		"\u00e8\u0001\u0000\u0000\u0000:\u00f7\u0001\u0000\u0000\u0000<=\u0005"+
		"\u0005\u0000\u0000=>\u0005\u0001\u0000\u0000>?\u0005\u0017\u0000\u0000"+
		"?@\u0003\u0002\u0001\u0000@A\u0003\u0004\u0002\u0000AB\u0005\u0007\u0000"+
		"\u0000BC\u0003\u0010\b\u0000CD\u0005\u000f\u0000\u0000D\u0001\u0001\u0000"+
		"\u0000\u0000EG\u0003\u0006\u0003\u0000FE\u0001\u0000\u0000\u0000FG\u0001"+
		"\u0000\u0000\u0000G\u0003\u0001\u0000\u0000\u0000HJ\u0003\f\u0006\u0000"+
		"IH\u0001\u0000\u0000\u0000JM\u0001\u0000\u0000\u0000KI\u0001\u0000\u0000"+
		"\u0000KL\u0001\u0000\u0000\u0000L\u0005\u0001\u0000\u0000\u0000MK\u0001"+
		"\u0000\u0000\u0000NO\u0005\u0010\u0000\u0000OP\u0003\b\u0004\u0000P\u0007"+
		"\u0001\u0000\u0000\u0000QR\u0005\u0001\u0000\u0000RS\u0005\u0016\u0000"+
		"\u0000S`\u0003\b\u0004\u0000TU\u0005\u0001\u0000\u0000UV\u0005\u0018\u0000"+
		"\u0000VW\u0003\n\u0005\u0000WX\u0005\u0017\u0000\u0000XY\u0003\b\u0004"+
		"\u0000Y`\u0001\u0000\u0000\u0000Z[\u0005\u0001\u0000\u0000[\\\u0005\u0018"+
		"\u0000\u0000\\]\u0003\n\u0005\u0000]^\u0005\u0017\u0000\u0000^`\u0001"+
		"\u0000\u0000\u0000_Q\u0001\u0000\u0000\u0000_T\u0001\u0000\u0000\u0000"+
		"_Z\u0001\u0000\u0000\u0000`\t\u0001\u0000\u0000\u0000ab\u0007\u0000\u0000"+
		"\u0000b\u000b\u0001\u0000\u0000\u0000cd\u0005\u0006\u0000\u0000de\u0005"+
		"\u0001\u0000\u0000ef\u0005\u0012\u0000\u0000fg\u0003\u000e\u0007\u0000"+
		"gh\u0005\u0013\u0000\u0000hi\u0005\u0014\u0000\u0000ij\u0003\u0002\u0001"+
		"\u0000jk\u0003\u0010\b\u0000kl\u0005\u0015\u0000\u0000lm\u0005\u0017\u0000"+
		"\u0000m\r\u0001\u0000\u0000\u0000no\u0005\u0001\u0000\u0000op\u0005\u0018"+
		"\u0000\u0000pr\u0003\n\u0005\u0000qn\u0001\u0000\u0000\u0000qr\u0001\u0000"+
		"\u0000\u0000r|\u0001\u0000\u0000\u0000st\u0005\u0001\u0000\u0000tu\u0005"+
		"\u0018\u0000\u0000uv\u0003\n\u0005\u0000vw\u0005\u0016\u0000\u0000wx\u0003"+
		"\u000e\u0007\u0000xz\u0001\u0000\u0000\u0000ys\u0001\u0000\u0000\u0000"+
		"yz\u0001\u0000\u0000\u0000z|\u0001\u0000\u0000\u0000{q\u0001\u0000\u0000"+
		"\u0000{y\u0001\u0000\u0000\u0000|\u000f\u0001\u0000\u0000\u0000}~\u0005"+
		"\u0014\u0000\u0000~\u007f\u0003\u0012\t\u0000\u007f\u0080\u0005\u0015"+
		"\u0000\u0000\u0080\u0011\u0001\u0000\u0000\u0000\u0081\u0082\u0003\u0014"+
		"\n\u0000\u0082\u0083\u0003\u0012\t\u0000\u0083\u0085\u0001\u0000\u0000"+
		"\u0000\u0084\u0081\u0001\u0000\u0000\u0000\u0084\u0085\u0001\u0000\u0000"+
		"\u0000\u0085\u0013\u0001\u0000\u0000\u0000\u0086\u008c\u0003\u0016\u000b"+
		"\u0000\u0087\u008c\u0003,\u0016\u0000\u0088\u008c\u00030\u0018\u0000\u0089"+
		"\u008c\u00032\u0019\u0000\u008a\u008c\u00038\u001c\u0000\u008b\u0086\u0001"+
		"\u0000\u0000\u0000\u008b\u0087\u0001\u0000\u0000\u0000\u008b\u0088\u0001"+
		"\u0000\u0000\u0000\u008b\u0089\u0001\u0000\u0000\u0000\u008b\u008a\u0001"+
		"\u0000\u0000\u0000\u008c\u0015\u0001\u0000\u0000\u0000\u008d\u008e\u0005"+
		"\u0001\u0000\u0000\u008e\u008f\u0005\u001d\u0000\u0000\u008f\u0090\u0003"+
		"\u0018\f\u0000\u0090\u0091\u0005\u0017\u0000\u0000\u0091\u0017\u0001\u0000"+
		"\u0000\u0000\u0092\u0093\u0003\u001c\u000e\u0000\u0093\u0094\u0003\u001a"+
		"\r\u0000\u0094\u0019\u0001\u0000\u0000\u0000\u0095\u0096\u0005!\u0000"+
		"\u0000\u0096\u009e\u0003\u001c\u000e\u0000\u0097\u0098\u0005 \u0000\u0000"+
		"\u0098\u009e\u0003\u001c\u000e\u0000\u0099\u009a\u0005\u001a\u0000\u0000"+
		"\u009a\u009e\u0003\u001c\u000e\u0000\u009b\u009c\u0005\u001f\u0000\u0000"+
		"\u009c\u009e\u0003\u001c\u000e\u0000\u009d\u0095\u0001\u0000\u0000\u0000"+
		"\u009d\u0097\u0001\u0000\u0000\u0000\u009d\u0099\u0001\u0000\u0000\u0000"+
		"\u009d\u009b\u0001\u0000\u0000\u0000\u009d\u009e\u0001\u0000\u0000\u0000"+
		"\u009e\u001b\u0001\u0000\u0000\u0000\u009f\u00a0\u0003 \u0010\u0000\u00a0"+
		"\u00a1\u0003\u001e\u000f\u0000\u00a1\u001d\u0001\u0000\u0000\u0000\u00a2"+
		"\u00a3\u0005\u0019\u0000\u0000\u00a3\u00a7\u0003\u001c\u000e\u0000\u00a4"+
		"\u00a5\u0005\u001a\u0000\u0000\u00a5\u00a7\u0003\u001c\u000e\u0000\u00a6"+
		"\u00a2\u0001\u0000\u0000\u0000\u00a6\u00a4\u0001\u0000\u0000\u0000\u00a6"+
		"\u00a7\u0001\u0000\u0000\u0000\u00a7\u001f\u0001\u0000\u0000\u0000\u00a8"+
		"\u00a9\u0003$\u0012\u0000\u00a9\u00aa\u0003\"\u0011\u0000\u00aa!\u0001"+
		"\u0000\u0000\u0000\u00ab\u00ac\u0005\u001b\u0000\u0000\u00ac\u00b0\u0003"+
		" \u0010\u0000\u00ad\u00ae\u0005\u001c\u0000\u0000\u00ae\u00b0\u0003 \u0010"+
		"\u0000\u00af\u00ab\u0001\u0000\u0000\u0000\u00af\u00ad\u0001\u0000\u0000"+
		"\u0000\u00af\u00b0\u0001\u0000\u0000\u0000\u00b0#\u0001\u0000\u0000\u0000"+
		"\u00b1\u00b2\u0005\u0012\u0000\u0000\u00b2\u00b3\u0003\u0018\f\u0000\u00b3"+
		"\u00b4\u0005\u0013\u0000\u0000\u00b4\u00b9\u0001\u0000\u0000\u0000\u00b5"+
		"\u00b6\u0003&\u0013\u0000\u00b6\u00b7\u0003(\u0014\u0000\u00b7\u00b9\u0001"+
		"\u0000\u0000\u0000\u00b8\u00b1\u0001\u0000\u0000\u0000\u00b8\u00b5\u0001"+
		"\u0000\u0000\u0000\u00b9%\u0001\u0000\u0000\u0000\u00ba\u00bc\u0007\u0001"+
		"\u0000\u0000\u00bb\u00ba\u0001\u0000\u0000\u0000\u00bb\u00bc\u0001\u0000"+
		"\u0000\u0000\u00bc\'\u0001\u0000\u0000\u0000\u00bd\u00c0\u0005\u0001\u0000"+
		"\u0000\u00be\u00c0\u0003*\u0015\u0000\u00bf\u00bd\u0001\u0000\u0000\u0000"+
		"\u00bf\u00be\u0001\u0000\u0000\u0000\u00c0)\u0001\u0000\u0000\u0000\u00c1"+
		"\u00c2\u0007\u0002\u0000\u0000\u00c2+\u0001\u0000\u0000\u0000\u00c3\u00c4"+
		"\u0005\t\u0000\u0000\u00c4\u00c5\u0005\u0012\u0000\u0000\u00c5\u00c6\u0003"+
		"\u0018\f\u0000\u00c6\u00c7\u0005\u0013\u0000\u0000\u00c7\u00c8\u0005\u0011"+
		"\u0000\u0000\u00c8\u00c9\u0003\u0010\b\u0000\u00c9\u00ca\u0003.\u0017"+
		"\u0000\u00ca\u00cb\u0005\u0017\u0000\u0000\u00cb-\u0001\u0000\u0000\u0000"+
		"\u00cc\u00cd\u0005\n\u0000\u0000\u00cd\u00cf\u0003\u0010\b\u0000\u00ce"+
		"\u00cc\u0001\u0000\u0000\u0000\u00ce\u00cf\u0001\u0000\u0000\u0000\u00cf"+
		"/\u0001\u0000\u0000\u0000\u00d0\u00d1\u0005\b\u0000\u0000\u00d1\u00d2"+
		"\u0005\u0012\u0000\u0000\u00d2\u00d3\u0003\u0018\f\u0000\u00d3\u00d4\u0005"+
		"\u0013\u0000\u0000\u00d4\u00d5\u0005\u0011\u0000\u0000\u00d5\u00d6\u0003"+
		"\u0010\b\u0000\u00d6\u00d7\u0005\u0017\u0000\u0000\u00d71\u0001\u0000"+
		"\u0000\u0000\u00d8\u00d9\u0005\u0001\u0000\u0000\u00d9\u00da\u0005\u0012"+
		"\u0000\u0000\u00da\u00db\u00034\u001a\u0000\u00db\u00dc\u0005\u0013\u0000"+
		"\u0000\u00dc\u00dd\u0005\u0017\u0000\u0000\u00dd3\u0001\u0000\u0000\u0000"+
		"\u00de\u00e0\u00036\u001b\u0000\u00df\u00de\u0001\u0000\u0000\u0000\u00df"+
		"\u00e0\u0001\u0000\u0000\u0000\u00e05\u0001\u0000\u0000\u0000\u00e1\u00e7"+
		"\u0003\u0018\f\u0000\u00e2\u00e3\u0003\u0018\f\u0000\u00e3\u00e4\u0005"+
		"\u0016\u0000\u0000\u00e4\u00e5\u00036\u001b\u0000\u00e5\u00e7\u0001\u0000"+
		"\u0000\u0000\u00e6\u00e1\u0001\u0000\u0000\u0000\u00e6\u00e2\u0001\u0000"+
		"\u0000\u0000\u00e77\u0001\u0000\u0000\u0000\u00e8\u00e9\u0005\r\u0000"+
		"\u0000\u00e9\u00ea\u0005\u0012\u0000\u0000\u00ea\u00eb\u0003:\u001d\u0000"+
		"\u00eb\u00ec\u0005\u0013\u0000\u0000\u00ec\u00ed\u0005\u0017\u0000\u0000"+
		"\u00ed9\u0001\u0000\u0000\u0000\u00ee\u00f8\u0003\u0018\f\u0000\u00ef"+
		"\u00f8\u0005\u0002\u0000\u0000\u00f0\u00f1\u0003\u0018\f\u0000\u00f1\u00f2"+
		"\u0005\u0016\u0000\u0000\u00f2\u00f3\u0003:\u001d\u0000\u00f3\u00f8\u0001"+
		"\u0000\u0000\u0000\u00f4\u00f5\u0005\u0002\u0000\u0000\u00f5\u00f6\u0005"+
		"\u0016\u0000\u0000\u00f6\u00f8\u0003:\u001d\u0000\u00f7\u00ee\u0001\u0000"+
		"\u0000\u0000\u00f7\u00ef\u0001\u0000\u0000\u0000\u00f7\u00f0\u0001\u0000"+
		"\u0000\u0000\u00f7\u00f4\u0001\u0000\u0000\u0000\u00f8;\u0001\u0000\u0000"+
		"\u0000\u0012FK_qy{\u0084\u008b\u009d\u00a6\u00af\u00b8\u00bb\u00bf\u00ce"+
		"\u00df\u00e6\u00f7";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}