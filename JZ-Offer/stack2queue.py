class Solution:
    def __init__(self):
        self.stackIn = []
        self.stackOut = []

    def push(self, node):
        self.stackIn.append(node)

    def pop(self):
        if len(self.stackOut):
            return self.stackOut.pop()
        while self.stackIn:
            self.stackOut.append(self.stackIn.pop())
        return self.stackOut.pop()