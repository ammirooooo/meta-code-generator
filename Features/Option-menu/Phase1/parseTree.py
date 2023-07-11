from antlr4 import *
from gen.XMLLexer import XMLLexer
from gen.XMLParser import XMLParser
from gen.XMLListener import XMLListener


class MyXMLListener(XMLListener):
    def __init__(self):
        self.ast = None
        self.current_node = None

    def enterOptionmenu(self, ctx):
        self.ast = {
            'type': 'Optionmenu',
            'text': ctx.text_.strip(),
            'children': []
        }
        self.current_node = self.ast

    def exitOptionmenu(self, ctx):
        self.current_node = None

    def enterOption(self, ctx):
        node = {
            'type': 'Option',
            'text': ctx.text_.strip(),
            'attributes': {
                'value': ctx.value_.strip(),
                'text': ctx.text_attr.strip()
            },
            'children': [None]
        }
        self.current_node['children'].append(node)
        self.current_node = node

    def exitOption(self, ctx):
        self.current_node = self.current_node['parent']

    def visitTerminal(self, node):
        if node.symbol.text == '</Option>':
            self.current_node = self.current_node['parent']

def main():
    xml_string = '<OptionMenu text="Select a color">\n    <Option value="red" text="Red">Option 1</Option>\n    <Option value="green" text="Green">Option 2</Option>\n    <Option value="blue" text="Blue">Option 3</Option>\n    <Option value="yellow" text="Yellow">Option 4</Option>\n</OptionMenu>'

    lexer = XMLLexer(InputStream(xml_string))

    stream = CommonTokenStream(lexer)

    parser = XMLParser(stream)

    tree = parser.optionmenu()

    printer = MyXMLListener()

    walker = ParseTreeWalker()

    walker.walk(printer, tree)

    print(printer.ast)
    

    

if __name__ == '__main__':
    main()
