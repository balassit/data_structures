class Node():

    def __init__(self, item):
        self.next = None
        self.previous = None
        self.item = item

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return (f'{self.item!r}')

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return self.item == other.item

class Queue(object):
    def __init__(self):
        self.length = 0
        self._head = None
        self._tail = None

    def put(self, item):
        newNode = Node(item=item)
        if(self._head == None):
            self._head = self._tail = newNode
        else:
            self._tail.next = newNode
            newNode.previous = self._tail
            self._tail = newNode
        self.length += 1
    
    def pop(self):
        item = self._head.item
        self._head = self._head.next
        self.length -= 1
        if(self.length == 0):
            self._tail = None
        return item
    
    def size(self):
        return self.length

    def empty(self):
        return self.length == 0

    def __iter__(self):
        current = self._head
        while current is not None:
            yield current
            current = current.next
    
    def __str__(self):
           return ' '.join(str(o) for o in self)