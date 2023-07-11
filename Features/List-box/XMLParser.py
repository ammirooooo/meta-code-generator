# Generated from XML.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("A\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3\30\n\3\3\4\3\4\5")
        buf.write("\4\34\n\4\3\5\3\5\7\5 \n\5\f\5\16\5#\13\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\7\7-\n\7\f\7\16\7\60\13\7\3\7\5\7")
        buf.write("\63\n\7\3\7\3\7\3\b\3\b\5\b9\n\b\3\b\3\b\5\b=\n\b\3\b")
        buf.write("\3\b\3\b\2\2\t\2\4\6\b\n\f\16\2\2\2@\2\20\3\2\2\2\4\27")
        buf.write("\3\2\2\2\6\33\3\2\2\2\b\35\3\2\2\2\n&\3\2\2\2\f*\3\2\2")
        buf.write("\2\16\66\3\2\2\2\20\21\5\4\3\2\21\3\3\2\2\2\22\23\5\b")
        buf.write("\5\2\23\24\5\6\4\2\24\25\5\n\6\2\25\30\3\2\2\2\26\30\5")
        buf.write("\f\7\2\27\22\3\2\2\2\27\26\3\2\2\2\30\5\3\2\2\2\31\34")
        buf.write("\5\4\3\2\32\34\7\b\2\2\33\31\3\2\2\2\33\32\3\2\2\2\34")
        buf.write("\7\3\2\2\2\35!\7\5\2\2\36 \5\16\b\2\37\36\3\2\2\2 #\3")
        buf.write("\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"$\3\2\2\2#!\3\2\2\2$%\7")
        buf.write("\6\2\2%\t\3\2\2\2&\'\7\6\2\2\'(\7\t\2\2()\7\6\2\2)\13")
        buf.write("\3\2\2\2*.\7\5\2\2+-\5\16\b\2,+\3\2\2\2-\60\3\2\2\2.,")
        buf.write("\3\2\2\2./\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\61\63\7\f\2")
        buf.write("\2\62\61\3\2\2\2\62\63\3\2\2\2\63\64\3\2\2\2\64\65\7\3")
        buf.write("\2\2\65\r\3\2\2\2\668\7\t\2\2\679\7\f\2\28\67\3\2\2\2")
        buf.write("89\3\2\2\29:\3\2\2\2:<\7\4\2\2;=\7\f\2\2<;\3\2\2\2<=\3")
        buf.write("\2\2\2=>\3\2\2\2>?\7\n\2\2?\17\3\2\2\2\t\27\33!.\628<")
        return buf.getvalue()


class XMLParser ( Parser ):

    grammarFileName = "XML.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'/>'", "'='", "'<'", "'</'", "'<!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "OPEN_TAG", 
                      "CLOSE_TAG", "EMPTY_TAG", "TEXT", "NAME", "STRING", 
                      "ENTITY", "WS" ]

    RULE_xml = 0
    RULE_element = 1
    RULE_content = 2
    RULE_startTag = 3
    RULE_endTag = 4
    RULE_emptyTag = 5
    RULE_attribute = 6

    ruleNames =  [ "xml", "element", "content", "startTag", "endTag", "emptyTag", 
                   "attribute" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    OPEN_TAG=3
    CLOSE_TAG=4
    EMPTY_TAG=5
    TEXT=6
    NAME=7
    STRING=8
    ENTITY=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class XmlContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self):
            return self.getTypedRuleContext(XMLParser.ElementContext,0)


        def getRuleIndex(self):
            return XMLParser.RULE_xml

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXml" ):
                listener.enterXml(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXml" ):
                listener.exitXml(self)




    def xml(self):

        localctx = XMLParser.XmlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_xml)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.element()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def startTag(self):
            return self.getTypedRuleContext(XMLParser.StartTagContext,0)


        def content(self):
            return self.getTypedRuleContext(XMLParser.ContentContext,0)


        def endTag(self):
            return self.getTypedRuleContext(XMLParser.EndTagContext,0)


        def emptyTag(self):
            return self.getTypedRuleContext(XMLParser.EmptyTagContext,0)


        def getRuleIndex(self):
            return XMLParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)




    def element(self):

        localctx = XMLParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_element)
        try:
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.startTag()
                self.state = 17
                self.content()
                self.state = 18
                self.endTag()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.emptyTag()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self):
            return self.getTypedRuleContext(XMLParser.ElementContext,0)


        def TEXT(self):
            return self.getToken(XMLParser.TEXT, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContent" ):
                listener.enterContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContent" ):
                listener.exitContent(self)




    def content(self):

        localctx = XMLParser.ContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_content)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [XMLParser.OPEN_TAG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.element()
                pass
            elif token in [XMLParser.TEXT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.match(XMLParser.TEXT)
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


    class StartTagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_TAG(self):
            return self.getToken(XMLParser.OPEN_TAG, 0)

        def CLOSE_TAG(self):
            return self.getToken(XMLParser.CLOSE_TAG, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XMLParser.AttributeContext,i)


        def getRuleIndex(self):
            return XMLParser.RULE_startTag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStartTag" ):
                listener.enterStartTag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStartTag" ):
                listener.exitStartTag(self)




    def startTag(self):

        localctx = XMLParser.StartTagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_startTag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(XMLParser.OPEN_TAG)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==XMLParser.NAME:
                self.state = 28
                self.attribute()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
            self.match(XMLParser.CLOSE_TAG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndTagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLOSE_TAG(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CLOSE_TAG)
            else:
                return self.getToken(XMLParser.CLOSE_TAG, i)

        def NAME(self):
            return self.getToken(XMLParser.NAME, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_endTag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndTag" ):
                listener.enterEndTag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndTag" ):
                listener.exitEndTag(self)




    def endTag(self):

        localctx = XMLParser.EndTagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_endTag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(XMLParser.CLOSE_TAG)
            self.state = 37
            self.match(XMLParser.NAME)
            self.state = 38
            self.match(XMLParser.CLOSE_TAG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmptyTagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_TAG(self):
            return self.getToken(XMLParser.OPEN_TAG, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XMLParser.AttributeContext,i)


        def WS(self):
            return self.getToken(XMLParser.WS, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_emptyTag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyTag" ):
                listener.enterEmptyTag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyTag" ):
                listener.exitEmptyTag(self)




    def emptyTag(self):

        localctx = XMLParser.EmptyTagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_emptyTag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(XMLParser.OPEN_TAG)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==XMLParser.NAME:
                self.state = 41
                self.attribute()
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==XMLParser.WS:
                self.state = 47
                self.match(XMLParser.WS)


            self.state = 50
            self.match(XMLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(XMLParser.NAME, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.WS)
            else:
                return self.getToken(XMLParser.WS, i)

        def getRuleIndex(self):
            return XMLParser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)




    def attribute(self):

        localctx = XMLParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(XMLParser.NAME)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==XMLParser.WS:
                self.state = 53
                self.match(XMLParser.WS)


            self.state = 56
            self.match(XMLParser.T__1)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==XMLParser.WS:
                self.state = 57
                self.match(XMLParser.WS)


            self.state = 60
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





