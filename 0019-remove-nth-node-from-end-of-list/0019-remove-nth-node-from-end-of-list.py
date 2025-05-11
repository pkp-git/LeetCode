# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        temp = head
        count = 0
        
        while temp:
            count += 1
            temp = temp.next
        
        target = count - n
        temp = dummy
        for _ in range(target):
            temp = temp.next
        
        temp.next = temp.next.next
        
        return dummy.next
