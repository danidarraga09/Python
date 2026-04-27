class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def create_circle(n):
    head = Node(1)
    current = head

    for i in range(2,n+1):
        current.next = Node(i)
        current = current.next

        current.next = head
        return head
    
def josephus(n,k):
    head= create_circle(n)
    current = head
    prev = None

    while current.next != current:
        for _ in range(k-1):
            prev = current
            current.next

        prev.next = current.next
        current= current.next

    return current.data



