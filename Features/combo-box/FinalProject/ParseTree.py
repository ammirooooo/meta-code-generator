
class Name:
    def __init__(self, id):
        self.id = id


class Str:
    def __init__(self, string=""):
        self.string = string


class Param:
    def __init__(self, parameters=[]):
        self.parameters = parameters


class Assign:
    def __init__(self, target, value):
        self.target = target
        self.value = value


class Function:
    def __init__(self, identifier=None, args=None):
        self.identifier = identifier
        self.args = args
