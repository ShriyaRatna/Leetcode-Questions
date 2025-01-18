# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        if temp.next == None:
            temp = None
            return temp
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
