# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, heada: ListNode, headb: ListNode) -> Optional[ListNode]:
        if not heada or not headb:
            return None
        
        pa = heada
        pb = headb

        while pa!=pb:
            if pa:
                pa = pa.next
            else:
                pa = headb
            
            if pb:
                pb = pb.next
            else:
                pb = heada
        
        return pb