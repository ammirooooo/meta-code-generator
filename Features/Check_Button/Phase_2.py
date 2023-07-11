from gen.XMLParserListener import XMLParserListener
from gen.XMLParser import XMLParser


class Node():
    def __init__(self):
        self.attr = ""
        self.val = ""


class ASTConverter(XMLParserListener):
    def __init__(self):
        self.AST = []
        self.root = ""
        self.result = []

    def enterElement(self, ctx: XMLParser.ElementContext):
        self.root = str(ctx.Name()[0])

    def enterAttribute(self, ctx: XMLParser.AttributeContext):
        node = Node()
        node.attr = str(ctx.Name())
        node.val = str(ctx.STRING())
        self.AST.append(node)

    def enterContent(self, ctx:XMLParser.ContentContext):
        node = Node()
        node.attr = str('content')
        node.val = str(ctx.getChild(0).TEXT())
        self.AST.append(node)

    def printTree(self):
        print(self.root)
        print("|")
        for i in range(len(self.AST)):
            print("|_____",
                  self.AST[i].attr, "--->", self.AST[i].val)
            if i != len(self.AST) - 1:
                print("|")

    def resultContent(self):
        for i in range(len(self.AST)):
            if(self.AST[i].attr == "name"):
                self.AST[i].attr = "variable"
            if(self.AST[i].attr == "content"):
                self.AST[i].attr = "text"
            self.result.append((self.AST[i].attr, self.AST[i].val))
