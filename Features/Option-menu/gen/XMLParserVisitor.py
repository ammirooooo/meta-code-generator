# Generated from //wsl$/Ubuntu-22.04/home/mohammadali/University/Compiler/project/option-menu/Phase1\XMLParser.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .XMLParser import XMLParser
else:
    from XMLParser import XMLParser

# This class defines a complete generic visitor for a parse tree produced by XMLParser.

class XMLParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by XMLParser#optionmenu.
    def visitOptionmenu(self, ctx:XMLParser.OptionmenuContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#prolog.
    def visitProlog(self, ctx:XMLParser.PrologContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#content.
    def visitContent(self, ctx:XMLParser.ContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#element.
    def visitElement(self, ctx:XMLParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#reference.
    def visitReference(self, ctx:XMLParser.ReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#attribute.
    def visitAttribute(self, ctx:XMLParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#chardata.
    def visitChardata(self, ctx:XMLParser.ChardataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#misc.
    def visitMisc(self, ctx:XMLParser.MiscContext):
        return self.visitChildren(ctx)



del XMLParser