class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a= Node('A')
b= Node('B')
c= Node('C')
d= Node('D')
e= Node('E')

a.next = b 
b.next = c
c.next = d
d.next = e

def printLinkedList(head):
    if head == None:
        return
    print(head.val,end = '')
    if head.next != None:
        print("->",end = '')
    printLinkedList(head.next)

    # current = head
    # while current != None:
    #     print(current.val,end = '')
    #     current = current.next
    #     if current != None:
            # print("->",end = '')


printLinkedList(a)