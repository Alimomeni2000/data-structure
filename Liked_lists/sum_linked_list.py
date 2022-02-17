class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a= Node(1)
b= Node(2)
c= Node(-3)
d= Node(-1)
e= Node(5)

a.next = b 
b.next = c
c.next = d
d.next = e

def sumList(head):
    if head == None:
        return 0
    return head.val+ sumList(head.next)

    # num = 0
    # current = head
    # while current != None:
    #     num += current.val
    #     current = current.next
    # return num


print(sumList(a))