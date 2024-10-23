# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = head
        count = 0
        while temp.next != None:
            count += 1
            temp = temp.next
        n = count // 2
        if count % 2 == 1:
            n = n + 1

        count = 1
        temp = head
        while count < n:
            count += 1
            temp = temp.next

        curr = temp.next
        temp.next = temp.next.next
        curr = None
        return head


def create_linked_list(values):
    dummy = ListNode()
    curr = dummy
    for value in values:
        curr.next = ListNode(value)
        curr = curr.next
    return dummy.next


def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)


head = create_linked_list([1, 3, 4, 7, 1, 6])
solution = Solution()
new_head = solution.deleteMiddle(head)

print_linked_list(new_head)
