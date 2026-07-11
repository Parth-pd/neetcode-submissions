# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        l = 0 #total nodes
        while curr: #for counting the length of linkedlist
            curr = curr.next
            l += 1
        curr = head # again setting the curr pointer to head
        
        for _ in range(l - n - 1):
            curr = curr.next
        if n == l:
            head = head.next
        else:
            if curr.next != None:
                curr.next = curr.next.next
        return head