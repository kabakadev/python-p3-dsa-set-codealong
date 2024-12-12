class MySet:
    def __init__(self,enumarable = []):
        self.dictionary = {}
        for value in enumarable:
            self.dictionary[value] = True
    def has(self,value):
        return value in self.dictionary
    def add(self,value):
        self.dictionary[value] = True
        return self
    def delete(self,value):
        self.dictionary.pop(value,None)
        return self
    def size(self):
        return len(self.dictionary)
    def clear(self):
        self.dictionary.clear()
        return self.dictionary
    def __str__(self):
       return f"MySet: {{{','.join(map(str, sorted(self.dictionary)))}}}"
