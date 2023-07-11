from nodeModel import Node, PropertyModel

class PythonCodeGenerator:
    def __init__(self):
        self.python_code = ""

    def visit(self, node):
        if isinstance(node, Node):
            self.visit_node(node)
        elif isinstance(node, PropertyModel):
            self.visit_property(node)

    def visit_node(self, node):
        self.python_code += f"class {node.name}:\n"
        self.python_code += f"    def __init__(self, {', '.join(prop.name for prop in node.properties)}):\n"
        for prop in node.properties:
            self.python_code += f"        self.{prop.name} = {prop.name}\n"
        self.python_code += "\n"

    def visit_property(self, prop):
        self.python_code += f"        self.{prop.name} = {prop.name}\n"

    def get_python_code(self):
        return self.python_code

