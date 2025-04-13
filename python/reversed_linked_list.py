""""
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?






"""

class Node():
    def __init__(self,data):
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
    def reverseList(self,head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            
            prev = current 
            current = next_node
        return prev 
            
            
if __name__ in "__main__":
   common = [2,5,3,6,4,7] 
   
   head = create_linked_list(common)
   r = Solution()
   rev_arr = r.reverselist(head)
   print(rev_arr)
   
