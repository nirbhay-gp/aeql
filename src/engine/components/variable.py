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
    def set_registry(cls, registry):
        cls.__registry = registry
        

class use_(Variable):
    
    def __init__(self, name: str):
        super().__init__('use', name)
        
    @property
    def value(self):
        return self.__registry.get(self.name)
    
    @property
    def _registry(self):
        return self.__registry
    
    @classmethod
    def set_registry(cls, registry):
        cls.__registry = registry