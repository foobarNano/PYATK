class Element:

    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE: Element = nextE

class MyLinkedList:

    def __init__(self):
        self.head: Element = None
        self.tail: Element = None
        self.size: int = 0

    def __str__(self):
        result = '[' + __recursive(self.head) + ']'

    def get(self, e: Element):
        temp: Element = self.head
        while temp != e:
            if temp == None: return
            temp = temp.nextE
        return temp
        

    def delete(self, e: Element):
        if self.head == e:
            self.head = self.head.nextE
            return

        temp: Element = self.head
        while temp.nextE != e:
            if temp.nextE == None: return
            temp = temp.nextE
        temp.nextE = temp.nextE.nextE
        

    def append(self, e: Element, func = None):
        pass

    def __recursive(e: Element) -> str:
        if e.nextE == None: return e.data
        return e.data + ', ' + __recursive_get(self, e.nextE)