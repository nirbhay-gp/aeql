from abc import ABCMeta, abstractmethod, abstractproperty


class MathExpression(metaclass=ABCMeta):
    def __init__(self, operator, *args):
        self.__operator = operator
        self.__parameters = args

    @property
    def left_operand(self):
        return self.__parameters[0].value

    @property
    def right_operand(self):
        return self.__parameters[1].value

    @property
    def type(self):
        return self.__operator
    
    @abstractproperty
    def value(self):
        pass
