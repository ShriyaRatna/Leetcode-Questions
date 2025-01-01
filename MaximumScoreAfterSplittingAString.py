class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        maximum = -1
        n = 1
        s = list(s)
        while n < (len(s)):
            left = s[0:n]
            right = s[n : len(s)]
            zero = left.count("0")
            one = right.count("1")
            sumation = one + zero
            if sumation > maximum:
                maximum = sumation
            n = n + 1

        return maximum
