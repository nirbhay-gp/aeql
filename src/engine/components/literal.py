from src.engine.protocols import Literal


class bool_(Literal):
    def __init__(self, value):
        super().__init__("bool", value)


class int_(Literal):
    def __init__(self, value):
        super().__init__("int", value)


class float_(Literal):
    def __init__(self, value):
        super().__init__("float", value)


class str_(Literal):
    def __init__(self, value):
        super().__init__("str", value)
