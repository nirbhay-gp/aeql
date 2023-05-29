
class context_store:
    
    def __init__(self):
        self.__values = {}
        
    def get_(self, key):
        return self.__values.get(key)
    
    def set_(self, key, value):
        self.__values[key] = value