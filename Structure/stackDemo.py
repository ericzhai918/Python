class Stack(object):
    def __init__(self, limit=10):
        self.__items = []
        self.__limit = limit

    def isEmpty(self):
        return self.__items == []

    def peek(self):
        return self.__items[len(self.__items) - 1]

    def size(self):
        return len(self.__items)

    def push(self, item):
        if len(self.__items) >= self.__limit:
            self.double_limit()
        self.__items.append(item)

    def pop(self):
        if len(self.__items) <= 0:
            return -1
        else:
            return self.__items.pop()

    def double_limit(self):
        self.__limit *= 2

if __name__=="__main__":
    myStack = Stack()
    myStack.push(1)
    myStack.push(3)
    myStack.push(5)
    myStack.push(7)
    myStack.push(8)
    print(myStack.size())
    myStack.pop()
    myStack.pop()
    myStack.pop()
    print(myStack.size())
