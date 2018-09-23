from Queue import Queue

queue = Queue()
queue.put('a') 
queue.put('b')
queue.put('c')
queue.put('d') # size 4 list - 'a' 'b' 'c' 'd'
print(queue)
queue.pop()
print(queue)
queue.pop()
queue.pop()
queue.pop()
print(queue)
print(queue.size())