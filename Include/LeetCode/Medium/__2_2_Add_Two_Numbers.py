# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def printLinkedList(head):
    tmp = head
    while tmp:
        print(tmp.val, end=' ')
        tmp = tmp.next
    print()

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    cur = dummy

    carry = 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        sumV = v1 + v2 + carry
        carry = sumV // 10
        sumV = sumV % 10
        cur.next = ListNode(sumV)

        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next




if __name__ == '__main__':
    n1 = ListNode(2)
    n2 = ListNode(4)
    n3 = ListNode(3)
    n4 = ListNode(3)
    n1.next = n2
    n2.next = n3
    n3.next = n4


    l1 = ListNode(5)
    l2 = ListNode(6)
    l3 = ListNode(4)
    l1.next = l2
    l2.next = l3


    print("Add")
    printLinkedList(addTwoNumbers(n1, l1))