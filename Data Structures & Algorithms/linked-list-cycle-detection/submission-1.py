# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        curr = head
        while curr:
            nxt = curr
            curr = curr.next
            if nxt not in seen:
                seen.add(nxt)
            else:
                return True
        return False

            
        
        