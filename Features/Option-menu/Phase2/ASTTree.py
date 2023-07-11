from antlr4 import *
from gen.XMLLexer import XMLLexer
from gen.XMLParser import XMLParser

class ASTGenerator(XMLParser):
    def __init__(self, stream):
        super().__init__(stream)
        self.ast = None

    def optionmenu(self):
        self.ast = self.visitOptionmenu(super().optionMenu())
        return self.ast

    def visitOptionmenu(self, ctx:XMLParser.OptionMenuContext):
        return {
            "type": "Optionmenu",
            "text": ctx.getText(),
            "children": [self.visitChild(c) for c in ctx.children if not isinstance(c, TerminalNode)]
        }

    def visitChild(self, ctx):
        if isinstance(ctx, XMLParser.OptionContext):
            return self.visitOption(ctx)
        elif isinstance(ctx, XMLParser.AttValue):
            return self.visitValue(ctx)

    def visitOption(self, ctx:XMLParser.OptionContext):
        return {
            "type": "Option",
            "text": ctx.getText(),
            "value": self.visitValue(ctx.value())
        }

    def visitValue(self, ctx:XMLParser.AttValue):
        return {
            "type": "Value",
            "text": ctx.getText()
        }

class DrawAST:
    def __init__(self, inputAddress):
        self.input = inputAddress

    def draw(self):
        with open(self.input, 'r') as file:
            file_stream = InputStream(file.read())
            lexer = XMLLexer(file_stream)
            stream = CommonTokenStream(lexer)
            parser = ASTGenerator(stream)
            tree = parser.optionmenu()
            print(tree)


if __name__ == '__main__':
    draw=DrawAST("./option-menu.xml")
    draw.draw()