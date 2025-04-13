"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pointer is used to denote the index of the node that tail's next pointer is connected to. Note that pointer is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""
class node():
    def __init__(self, data):
        self.data = data
        self.next = None

def create_linked_list(arr):
    if not arr:
        return None
    head = node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = node(value)
        current = current.next
    return head  


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
    # Tạo list chung từ 7 -> 8 -> 9
    common = create_linked_list([7, 8, 9])

    # Tạo listA: 3 -> 4 -> 1 -> common
    headA = create_linked_list([3, 4, 1])
    temp = headA
    while temp.next:
        temp = temp.next
    temp.next = common  # Nối vô node chung

    # Tạo listB: 1 -> 2 -> 3 -> 1 -> common
    headB = create_linked_list([1, 2, 3, 1])
    temp = headB
    while temp.next:
        temp = temp.next
    temp.next = common  # Nối vô node chung

    r = Solution()
    r.run(headA, 1)