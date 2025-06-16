# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = {}
        index = 0
        current = head

        while current:
            if current in visited:
                return current
            visited[current] = index
            current = current.next
            index += 1

        return None
