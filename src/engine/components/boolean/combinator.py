from src.engine.protocols import BooleanCombinator

class all_(BooleanCombinator):
    
    @property
    def value(self):
        for operand in self.operands:
            if operand == False:
                return False
        
class any_(BooleanCombinator):
    
    @property
    def value(self):
        for operand in self.operands:
            if operand == True:
                return True
        return False
    
__all__ = ('all_', 'any_') 