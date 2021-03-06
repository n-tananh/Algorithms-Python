class Stack :
    def __init__(self) :
        self.items = []

    def push(self, item) :
        self.items.append(item)

    def pop(self) :
        return self.items.pop()

    def top(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]

    def isEmpty(self) :
        return (self.items == [])

    def size(self):
        return len(self.items)





