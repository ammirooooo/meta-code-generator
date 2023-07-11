from antlr4 import *
from gen.XMLLexer import XMLLexer
from gen.XMLParser import XMLParser
import argparse

class metric():

    def getParseTree(fileAddress):
        parser = argparse.ArgumentParser()
        parser.add_argument('-n', '--file', default=fileAddress)
        args = parser.parse_args()
        xmlFile = FileStream(args.file, encoding='utf8')
        lex = XMLLexer(xmlFile)
        token = CommonTokenStream(lex)
        parsedFile = XMLParser(token)
        return parsedFile.document()
