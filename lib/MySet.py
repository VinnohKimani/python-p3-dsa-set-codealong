class MySet:
    def __init__(self, enumerable=[]):
        self.dictionary={}
        for value in enumerable:
             self.dictionary[value] = True

    # Runnig add
    def add(self, value):
        # Adding a value as a key in the dictionary
        self.dictionary[value] = True
        # Return the updated set
        return self
    
    # Checks whether value is already included in the set
    def has(self, value):
        return value in self.dictionary
    
    # Running Delete
    def delete(self, value):
        # Deleting a value
        self.dictionary.pop(value, None)
        # Returning the   set after delete
        return self
    
    # Running size Check
    def size(self):
        return len(self.dictionary)
    
    # Running Delete All(Myset.clear)
    # Removes all the items from the set, and returns the updated set.
    def clear(self, *values):
        self.dictionary.clear(*values)
        # returning updated set
        return self
    
    # Printing the set    
    def __str__(self):
        # empty list to hold the sets
        set_list = []
        for key, value in self.dictionary.items():
            set_list.append(str(key))
        return f'MySet: {{{",".join(set_list)}}}'
    
    




# def first_repeated_value(list):
#     # create a Set to keep track of values we've seen
#     number_set = set()
#     # iterate over each element from the list
#     for i in range(0, len(list)):
#         # if we've already seen a value, we've found the duplicate!
#         if list[i] in number_set:
#             return list[i]
#         # otherwise, add the value to our set
#         number_set.add(list[i])
#     # return None if we reach the end and haven't found our value
#     return None


# first_repeated_value([1, 2, 3, 3, 4, 4])