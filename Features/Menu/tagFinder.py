from antlr4 import *
from gen.XMLLexer import XMLLexer
from gen.XMLParser import XMLParser
from gen.XMLParserListener import XMLParserListener

class TagFinder(XMLParserListener):
    def __init__(self):
        self.tag = []

    @property
    def getTag(self):
        return self.tag

    def enterElement(self, ctx: XMLParser.ElementContext):
        if ctx.children[1].getText() == "menu":
            self.tag.append(ctx)
