class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.properties = []
        self.children = []
        self.parent = parent

    def toString(self):
        firstItemFlag = (self.index == 0)
        if not firstItemFlag:
            print("|__", self.name)

        for prop in self.properties:
            space = ''
            if not firstItemFlag:
                space = '      '

            print(space, "|__", '|' + prop.name + '|', "->", prop.value)

    # Accept method for Visitor pattern
    def accept(self, visitor):
        visitor.visitNode(self)
        for prop in self.properties:
            prop.accept(visitor)

    def add_child(self, node):
        self.children.append(node)

class PropertyModel:
    def __init__(self, name='', value=''):
        self.name = name
        self.value = value

    def accept(self, visitor):
        visitor.visitPropertyModel(self)

class Item:
    def __init__(self, id, content, openType=None):
        self.id = id
        self.content = content
        self.openType = openType
