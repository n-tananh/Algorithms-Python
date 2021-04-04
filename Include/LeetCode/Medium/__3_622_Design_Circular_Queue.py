class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [None]*k
        self.front = self.rear = -1
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.rear += 1
        if self.isEmpty():
            self.front = self.rear
        if self.rear == self.size:
            self.rear = 0

        self.queue[self.rear] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.queue[self.front] = None
        self.front += 1
        if self.front == self.size:
            self.front = 0
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size

    def printQueue(self):
        return self.queue

if __name__ == '__main__':
    k = 6
    value = 100

    obj = MyCircularQueue(k)
    param_1 = obj.enQueue(6)
    param_2 = obj.enQueue(6)
    param_3 = obj.enQueue(6)
    param_4 = obj.enQueue(6)
    param_5 = obj.enQueue(6)
    param_9 = obj.deQueue()
    param_10 = obj.deQueue()
    param_11 = obj.deQueue()

    print(obj.printQueue())

