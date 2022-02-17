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


def linkedListFind(head, target):
    if head == None: 
        return False
    if head.val == target:
        return True
    return linkedListFind(head.next, target)
    
    # current = head
    # while current != None:
    #     if current.val == target:
    #         return True
    #     else:
    #         current= current.next
    # return False


print(linkedListFind(a,1))