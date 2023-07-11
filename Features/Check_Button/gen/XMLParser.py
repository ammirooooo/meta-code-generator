# Generated from E:/Compiler/Check_Button\XMLParser.g4 by ANTLR 4.11.1
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
        4,1,19,129,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,3,0,20,8,0,1,0,5,0,23,8,0,10,0,12,0,26,9,0,
        1,0,1,0,3,0,30,8,0,1,0,5,0,33,8,0,10,0,12,0,36,9,0,1,0,1,0,1,1,1,
        1,1,1,5,1,43,8,1,10,1,12,1,46,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,5,1,58,8,1,10,1,12,1,61,9,1,1,1,3,1,64,8,1,1,2,1,2,5,2,
        68,8,2,10,2,12,2,71,9,2,1,2,1,2,1,3,3,3,76,8,3,1,3,1,3,1,3,1,3,1,
        3,3,3,83,8,3,1,3,3,3,86,8,3,5,3,88,8,3,10,3,12,3,91,9,3,1,4,1,4,
        1,4,5,4,96,8,4,10,4,12,4,99,9,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,5,4,111,8,4,10,4,12,4,114,9,4,1,4,3,4,117,8,4,1,5,1,5,1,
        6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,
        3,1,0,5,6,2,0,7,7,10,10,3,0,2,2,7,7,19,19,137,0,19,1,0,0,0,2,63,
        1,0,0,0,4,65,1,0,0,0,6,75,1,0,0,0,8,116,1,0,0,0,10,118,1,0,0,0,12,
        120,1,0,0,0,14,124,1,0,0,0,16,126,1,0,0,0,18,20,3,4,2,0,19,18,1,
        0,0,0,19,20,1,0,0,0,20,24,1,0,0,0,21,23,3,16,8,0,22,21,1,0,0,0,23,
        26,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,29,1,0,0,0,26,24,1,0,0,
        0,27,30,3,2,1,0,28,30,3,8,4,0,29,27,1,0,0,0,29,28,1,0,0,0,30,34,
        1,0,0,0,31,33,3,16,8,0,32,31,1,0,0,0,33,36,1,0,0,0,34,32,1,0,0,0,
        34,35,1,0,0,0,35,37,1,0,0,0,36,34,1,0,0,0,37,38,5,0,0,1,38,1,1,0,
        0,0,39,40,5,8,0,0,40,44,5,1,0,0,41,43,3,12,6,0,42,41,1,0,0,0,43,
        46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,47,1,0,0,0,46,44,1,0,0,
        0,47,48,5,11,0,0,48,49,3,6,3,0,49,50,5,8,0,0,50,51,5,14,0,0,51,52,
        5,1,0,0,52,53,5,11,0,0,53,64,1,0,0,0,54,55,5,8,0,0,55,59,5,1,0,0,
        56,58,3,12,6,0,57,56,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,
        0,0,0,60,62,1,0,0,0,61,59,1,0,0,0,62,64,5,13,0,0,63,39,1,0,0,0,63,
        54,1,0,0,0,64,3,1,0,0,0,65,69,5,9,0,0,66,68,3,12,6,0,67,66,1,0,0,
        0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,72,1,0,0,0,71,69,
        1,0,0,0,72,73,5,12,0,0,73,5,1,0,0,0,74,76,3,14,7,0,75,74,1,0,0,0,
        75,76,1,0,0,0,76,89,1,0,0,0,77,83,3,8,4,0,78,83,3,10,5,0,79,83,5,
        3,0,0,80,83,5,19,0,0,81,83,5,2,0,0,82,77,1,0,0,0,82,78,1,0,0,0,82,
        79,1,0,0,0,82,80,1,0,0,0,82,81,1,0,0,0,83,85,1,0,0,0,84,86,3,14,
        7,0,85,84,1,0,0,0,85,86,1,0,0,0,86,88,1,0,0,0,87,82,1,0,0,0,88,91,
        1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,7,1,0,0,0,91,89,1,0,0,0,92,
        93,5,8,0,0,93,97,5,17,0,0,94,96,3,12,6,0,95,94,1,0,0,0,96,99,1,0,
        0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,100,1,0,0,0,99,97,1,0,0,0,100,
        101,5,11,0,0,101,102,3,6,3,0,102,103,5,8,0,0,103,104,5,14,0,0,104,
        105,5,17,0,0,105,106,5,11,0,0,106,117,1,0,0,0,107,108,5,8,0,0,108,
        112,5,17,0,0,109,111,3,12,6,0,110,109,1,0,0,0,111,114,1,0,0,0,112,
        110,1,0,0,0,112,113,1,0,0,0,113,115,1,0,0,0,114,112,1,0,0,0,115,
        117,5,13,0,0,116,92,1,0,0,0,116,107,1,0,0,0,117,9,1,0,0,0,118,119,
        7,0,0,0,119,11,1,0,0,0,120,121,5,17,0,0,121,122,5,15,0,0,122,123,
        5,16,0,0,123,13,1,0,0,0,124,125,7,1,0,0,125,15,1,0,0,0,126,127,7,
        2,0,0,127,17,1,0,0,0,15,19,24,29,34,44,59,63,69,75,82,85,89,97,112,
        116
    ]

