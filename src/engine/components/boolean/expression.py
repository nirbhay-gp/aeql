from src.engine.protocols import BooleanExpression

class eq_(BooleanExpression):
    
    @property    
    def value(self):
        return self.left_operand == self.right_operand

class gt_(BooleanExpression):
    
    @property    
    def value(self):
        return self.left_operand > self.right_operand
    
class lt_(BooleanExpression):
    
    @property    
    def value(self):
        return self.left_operand < self.right_operand
    
class gte_(BooleanExpression):
    
    @property        
    def value(self):
        return self.left_operand >= self.right_operand
    
class lte_(BooleanExpression):
    
    @property        
    def value(self):
        return self.left_operand <= self.right_operand

class not_(BooleanExpression):
    
    @property        
    def value(self):
        return not self.left_operand
    

__all__ = ('eq_', 'gt_', 'gte_', 'lt_', 'lte_', 'not_')