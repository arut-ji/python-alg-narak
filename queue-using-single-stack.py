class Stack:
    def __init__(self):
        self.container = []
        self.size = 0

    def push(self, item):
        self.container += [item]
        self.size += 1

    def pop(self):
        last = self.container[-1]
        self.container = self.container[:-1]
        self.size -= 1
        return last

    def top(self):
        return self.container[-1]

    def empty(self):
        return self.size == 0


class Queue:

    def __init__(self):
        self.container = Stack()

    def enqueue(self, item):
        self.container.push(item)

    def dequeue(self, container=None):
        if container is None:
            return self.dequeue(self.container)
        else:
            if container.size == 1:
                # last = container.top()
                return container.pop()
            else:
                last_item = self.container.pop()
                first_item = self.dequeue(self.container)
                self.container.push(last_item)
                return first_item


array = [1, 2, 3, 4, 5, 6]
q = Queue()
for item in array:
    q.enqueue(item)

print(q.container.container)

while not q.container.empty():
    print(q.dequeue())
