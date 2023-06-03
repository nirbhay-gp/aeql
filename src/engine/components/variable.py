from src.engine.protocols import Variable

class data_(Variable):
    
    def __init__(self, name: str):
        super().__init__('var', name)
    
    @property
    def value(self):
        return self.__registry.get(self.name)
    
    @property
    def _registry(self):
        return self.__registry
    
    @classmethod
    def bind(cls, registry):
        cls.__registry = registry
        

class context_(Variable):
    """
    context variable which represents objects that have lifespan of
    a rule execution
    """
    
    def __init__(self, name: str):
        super().__init__('use', name)
        
    @property
    def value(self):
        return self.__registry.get(self.name)
    
    @property
    def _registry(self):
        return self.__registry
    
    @classmethod
    def bind(cls, registry):
        cls.__registry = registry