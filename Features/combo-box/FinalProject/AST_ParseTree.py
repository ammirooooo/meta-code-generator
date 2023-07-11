from antlr4 import *
from gen.XMLLexer import XMLLexer
from gen.XMLParser import XMLParser
from gen.XMLParserListener import XMLParserListener


class XMLNode:
    def __init__(self, value=None, children=[]):
        self.value = value
        self.children = children


class XMLElement(XMLNode):
    def __init__(self, tag, value=None, children=[]):
        super().__init__(value, children)
        self.tag = tag


class XMLAttribute():
    def __init__(self, value):
        self.value = value


class AST(XMLParserListener):
    def __init__(self):
        self.nodes = []

    def enterElement(self, ctx: XMLParser.ElementContext):
        self.nodes.append(ctx)

    def enterAttribute(self, ctx: XMLParser.AttributeContext):
        name = ctx.Name().getText()
        value = ctx.STRING().getText()[1:-1]

