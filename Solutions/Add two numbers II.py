# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        
        
        def trav(node):
            
            n = ''
            while node:
                
                n += str(node.val)
                
                node = node.next
                
            
            return n
        
        
        s1 = trav(l1)
        s2 = trav(l2)
        
        sum_num = int(s1) + int(s2)
        
        sum_num = str(sum_num)
        
        head = ListNode(int(sum_num[0]))
        prev = head
        
        
        for i in range(1,len(sum_num)):
            
            node = ListNode(int(sum_num[i]))
            prev.next = node
            
            prev = node
        
        return head
            
            
            
        
        