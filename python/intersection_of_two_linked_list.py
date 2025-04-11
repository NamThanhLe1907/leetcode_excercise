""""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head

class Solution(object):
    def _get_length(head):
        if not head:
            return None
        length = 0
        while head:
            length += 1
            head.next
        return length
         
    
    def getIntersectionNode(self, headA, headB):
        def _get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length   
        A = headA
        B = headB
        C = _get_length(A)
        D = _get_length(B)
        print("C",C)
        print("D",D)
        
        
        while C > D:
            A = A.next
            C -=1
        while D > C:
            B = B.next
            D -=1
            
             
        while A and B:
            print(A.data, B.data)
            if A == B:
                print("found intersection")        
            A = A.next
            B = B.next

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
    r.getIntersectionNode(headA, headB)
  