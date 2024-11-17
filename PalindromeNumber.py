class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        for i in range(len(x) / 2):
            if x[i] != x[len(x) - 1 - i]:
                return False
        return True


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         return str(x) == str(x)[::-1]
        
	    