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

# def reverseList(head):

#     prev = None
#     current =head
#     while current !=None:
#         next= current.next
#         current.next = prev
#         prev = current
#         current = next
#     return prev
def reverseList(head,prev = None):
    if head ==None:
        return prev
    next = head.next
    head.next = prev
    return reverseList(next , head)


print(reverseList(a).val)
new_head =reverseList(a)
print(reverseList(new_head).val)

