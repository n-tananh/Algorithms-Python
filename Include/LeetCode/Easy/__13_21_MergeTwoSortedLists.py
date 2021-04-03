# Definition for singly-linked list.
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

def printList(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next


def mergeTwoLists(l1: Node, l2: Node):
    # Dieu kien dung
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    # Merge l1 to l2
    if l1.data <= l2.data:
        nextL1 = l1.next
        newEl = mergeTwoLists(nextL1, l2)
        l1.next = newEl
        return l1

    else:  # lấy 1 phần tử của L2
        mergeTwoLists(l2, l1)
        return l2


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(4)

    n1.next = n2
    n2.next = n3


    n4 = Node(3)
    n5 = Node(6)
    n6 = Node(7)

    n4.next = n5
    n5.next = n6

    printList(n1)
    print('\n')
    printList(n4)

    print('\n')
    newList = mergeTwoLists(n1, n4)

    printList(newList)

