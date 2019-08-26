class Queue:

    def __init__(self):
        self.Q = []

    def is_empty(self):
        return self.Q == []

    def enqueue(self, i):
        self.Q.insert(0, i)

    def dequeue(self):
        return self.Q.pop(len(self.Q) - 1)

    def traverse(self):
        return self.Q

    def search(self, x):
        try:
            return str(x)+" is at "+str(self.Q.index(x))
        except ValueError:
            return str(x)+" is Not in Queue"
