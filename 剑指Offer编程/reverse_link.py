#方法1
def printListFromTailToHead(self, listNode):
    newList = []
    while listNode:
        newList.append(listNode.val)
        listNode = listNode.next
    return newList[::-1]

# 方法2
    def printListFromTailToHead(self, listNode):
        stack = []
        while listNode:
            stack.append(listNode.val)
            listNode = listNode.next
        list = []
        while stack:
            list.append(stack.pop())
        return list