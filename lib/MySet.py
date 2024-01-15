class MySet:
    def __init__(self, enumerable=[]):
        self.dictionary = {}
        # the below will make sure the value is not stored in the dictionary if it's duplicated. In a dictionary, each key is unique, so duplicated keys will never happen.
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        # if the value is in the dictionary it will return true. If it's not, will return false.
        return value in self.dictionary
    
    def add(self, value):
        # Add a value as a key on the Dictionary and return the updated set.
        self.dictionary[value] = True
        return self
    
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self
    
    def size(self):
        return len(self.dictionary)
    
    def clear(self):
        self.dictionary.clear()
        
    def __str__(self):
        set_list = []
        for key in self.dictionary.keys():
            set_list.append(str(key))
        return f'MySet: {{{",".join(set_list)}}}'
    
# set = MySet([1, 2, 2, 3, 3])
# print(set.dictionary)
# print(set.has(5))
# print((set.add(5)).dictionary)
# print((set.delete(3)).dictionary)
# print(set.size())
# print(set.clear())
# print(set.__str__())
# print(set.dictionary)

        
    
            
        




    
