class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new = None
        ans = new
        curr = head
        stack = []
        while curr != None:
            stack.append(curr)
            curr = curr.next
        if stack:
            ans = stack.pop()
            new = ans
        while stack:
            curr = stack.pop()
            curr.next = None
            new.next = curr
            new = new.next
        return ans
