# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        p1 = head
        p2 = head.next
        head2 = head.next

        while p2 and p2.next:
            p1.next = p2.next
            p1 = p1.next

            p2.next = p1.next
            p2 = p2.next
        
        p1.next = head2
        return head