class XMLParser ( Parser ):

    grammarFileName = "XMLParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'checkbutton'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'<'", "<INVALID>", "<INVALID>", "'>'", "<INVALID>", 
                     "'/>'", "'/'", "'='" ]

    symbolicNames = [ "<INVALID>", "CheckButtonTag", "COMMENT", "CDATA", 
                      "DTD", "EntityRef", "CharRef", "SEA_WS", "OPEN", "XMLDeclOpen", 
                      "TEXT", "CLOSE", "SPECIAL_CLOSE", "SLASH_CLOSE", "SLASH", 
                      "EQUALS", "STRING", "Name", "S", "PI" ]

    RULE_document = 0
    RULE_checkButton = 1
    RULE_prolog = 2
    RULE_content = 3
    RULE_element = 4
    RULE_reference = 5
    RULE_attribute = 6
    RULE_chardata = 7
    RULE_misc = 8

    ruleNames =  [ "document", "checkButton", "prolog", "content", "element", 
                   "reference", "attribute", "chardata", "misc" ]

    EOF = Token.EOF
    CheckButtonTag=1
    COMMENT=2
    CDATA=3
    DTD=4
    EntityRef=5
    CharRef=6
    SEA_WS=7
    OPEN=8
    XMLDeclOpen=9
    TEXT=10
    CLOSE=11
    SPECIAL_CLOSE=12
    SLASH_CLOSE=13
    SLASH=14
    EQUALS=15
    STRING=16
    Name=17
    S=18
    PI=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DocumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(XMLParser.EOF, 0)

        def checkButton(self):
            return self.getTypedRuleContext(XMLParser.CheckButtonContext,0)


        def element(self):
            return self.getTypedRuleContext(XMLParser.ElementContext,0)


        def prolog(self):
            return self.getTypedRuleContext(XMLParser.PrologContext,0)


        def misc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.MiscContext)
            else:
                return self.getTypedRuleContext(XMLParser.MiscContext,i)


        def getRuleIndex(self):
            return XMLParser.RULE_document

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDocument" ):
                listener.enterDocument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDocument" ):
                listener.exitDocument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDocument" ):
                return visitor.visitDocument(self)
            else:
                return visitor.visitChildren(self)




    def document(self):

        localctx = XMLParser.DocumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_document)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 18
                self.prolog()


            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 524420) != 0:
                self.state = 21
                self.misc()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 27
                self.checkButton()
                pass

            elif la_ == 2:
                self.state = 28
                self.element()
                pass


            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 524420) != 0:
                self.state = 31
                self.misc()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 37
            self.match(XMLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CheckButtonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.OPEN)
            else:
                return self.getToken(XMLParser.OPEN, i)

        def CheckButtonTag(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CheckButtonTag)
            else:
                return self.getToken(XMLParser.CheckButtonTag, i)

        def CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CLOSE)
            else:
                return self.getToken(XMLParser.CLOSE, i)

        def content(self):
            return self.getTypedRuleContext(XMLParser.ContentContext,0)


        def SLASH(self):
            return self.getToken(XMLParser.SLASH, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XMLParser.AttributeContext,i)


        def SLASH_CLOSE(self):
            return self.getToken(XMLParser.SLASH_CLOSE, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_checkButton

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCheckButton" ):
                listener.enterCheckButton(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCheckButton" ):
                listener.exitCheckButton(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCheckButton" ):
                return visitor.visitCheckButton(self)
            else:
                return visitor.visitChildren(self)




    def checkButton(self):

        localctx = XMLParser.CheckButtonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_checkButton)
        self._la = 0 # Token type
        try:
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(XMLParser.OPEN)
                self.state = 40
                self.match(XMLParser.CheckButtonTag)
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==17:
                    self.state = 41
                    self.attribute()
                    self.state = 46
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 47
                self.match(XMLParser.CLOSE)
                self.state = 48
                self.content()
                self.state = 49
                self.match(XMLParser.OPEN)
                self.state = 50
                self.match(XMLParser.SLASH)
                self.state = 51
                self.match(XMLParser.CheckButtonTag)
                self.state = 52
                self.match(XMLParser.CLOSE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.match(XMLParser.OPEN)
                self.state = 55
                self.match(XMLParser.CheckButtonTag)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==17:
                    self.state = 56
                    self.attribute()
                    self.state = 61
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 62
                self.match(XMLParser.SLASH_CLOSE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrologContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def XMLDeclOpen(self):
            return self.getToken(XMLParser.XMLDeclOpen, 0)

        def SPECIAL_CLOSE(self):
            return self.getToken(XMLParser.SPECIAL_CLOSE, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XMLParser.AttributeContext,i)


        def getRuleIndex(self):
            return XMLParser.RULE_prolog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProlog" ):
                listener.enterProlog(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProlog" ):
                listener.exitProlog(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProlog" ):
                return visitor.visitProlog(self)
            else:
                return visitor.visitChildren(self)




    def prolog(self):

        localctx = XMLParser.PrologContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_prolog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(XMLParser.XMLDeclOpen)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 66
                self.attribute()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.match(XMLParser.SPECIAL_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def chardata(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.ChardataContext)
            else:
                return self.getTypedRuleContext(XMLParser.ChardataContext,i)


        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.ElementContext)
            else:
                return self.getTypedRuleContext(XMLParser.ElementContext,i)


        def reference(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.ReferenceContext)
            else:
                return self.getTypedRuleContext(XMLParser.ReferenceContext,i)


        def CDATA(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CDATA)
            else:
                return self.getToken(XMLParser.CDATA, i)

        def PI(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.PI)
            else:
                return self.getToken(XMLParser.PI, i)

        def COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.COMMENT)
            else:
                return self.getToken(XMLParser.COMMENT, i)

        def getRuleIndex(self):
            return XMLParser.RULE_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContent" ):
                listener.enterContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContent" ):
                listener.exitContent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContent" ):
                return visitor.visitContent(self)
            else:
                return visitor.visitChildren(self)




    def content(self):

        localctx = XMLParser.ContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7 or _la==10:
                self.state = 74
                self.chardata()


            self.state = 89
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 82
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [8]:
                        self.state = 77
                        self.element()
                        pass
                    elif token in [5, 6]:
                        self.state = 78
                        self.reference()
                        pass
                    elif token in [3]:
                        self.state = 79
                        self.match(XMLParser.CDATA)
                        pass
                    elif token in [19]:
                        self.state = 80
                        self.match(XMLParser.PI)
                        pass
                    elif token in [2]:
                        self.state = 81
                        self.match(XMLParser.COMMENT)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 85
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==7 or _la==10:
                        self.state = 84
                        self.chardata()

             
                self.state = 91
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.OPEN)
            else:
                return self.getToken(XMLParser.OPEN, i)

        def Name(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.Name)
            else:
                return self.getToken(XMLParser.Name, i)

        def CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CLOSE)
            else:
                return self.getToken(XMLParser.CLOSE, i)

        def content(self):
            return self.getTypedRuleContext(XMLParser.ContentContext,0)


        def SLASH(self):
            return self.getToken(XMLParser.SLASH, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XMLParser.AttributeContext,i)


        def SLASH_CLOSE(self):
            return self.getToken(XMLParser.SLASH_CLOSE, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = XMLParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_element)
        self._la = 0 # Token type
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.match(XMLParser.OPEN)
                self.state = 93
                self.match(XMLParser.Name)
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==17:
                    self.state = 94
                    self.attribute()
                    self.state = 99
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 100
                self.match(XMLParser.CLOSE)
                self.state = 101
                self.content()
                self.state = 102
                self.match(XMLParser.OPEN)
                self.state = 103
                self.match(XMLParser.SLASH)
                self.state = 104
                self.match(XMLParser.Name)
                self.state = 105
                self.match(XMLParser.CLOSE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.match(XMLParser.OPEN)
                self.state = 108
                self.match(XMLParser.Name)
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==17:
                    self.state = 109
                    self.attribute()
                    self.state = 114
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 115
                self.match(XMLParser.SLASH_CLOSE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReferenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EntityRef(self):
            return self.getToken(XMLParser.EntityRef, 0)

        def CharRef(self):
            return self.getToken(XMLParser.CharRef, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReference" ):
                listener.enterReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReference" ):
                listener.exitReference(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReference" ):
                return visitor.visitReference(self)
            else:
                return visitor.visitChildren(self)




    def reference(self):

        localctx = XMLParser.ReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_reference)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            _la = self._input.LA(1)
            if not(_la==5 or _la==6):
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


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Name(self):
            return self.getToken(XMLParser.Name, 0)

        def EQUALS(self):
            return self.getToken(XMLParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = XMLParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(XMLParser.Name)
            self.state = 121
            self.match(XMLParser.EQUALS)
            self.state = 122
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChardataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(XMLParser.TEXT, 0)

        def SEA_WS(self):
            return self.getToken(XMLParser.SEA_WS, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_chardata

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChardata" ):
                listener.enterChardata(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChardata" ):
                listener.exitChardata(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChardata" ):
                return visitor.visitChardata(self)
            else:
                return visitor.visitChildren(self)




    def chardata(self):

        localctx = XMLParser.ChardataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_chardata)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            _la = self._input.LA(1)
            if not(_la==7 or _la==10):
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


    class MiscContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(XMLParser.COMMENT, 0)

        def PI(self):
            return self.getToken(XMLParser.PI, 0)

        def SEA_WS(self):
            return self.getToken(XMLParser.SEA_WS, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_misc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMisc" ):
                listener.enterMisc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMisc" ):
                listener.exitMisc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMisc" ):
                return visitor.visitMisc(self)
            else:
                return visitor.visitChildren(self)




    def misc(self):

        localctx = XMLParser.MiscContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_misc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 524420) != 0):
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





