class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
 
 
# to print a linked list
def printList(head):
    curr = head
    result = []
    while curr:
        result.append(curr.data)
        curr = curr.next
    # print("None")
    print("your list is",result)
 
 
# Function to identify and remove cycle in a linked list using hashing
def removeCycle(head):
    prev = None        # previous pointer
    curr = head        # main pointer
 
    # maintain a set to store visited nodes
    s = set()
 
    # traverse the list
    while curr:
        # `s` previous pointer to None if the current node is seen before
        if curr in s:
            prev.next = None
            return
 
        s.add(curr)
 
        # update the previous pointer to the current node and
        # move the main pointer to the next node
        prev = curr
        curr = curr.next
 
 
if __name__ == '__main__':
 
    # total number of nodes in the linked list
    n = int(input("enter how many element in list"))
    elements=[]
    for ele in range(n):
        element = int(input("enter element: "))
        elements.append(element)

    # construct a linked list
    head = None
    for i in reversed(elements):
        head = Node(i, head)
    removeCycle(head)
    printList(head)
    X = int(input("enter X value"))
    if ((X>=0) and (X<=n)):
        print(1)
    else:
        print(0)