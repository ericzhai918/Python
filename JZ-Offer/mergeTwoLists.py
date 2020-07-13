class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#方法一：迭代
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        currentNode = tempNode = ListNode(0)
        if not l1 and not l2:
            return None
        while l1 and l2:
            if l1.val <= l2.val:
                currentNode.next = l1
                l1 = l1.next
            else:
                currentNode.next = l2
                l2 = l2.next
            currentNode = currentNode.next

        if l1 or l2:
            currentNode.next = l1 or l2

        return tempNode.next

#方法一：迭代（简化）
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        currentNode = tempNode = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                currentNode.next = l1
                l1 = l1.next
            else:
                currentNode.next = l2
                l2 = l2.next
            currentNode = currentNode.next
        currentNode.next = l1 or l2
        return tempNode.next

#方法二：递归
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        while l1 and l2:
            if l1.val < l2.val:
                l1.next = self.mergeTwoLists(l1.next,l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1,l2.next)
                return l2