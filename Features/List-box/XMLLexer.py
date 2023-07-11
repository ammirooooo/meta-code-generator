# Generated from XML.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("U\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\7\6\7&\n\7\r\7\16\7")
        buf.write("\'\3\b\3\b\7\b,\n\b\f\b\16\b/\13\b\3\t\3\t\3\t\7\t\64")
        buf.write("\n\t\f\t\16\t\67\13\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\nK\n\n\3\n")
        buf.write("\3\n\3\13\6\13P\n\13\r\13\16\13Q\3\13\3\13\2\2\f\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\3\2\7\4\2((>")
        buf.write(">\6\2<<C\\aac|\7\2/\60\62<C\\aac|\4\2$$>>\5\2\13\f\17")
        buf.write("\17\"\"\2]\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\3\27\3\2\2\2\5\32\3\2\2\2")
        buf.write("\7\34\3\2\2\2\t\36\3\2\2\2\13!\3\2\2\2\r%\3\2\2\2\17)")
        buf.write("\3\2\2\2\21\60\3\2\2\2\23:\3\2\2\2\25O\3\2\2\2\27\30\7")
        buf.write("\61\2\2\30\31\7@\2\2\31\4\3\2\2\2\32\33\7?\2\2\33\6\3")
        buf.write("\2\2\2\34\35\7>\2\2\35\b\3\2\2\2\36\37\7>\2\2\37 \7\61")
        buf.write("\2\2 \n\3\2\2\2!\"\7>\2\2\"#\7#\2\2#\f\3\2\2\2$&\n\2\2")
        buf.write("\2%$\3\2\2\2&\'\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2(\16\3\2")
        buf.write("\2\2)-\t\3\2\2*,\t\4\2\2+*\3\2\2\2,/\3\2\2\2-+\3\2\2\2")
        buf.write("-.\3\2\2\2.\20\3\2\2\2/-\3\2\2\2\60\65\7$\2\2\61\64\n")
        buf.write("\5\2\2\62\64\5\23\n\2\63\61\3\2\2\2\63\62\3\2\2\2\64\67")
        buf.write("\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\668\3\2\2\2\67\65")
        buf.write("\3\2\2\289\7$\2\29\22\3\2\2\2:J\7(\2\2;<\7n\2\2<K\7v\2")
        buf.write("\2=>\7i\2\2>K\7v\2\2?@\7c\2\2@A\7o\2\2AK\7r\2\2BC\7c\2")
        buf.write("\2CD\7r\2\2DE\7q\2\2EK\7u\2\2FG\7s\2\2GH\7w\2\2HI\7q\2")
        buf.write("\2IK\7v\2\2J;\3\2\2\2J=\3\2\2\2J?\3\2\2\2JB\3\2\2\2JF")
        buf.write("\3\2\2\2KL\3\2\2\2LM\7=\2\2M\24\3\2\2\2NP\t\6\2\2ON\3")
        buf.write("\2\2\2PQ\3\2\2\2QO\3\2\2\2QR\3\2\2\2RS\3\2\2\2ST\b\13")
        buf.write("\2\2T\26\3\2\2\2\t\2\'-\63\65JQ\3\b\2\2")
        return buf.getvalue()


class XMLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    OPEN_TAG = 3
    CLOSE_TAG = 4
    EMPTY_TAG = 5
    TEXT = 6
    NAME = 7
    STRING = 8
    ENTITY = 9
    WS = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'/>'", "'='", "'<'", "'</'", "'<!'" ]

    symbolicNames = [ "<INVALID>",
            "OPEN_TAG", "CLOSE_TAG", "EMPTY_TAG", "TEXT", "NAME", "STRING", 
            "ENTITY", "WS" ]

    ruleNames = [ "T__0", "T__1", "OPEN_TAG", "CLOSE_TAG", "EMPTY_TAG", 
                  "TEXT", "NAME", "STRING", "ENTITY", "WS" ]

    grammarFileName = "XML.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


