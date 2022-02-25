class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a= Node(7)
b= Node(2)
c= Node(-3)
d= Node(-1)
e= Node(6)

a.next = b 
b.next = c
c.next = d
d.next = e

g= Node(3)
h= Node(6)
i= Node(0)

g.next = h
h.next = i


def zipperLists(head1, head2):
    tail = head1
    head = head1
    current1 = head1.next
    current2 = head2
    count = 0

    while current1 != None and current2 != None:
        if count%2==0:
            tail.next = current2
            current2= current2.next
        else:
            tail.next = current1
            current1= current1.next 
        tail = tail.next
        count+=1


    if current1 != None:
        tail.next = current1
    if current2 != None:
        tail.next = current2

    return head

def printLinkedList(head):
    if head == None:
        return
    print(head.val,end = '')
    if head.next != None:
        print("->",end = '')
    printLinkedList(head.next)

printLinkedList(zipperLists(a, g))
