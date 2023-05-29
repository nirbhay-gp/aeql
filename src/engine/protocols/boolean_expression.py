from typing import List, Union
from abc import ABCMeta, abstractmethod, abstractproperty


class BooleanExpression(metaclass=ABCMeta):
    def __init__(self, operator, *args):
        self.__operator = operator
        self.__parameters = args

    @property
    def left_operand(self):
        return self.__parameters[0].value

    @property
    def right_operand(self):
        self.__parameters[0].value

    @abstractproperty
    def value(self):
        pass


class BooleanCombinator(metaclass=ABCMeta):
    def __init__(self, combinator, *args):
        self.__combinator = combinator
        self.__parameters = args

    @property
    def operands(self):
        for operand in self.__parameters:
            yield operand.value

    @abstractproperty
    def value(self):
        pass
