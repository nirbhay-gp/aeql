from abc import ABCMeta, abstractproperty, abstractclassmethod

class Variable(metaclass=ABCMeta):
    type: str
    name: str
    
    def __init__(self, *args):
        self.__type = args[0]
        self.__name = args[1]
        
    @property
    def type(self):
        return self.__type
    
    @property
    def name(self):
        return self.__name
    
    @abstractproperty
    def value(self):
        pass
    
    @abstractproperty
    def _registry(self):
        pass
    
    @abstractclassmethod
    def set_registry(cls, registry):
        pass