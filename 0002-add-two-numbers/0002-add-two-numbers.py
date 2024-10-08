# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tempnode = ListNode()
        pointer = tempnode
        carry = 0

        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
            else:                
                val1 = 0
            if l2:
                val2 = l2.val
            else:
                val2 = 0

            val = val1 + val2 + carry
            carry = val//10
            appendval = val%10

            pointer.next = ListNode(appendval)
            pointer = pointer.next
            
            if l1:
                l1 = l1.next
            else:
                None
            if l2:
                l2 = l2.next
            else:
                None

        self.print_linked_list(tempnode.next)

        return tempnode.next

    def print_linked_list(self, node: Optional[ListNode]):
        while node:
            print(node.val, end=" -> " if node.next else "\n")
            node = node.next
