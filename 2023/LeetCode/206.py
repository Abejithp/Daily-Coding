class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail, temp = None, None
        curr = head
       
        while curr != None:
            temp = curr.next
            curr.next = tail
            tail = curr
            curr = temp
        return tail
