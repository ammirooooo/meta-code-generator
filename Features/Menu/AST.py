from PythonCodeGenerator import PythonCodeGenerator
from gen.XMLParserListener import XMLParserListener
from gen.XMLParser import XMLParser
from nodeModel import *

class AST( XMLParserListener):
    def __init__(self):
        self.AST = []
        self.root = ""
        self.currentElement = ""
        self.currentIndex = 0

    def enterElement(self, ctx: XMLParser.ElementContext):
        self.currentElement = str(ctx.Name()[0])
        if self.root == "":
            self.root = self.currentElement

        self.currentIndex = len(self.AST)
        node = Node(str(ctx.Name()[0]), self.currentIndex)
        self.AST.append(node)

    def enterAttribute(self, ctx: XMLParser.AttributeContext):
        prop = PropertyModel(ctx.Name().getText(), ctx.STRING().getText())
        parent = str(ctx.parentCtx.Name()[0])
        index = len(self.AST) - 1
        if parent == 'menu':
            index = 0
        self.AST[index].properties.append(prop)

    def enterContent(self, ctx: XMLParser.ContentContext):
        parent = str(ctx.parentCtx.Name()[0])
        if parent == 'menu':
            return
        prop = PropertyModel('content', str(ctx.getChild(0).getText()))
        index = len(self.AST) - 1
        self.AST[index].properties.append(prop)

    def getTree(self):
        print(self.root)
        print("|")
        for i in range(len(self.AST)):
            self.AST[i].toString()
            if i != len(self.AST) - 1:
                print("|")

    def to_python_code(self):
        if not self.AST:
            return ""

        python_code_generator = PythonCodeGenerator()
        python_code_generator.visit(self.AST[0])  # Starting from the root node
        return python_code_generator.python_code  # Use 'python_code' instead of 'get_python_code()'

