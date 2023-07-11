from antlr4 import *
from Phase_1 import Phase_1
from Phase_2 import ASTConverter
from gen.XMLLexer import XMLLexer
from gen.XMLParser import XMLParser
from gen.XMLParserListener import ParseTreeWalker
from gen.CodeGenerator import CodeGenerator

def main():
    fileAddress = 'XmlExample.xml'#input("Input File Address : ")  # "XmlExample.xml"
    CheckButtonParseTrees = Phase_1().getCheckButtonsParseTrees(fileAddress)
    #phase 1
    a: XMLParser.ElementContext
    # for i in CheckButtonParseTrees:
    #     print(i.getText())

    #phase 2
    ast_list = []
    for tree in CheckButtonParseTrees:
        walker = ParseTreeWalker()
        listener = ASTConverter()
        walker.walk(t=tree, listener=listener)
        ast_list.append(listener)

    # for i in ast_list:
    #     i.printTree()
    #     print("\n")

    # phase 3
    res = []
    for a in ast_list:
        a.resultContent()

    for A in ast_list:
        res.append(A.result)

    code_generator = CodeGenerator('generated_code.py', res)
    code_generator.generate_code()

main()
