class Solution:
    def FindKthToTail(self, head, k):
        if head == None or k <= 0:
            return None
        fast = head
        slow = head
        for i in range(k-1):
            if fast.next == None:
                return None
            fast = fast.next
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        return slow