class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printList(head):
    while head is not None:
        print(head.val, end=' ')
        head = head.next
    print()


def swapPairs(head: ListNode) -> ListNode:
    if head is None:
        return None
    if head.next is None:
        return head

    # THTQ
    nextNode = head.next

    # Swap head and nextNode
    head.next = nextNode.next
    nextNode.next = head

    # Recursion
    headNew = swapPairs(head.next)

    # Noi bai toan hian tai vao bai toan con
    head.next = headNew

    return nextNode


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)

    n1.next = n2

    printList(n1)

    res = swapPairs(n1)

    print("After swap")
    printList(res)
