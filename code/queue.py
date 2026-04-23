

class Queue:
    def __init__(self):
        self.array = []
        self.is_empty = True

    def push(self, thing):
        if thing not in self.array:
            self.array.append(thing)
            self.is_empty = False

    def can_pop(self):
        return not self.is_empty

    def pop(self):
        if self.is_empty:
            raise Exception("Error: cannot pop from an empty queue!")
        ans = self.array[0]
        if len(self.array) == 1:
            self.array = []
            self.is_empty = True
        else:
            self.array = self.array[1:]
        return ans
    
    def peek(self):
        return False if not self.array else self.array[0]
    
    def size(self):
        return len(self.array)
        