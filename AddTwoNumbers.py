# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list1 = []
        temp = l1
        while temp.next != None:
            list1.append(temp.val)
            temp = temp.next
        list1.append(temp.val)
        list2 = []
        temp = l2
        while temp.next != None:
            list2.append(temp.val)
            temp = temp.next
        list2.append(temp.val)

        if len(list1) > len(list2):
            x = len(list2)
            for i in range(x, len(list1)):
                list2.append(0)

        elif len(list1) < len(list2):
            x = len(list1)
            for i in range(x, len(list2)):
                list1.append(0)

        # list1.reverse()
        # list2.reverse()
        ans = []
        carry = 0
        print(len(list1), len(list2))
        for i in range(len(list1)):
            x = list1[i] + list2[i] + carry
            if x > 9:
                carry = 1
            else:
                carry = 0
            ans.append(x % 10)
        if carry == 1:
            ans.append(1)

        # ans.reverse()

        curr = ListNode(ans[0])
        head = curr
        # curr.val = ans[0]
        for i in range(1, len(ans)):
            temp = ListNode(ans[i])
            curr.next = temp
            curr = curr.next
        return head
