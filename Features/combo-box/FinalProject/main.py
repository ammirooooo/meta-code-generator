from antlr4 import *
from gen.XMLLexer import XMLLexer
from gen.XMLParser import XMLParser
from AST_ParseTree import AST, XMLAttribute, XMLElement
from ParseTree import *
import argparse


def main(args):
    input_stream = FileStream(args.file, encoding='utf8')
    lexer = XMLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    pars = XMLParser(stream)
    tree = pars.document()

    ast = AST()
    walker = ParseTreeWalker()
    walker.walk(ast, tree)
    nodes = ast.nodes

    def get_xml_ast(root):
        node = root[0]
        name = node.Name()[0].getText()
        value = node.content().getText()
        return XMLElement(name, value, [get_xml_ast([child]) for child in node.content().children
                                        if isinstance(child, XMLParser.ElementContext)])

    def convert_xml_to_py_parse_tree(node):
        if node is None:
            return None
        elif node.tag == 'Text' or node.tag =='Scrollbar':
            return Function(identifier=Name(id="Text"),
                    args=Param(parameters=[convert_xml_to_py_parse_tree(child) for child in node.children])
                    )
        elif node.tag == 'root':
            value = node.value
            expr = Assign(target="root", value=value)
            return expr
        elif node.tag == 'bg':
            value = node.value
            expr = Assign(target='bg', value=value)
            return expr
        elif node.tag == 'bd':
            value = node.value
            expr = Assign(target='bd', value=value)
            return expr
        elif node.tag == 'fg':
            value = node.value
            expr = Assign(target='fg', value=value)
            return expr
        elif node.tag == 'height':
            value = node.value
            expr = Assign(target='height', value=value)
            return expr
        elif node.tag == 'width':
            value = node.value
            expr = Assign(target='width', value=value)
            return expr
        elif node.tag == 'font':
            value = node.value
            expr = Assign(target='font', value=value)
            return expr
        elif node.tag == 'command':
            value = node.value
            expr = Assign(target='command', value=value)
            return expr
        elif node.tag == 'cursor':
            value = node.value
            expr = Assign(target='cursor', value=value)
            return expr
        elif node.tag == 'Highlightbackground':
            value = node.value
            expr = Assign(target='Highlightbackground', value=value)
            return expr
        elif node.tag == 'highlighcolor':
            value = node.value
            expr = Assign(target='highlighcolor', value=value)
            return expr
        elif node.tag == 'orient':
            value = node.value
            expr = Assign(target='orient', value=value)
            return expr
        elif node.tag == 'jump':
            value = node.value
            expr = Assign(target='jump', value=value)
            return expr
        elif node.tag == 'repeatdelay':
            value = node.value
            expr = Assign(target='repeatdelay', value=value)
            return expr
        elif node.tag == 'repeatinterval':
            value = node.value
            expr = Assign(target='repeatinterval', value=value)
            return expr
        elif node.tag == 'takefocus':
            value = node.value
            expr = Assign(target='takefocus', value=value)
            return expr
        elif node.tag == 'troughcolor':
            value = node.value
            expr = Assign(target='troughcolor', value=value)
            return expr
        else:
            raise ValueError('Unknown node type: %s' % node.tag)
    ast_root = get_xml_ast(nodes)

    print("XML AST:")
    for ch in ast_root.children:
        print("   " + ch.tag + "   " + ch.value)

    p_tree = convert_xml_to_py_parse_tree(ast_root)

    def get_python_code(root):
        expr_list = []
        python_statement = ""
        identifier = root.identifier.id
        python_statement = python_statement+identifier+"("

        for param in root.args.parameters:
            expr = param.target+" = "+param.value
            expr_list.append(expr)

        for expr in expr_list:
            python_statement = python_statement+expr+", "
        python_statement = python_statement+")"
        print(python_statement)

    get_python_code(p_tree)


if __name__ == "__main__":
    inpfile = input("Enter File Name: ")
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-n', '--file',
        default=inpfile + "")
    args = parser.parse_args()
    main(args)