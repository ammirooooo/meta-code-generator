# Generated from XML.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .XMLParser import XMLParser
else:
    from XMLParser import XMLParser

# This class defines a complete listener for a parse tree produced by XMLParser.
class XMLListener(ParseTreeListener):

    # Enter a parse tree produced by XMLParser#xml.
    def enterXml(self, ctx:XMLParser.XmlContext):
        pass

    # Exit a parse tree produced by XMLParser#xml.
    def exitXml(self, ctx:XMLParser.XmlContext):
        pass


    # Enter a parse tree produced by XMLParser#element.
    def enterElement(self, ctx:XMLParser.ElementContext):
        pass

    # Exit a parse tree produced by XMLParser#element.
    def exitElement(self, ctx:XMLParser.ElementContext):
        pass


    # Enter a parse tree produced by XMLParser#content.
    def enterContent(self, ctx:XMLParser.ContentContext):
        pass

    # Exit a parse tree produced by XMLParser#content.
    def exitContent(self, ctx:XMLParser.ContentContext):
        pass


    # Enter a parse tree produced by XMLParser#startTag.
    def enterStartTag(self, ctx:XMLParser.StartTagContext):
        pass

    # Exit a parse tree produced by XMLParser#startTag.
    def exitStartTag(self, ctx:XMLParser.StartTagContext):
        pass


    # Enter a parse tree produced by XMLParser#endTag.
    def enterEndTag(self, ctx:XMLParser.EndTagContext):
        pass

    # Exit a parse tree produced by XMLParser#endTag.
    def exitEndTag(self, ctx:XMLParser.EndTagContext):
        pass


    # Enter a parse tree produced by XMLParser#emptyTag.
    def enterEmptyTag(self, ctx:XMLParser.EmptyTagContext):
        pass

    # Exit a parse tree produced by XMLParser#emptyTag.
    def exitEmptyTag(self, ctx:XMLParser.EmptyTagContext):
        pass


    # Enter a parse tree produced by XMLParser#attribute.
    def enterAttribute(self, ctx:XMLParser.AttributeContext):
        pass

    # Exit a parse tree produced by XMLParser#attribute.
    def exitAttribute(self, ctx:XMLParser.AttributeContext):
        pass


