from abc import ABCMeta, abstractproperty

class Rule(metaclass=ABCMeta):
    
    @abstractproperty
    def descriptor(self):
        pass
    
    @abstractproperty
    def selector(self):
        pass
    
    @abstractproperty
    def qualifier(self):
        pass
    
    @abstractproperty
    def executor(self):
        pass
    
    @abstractproperty
    def result(self):
        pass