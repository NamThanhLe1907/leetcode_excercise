"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pointer is used to denote the index of the node that tail's next pointer is connected to. Note that pointer is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""
class node():
    def __init__(self, data):
        self.data = data
        self.next = None


class pos():
    def __init__(self, node):
        self.node = node

    def next_node(self):
        self.node = self.node.next


class Solution(object):
    def run(self, head, p):
        loop_node = None
        for i in range(len(head)):
            number = node(head[i])
            if i == 0:
                head_node = number
            else:
                prev.next = number

            if i == p:
                loop_node = number

            prev = number

        if p != -1:
            prev.next = loop_node

        pointer = pos(head_node)
        for _ in range(10):
            print("Data", pointer.node.data)
            pointer.next_node()


if __name__ == '__main__':
    head = [3, 2, 0, -4]
    p = 1
    g = Solution()
    g.run(head, p)
