# ast_listener.py
from gen.XMLParser import XMLParser
from gen.XMLParserListener import XMLParserListener
from nodeModel import Node, PropertyModel

class XMLListenerToAst(XMLParserListener):
    def __init__(self):
        super().__init__()
        self.ast_list = []
        self.current_node = None


    def enterElement(self, ctx: XMLParser.ElementContext):
        node_name = ctx.Name(0).getText()
        node = Node(node_name)
        if self.current_node is not None:
            node.parent = self.current_node
        self.current_node = node
        self.ast_list.append(node)

    def exitElement(self, ctx: XMLParser.ElementContext):
        self.current_node = self.current_node.parent

    def visitTerminal(self, node):
        text = node.getText().strip()
        if text:
            prop = PropertyModel(node.getSymbol().type, text)
            self.current_node.properties.append(prop)

    def getASTList(self):
        return self.ast_list