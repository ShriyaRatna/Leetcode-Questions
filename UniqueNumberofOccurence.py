class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        no = [0] * len(set(arr))
        li = list(set(arr))
        for i in range(len(set(arr))):
            no[i] = arr.count(li[i])
        if len(set(no)) == len(set(arr)):
            return True
        else:
            return False
