"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head: return None

        cur = head
        hmp = {}

        while cur:
            # node = Node(x=cur.val)
            # hmp[cur] = node
            hmp[cur] = Node(x=cur.val)
            cur = cur.next

        cur = head

        while cur:
            new_node = hmp[cur]
            new_node.next = hmp[cur.next] if cur.next else None
            new_node.random = hmp[cur.random] if cur.random else None
            cur = cur.next

        return hmp[head]

        
        