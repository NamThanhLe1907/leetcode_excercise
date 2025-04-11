
class Solution(object):
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

        while C > D:
            A = A.next
            C -=1
        while D > C:
            B = B.next
            D -=1

        while A and B:
            if A == B:
                return A        
            A = A.next
            B = B.next
        return None
