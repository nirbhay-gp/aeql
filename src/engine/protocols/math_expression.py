from abc import ABCMeta, abstractmethod, abstractproperty


class MathExpression(metaclass=ABCMeta):
    
    def __init__(self, operator, *args):
        self.operator = operator
        self.parameters = args
    
    @property
    def left_operand(self):
        return self.parameters[0].value
    
    @property
    def right_operand(self):
        return self.parameters[0].value
    
    @abstractproperty
    def value(self):
        pass
