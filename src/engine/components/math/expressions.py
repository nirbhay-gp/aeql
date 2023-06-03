import math
from src.engine.protocols import MathExpression


class add_(MathExpression):
    
    def __init__(self, *args):
        super().__init__('add', *args)
    
    @property
    def value(self):
        return self.left_operand + self.right_operand


class subtract_(MathExpression):
    
    def __init__(self, *args):
        super().__init__('subtract', *args)
    
    @property
    def value(self):
        return self.left_operand - self.right_operand


class divide_(MathExpression):
    
    def __init__(self, *args):
        super().__init__('divide', *args)
    
    @property
    def value(self):
        return self.left_operand / self.right_operand


class multiply_(MathExpression):
    
    def __init__(self, *args):
        super().__init__('multiply', *args)
        
    @property
    def value(self):
        return self.left_operand * self.right_operand


class exponent_(MathExpression):
    
    def __init__(self, *args):
        super().__init__('exponent', *args)
        
    @property
    def value(self):
        return math.exp(self.left_operand, self.right_operand)
