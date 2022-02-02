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
        if head == None:
            return None

        # Build dictionary of reference-newNode
        # Build all the new nodes
        node_dict = {}
        pointer = head
        while pointer:
            node_dict[pointer] = Node(pointer.val, None, None)
            pointer = pointer.next

        # Revise the reference
        pointer = head
        while pointer:
            if pointer.next:
                node_dict[pointer].next = node_dict[pointer.next]
            if pointer.random:
                node_dict[pointer].random = node_dict[pointer.random]
            pointer = pointer.next

        return node_dict[head]