#方法1：
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        stackA = []
        stackB = []
        while headA:
            stackA.append(headA)
            headA = headA.next
        while headB:
            stackB.append(headB)
            headB = headB.next
        temp = None
        while stackA and stackB:
            a = stackA.pop()
            b = stackB.pop()
            if a != b:
                return temp
            else:
                temp = a
        return temp

#方法2：
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = lenB = 0
        ahead = headA
        bhead = headB
        while ahead:
            ahead = ahead.next
            lenA += 1
        while bhead:
            bhead = bhead.next
            lenB += 1
        if lenA > lenB:
            long = headA
            short = headB
        else:
            long = headB
            short = headA
        len = abs(lenA-lenB)
        for i in range(len):
            long = long.next
        while long != None and short != None and short != long:
            long = long.next
            short = short.next
        return long

#方法3：

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        pa = headA
        pb = headB
        while pa is not pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa