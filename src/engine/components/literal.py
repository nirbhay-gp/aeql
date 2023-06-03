import functools
from src.engine.protocols import Literal


class bool_(Literal):
    def __init__(self, value):
        super().__init__("bool", value)

    @functools.cached_property
    def value(self):
        value = super().value
        if value == "true":
            return True
        elif value == "false":
            return False


class int_(Literal):
    def __init__(self, value):
        super().__init__("int", value)

    @functools.cached_property
    def value(self):
        value = super().value
        return int(value)


class float_(Literal):
    def __init__(self, value):
        super().__init__("float", value)

    @functools.cached_property
    def value(self):
        value = super().value
        return float(value)


class str_(Literal):
    def __init__(self, value):
        super().__init__("str", value)
