class Stack:
    def __init__(self,max_size):
        self.stack = list()
        self.max_size = max_size

    def push(self,e):
        if len(self.stack)< self.max_size:
            self.stack.append(e)

    def pop(self):
        if self.stack: return self.stack.pop()
        else: return 'Empty'
        