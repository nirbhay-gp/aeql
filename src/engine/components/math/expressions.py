import math
from src.engine.protocols import MathExpression

class add_(MathExpression):
    
    @property
    def value(self):
        return self.left_operand + self.right_operand
    
class subtract_(MathExpression):
    
    @property
    def value(self):
        return self.left_operand - self.right_operand

class divide_(MathExpression):
    
    @property
    def value(self):
        return self.left_operand / self.right_operand    
    
class multiply_(MathExpression):
    
    @property
    def value(self):
        return self.left_operand * self.right_operand    
    
class exponent_(MathExpression):
    
    @property
    def value(self):
        return math.exp(self.left_operand, self.right_operand)
    
        