from antlr4 import *

from gen.XMLLexer import XMLLexer
from gen.XMLParser import XMLParser
from gen.XMLParserListener import XMLParserListener
import argparse


class CheckButtonGetter(XMLParserListener):
    def __init__(self):
        self.checkButtons = []

    @property
    def get_check_buttons(self):
        return self.checkButtons

    def enterElement(self, ctx: XMLParser.ElementContext):
        if ctx.children[1].getText() == "checkbutton":
            self.checkButtons.append(ctx)


class Phase_1:
    def __init__(self):
        pass

    @staticmethod
    def getParseTree(parseArgs):
        cppFile = FileStream(parseArgs.file, encoding='utf8')
        lex = XMLLexer(cppFile)
        token = CommonTokenStream(lex)
        parsedFile = XMLParser(token)
        return parsedFile.document()

    def getCheckButtonsParseTrees(self, fileAddress):
        parser = argparse.ArgumentParser()
        parser.add_argument('-n', '--file', default=fileAddress)
        args = parser.parse_args()
        parseTree = self.getParseTree(args)

        listener = CheckButtonGetter()
        ParseTreeWalker().walk(t=parseTree, listener=listener)

        return listener.get_check_buttons
