# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: ListNode) -> bool:
    """
    Using set, traversal through each node
        If in set dont have node -> add node to set
        if in set have node -> return have node
    """

    passed = set()
    tmp = head
    while tmp:
        if tmp in passed:
            return True
        passed.add(tmp)
        tmp = tmp.next
    return False




def floyd_algorithms(head: ListNode) -> bool:
    """
    2 pointer
        slow_p : jumped 1
        fast_p : jumped 2
    if have cycle :
        slow_p will meet fast_p in cycle
    else:
        never meet together
    """
    slow_p = head
    fast_p = head
    while slow_p and fast_p and fast_p.next:
        slow_p = slow_p.next
        fast_p = fast_p.next.next
        if slow_p is fast_p:
            return True
    return False


def printList(head: ListNode) -> None:
    tmp = head
    if tmp:
        while True:
            print(tmp.val, end=" ")
            tmp = tmp.next
            if tmp.val == head.val:
                break
    print()

if __name__ == '__main__':
    head = [3, 2, 0, -4]

    # Test case 1
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2


    # # Test case 2
    # n1 = ListNode(1)
    # n2 = ListNode(2)
    # n1.next = n2



    print(floyd_algorithms(n1))

