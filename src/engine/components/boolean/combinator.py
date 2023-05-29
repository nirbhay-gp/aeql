from src.engine.protocols import BooleanCombinator


class all_(BooleanCombinator):
    def __init__(self, *args):
        super().__init__('all', *args)
        
    @property
    def value(self):
        for operand in self.operands:
            if operand == False:
                return False


class any_(BooleanCombinator):
    
    def __init__(self, *args):
        super().__init__('any', *args)
    
    @property
    def value(self):
        for operand in self.operands:
            if operand == True:
                return True
        return False


__all__ = ("all_", "any_")
