from antlr4 import *
from metric import *
from tagFinder import TagFinder
from AST import AST
from nodeModel import *  # Import the Node and PropertyModel classes
from PythonCodeGenerator import PythonCodeGenerator

# PythonCodeGenerator class definition here...

def main():
    # 1. Create an instance of the AST class
    ast = AST()

    # 2. Create parseTree using the getParseTree function from the metric class
    parseTree = metric.getParseTree('input.xml')

    # 3. Process parseTree using the TagFinder class to get the list of tags
    listener = TagFinder()
    walker = ParseTreeWalker()
    walker.walk(t=parseTree, listener=listener)

    tagParseTree = listener.getTag

    # 4. Create AST from each tag using the AST class
    for parseTree in tagParseTree:
        astListener = AST()
        walker.walk(t=parseTree, listener=astListener)
        ast = astListener
        # 5. Generate Python code from each AST using the PythonCodeGenerator class
        python_code = ""
        instance_creations = []

        for i, parseTree in enumerate(tagParseTree):
            astListener = AST()
            walker.walk(t=parseTree, listener=astListener)
            ast = astListener

            # Generate Python code for the current menu node
            python_code = ast.to_python_code()

            # Get the class name (menu)
            class_name = "menu"

            # Create instance and append to the list of instance creations
            instance_name = f"{class_name}{i + 1}"
            instance_creation = f"{instance_name} = {class_name}({', '.join(prop.value for prop in ast.AST[0].properties)})"
            instance_creations.append(instance_creation)

        # Write the output to the Generated_code.py file
        with open("Generated_code.py", "w") as file:
            file.write(python_code)
            file.write("\n".join(instance_creations))

    print('Python Code Generated !!!')

if __name__ == '__main__':
    main()
