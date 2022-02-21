from pydantic import NoneIsAllowedError
from sqlalchemy import null


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a= Node(7)
b= Node(2)
c= Node(-3)
d= Node(-1)
e= Node(5)

a.next = b 
b.next = c
c.next = d
d.next = e
def getNodeValue(head, index):
    current = head
    while current!= None:
        if index == 0 :
            return current.val
        else:
            index -=1
            current= current.next
    return None
    # if head == None:
    #     return None
    # if index == 0:
    #     return head.val
    # return getNodeValue(head.next, index-1)
    
print(getNodeValue(a, 2))