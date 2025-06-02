class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def list_to_linkedlist(arr):
    if not arr:
        return None
    head = Node(arr[0])
    curr = head
    for value in arr[1:]:
        curr.next = Node(value)
        curr = curr.next
    return head

def traverse(head:Node):
    curr = head
    while curr:
        print(curr.data, end='->')
        curr = curr.next
    print("None")

def length_of_ll(head):
    curr = head
    size = 0
    while curr:
        size += 1
        curr = curr.next
    return size

def search(head,data):
    curr = head
    while curr:
        if curr.data == data:
            return True
        curr = curr.next
    return False


l1 = [1,2,3,4,5]
head = list_to_linkedlist(l1)
traverse(head)
print(length_of_ll(head))
print(search(head,6))
