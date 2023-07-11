import matplotlib.pyplot as plt
from antlr4.TokenStreamRewriter import TokenStreamRewriter
from antlr4.tree.Tree import TerminalNodeImpl

from gen.XMLParser import XMLParser
from gen.XMLLexer import XMLLexer
from gen.XMLParserListener import XMLParserListener
from gen.XMLParserVisitor import XMLParserVisitor
from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
import sys
import networkx as nx

ENTRY = 'entry'
ATTRIBUTES = 'attributes'
CONTENT = 'content'


class MyXMLVisitor(XMLParserVisitor):
    def __init__(self, graph: nx.DiGraph):
        self.graph = graph
        self.graph.add_edge(ENTRY, ATTRIBUTES)
        self.graph.add_edge(ENTRY, CONTENT)
        # self.data = {}

    def visitAttribute(self, ctx: XMLParser.AttributeContext):
        key = ctx.children[0].symbol.text
        value = ctx.children[2].symbol.text.replace("\"", "")
        self.graph.add_edge(ATTRIBUTES, key)
        self.graph.add_edge(key, value)
        # self.data[key] = value

    def visitContent(self, ctx: XMLParser.ContentContext):
        value = ctx.getText()
        if value == "":
            value = "' '"
        self.graph.add_edge(CONTENT, value)
        # self.data["value"] = f'"""{value}"""'


class codeGenerator:
    def __init__(self,graph: nx.DiGraph ):
        self.root_var = 'root'
        self.lib_alias = 'tk'
        self.data={}
        edges = graph.edges(data=True)
        for edge in edges:
            if edge[0] == 'content':
                self.data["value"] = f'"""{edge[1]}"""'
            elif edge[0]=='entry' or edge[0]=='attributes':
                continue
            else:
                self.data[edge[0]] = edge[1]
        print(self.data)
        self.template=f'''
        
import tkinter as {self.lib_alias}

{self.root_var} = {self.lib_alias}.Tk()
<code>
{self.root_var}.mainloop()
'''

    def generate_code(self):
        code = self.make_entries()
        return self.template.replace("<code>",code)

    def make_entries(self):
        args = ""
        val=""
        for (key, value) in self.data.items():
            if key == "name":
                continue
            if key == "value":
                val=value
                continue
            args += f",{key}={value}"
        code=f'''{self.data["name"]}={self.lib_alias}.Entry({self.root_var}{args})'''
        if val!="":
            code+=f'\n{self.data["name"]}.insert(0,{val})'
            code+=f'\n{self.data["name"]}.pack()'
        return code


def main(argv):
    code = ""
    with open(argv[1], 'r') as f:
        code = f.read()
    codeStream = InputStream(code)
    lexer = XMLLexer(codeStream)
    commonToken = CommonTokenStream(lexer)
    parser = XMLParser(commonToken)
    tree = parser.entry()
    graph = nx.DiGraph()
    myVisitor = MyXMLVisitor(graph)
    myVisitor.visit(tree)
    code_gen=codeGenerator(graph)

    # print(myVisitor.data)

    result=code_gen.generate_code()
    with open("./output.py", "w") as f:
        f.write(result)
    graph = nx.dfs_tree(graph, ENTRY)
    pos = nx.nx_pydot.graphviz_layout(graph, prog="dot")
    nx.draw(graph, pos, with_labels=True, node_size=1500, node_color="skyblue", font_color="black")
    plt.show()
if __name__ == '__main__':
    main(["", "./test.xml"])
    # main(sys.argv)
