class ArrayStack:
    """LIFO Stack implementation using python list"""
    pass
    def __init__(self):
        """Creates an empty stack. """
        self.__data = []
    
    def __len__(self):
        """Returns the number of elements in the stack"""
        return len(self.__data)

    def is_empty(self):
        """Returns True if stack is empty"""
        return self.__len__() == 0
    
    def push(self, e):
        """Add an element e to the top of stack"""
        self.__data.append(e)
    
    def pop(self):
        """Removes and returns the element from the top of stack
           (LIFO)"""
        if self.is_empty():
            raise Empty('Stack is empty')
        
        return self.__data.pop()

    def top(self):
        """Return the element at top of the stack, without removing
           from the stack"""
        if self.is_empty():
            raise Empty('Stack is empty')
        
        return self.__data[-1]

class Empty(Exception):
    """Error attempting to access an element from an empty stack"""
    pass
