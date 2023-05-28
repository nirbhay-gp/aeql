from abc import ABCMeta


class Literal(metaclass=ABCMeta):
    
    __type: str
    __value: str
    
    def __init__(self, *args):
        self.__type = args[0]
        self.__value = args[1]
        
    @property
    def type(self):
        return self.__type
    
    @property
    def value(self):
        return self.__value