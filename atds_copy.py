

class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def getStack(self):
        return self.stack()

    def __repr__(self):
        return "Stack" + str(self.stack)

class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        return self.queue.pop()

    def peek(self):
        return self.queue[-1]

    def size(self):
        return len(self.queue)

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def __repr__(self):
        return "Queue" + str(self.queue)

class Deque(object):
    def __init__(self):
        self.deque = []

    def add_rear(self, item):
        self.deque.insert(0, item)

    def add_front(self,item):
        self.deque.append(item)

    def remove_front(self):
        self.deque.pop()

    def remove_rear(self):
        self.deque.remove(0)

    def size(self):
        return len(self.deque)

    def is_empty(self):
        if len(self.deque) == 0:
            return True
        else:
            return False

    def __repr__(self):
        return "Deque" + str(self.deque)