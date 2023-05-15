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

    def get(self, e: Element) -> Element:
        pass

    def delete(self, e: Element):
        pass

    def append(self, e: Element, func = None):
        pass

    def __recursive(e: Element) -> str:
        if e.nextE == None: return e.data
        return e.data + ', ' + __recursive_get(self, e.nextE)