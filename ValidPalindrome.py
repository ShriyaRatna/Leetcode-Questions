import string


class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        s = s.replace(" ", "")
        s = self.remove(s)
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False

        return True

    def remove(self, s):
        punc = """!()-[]{};:'"\,<>./?@#$%^&*_~`"""
        for ele in s:
            if ele in punc:
                s = s.replace(ele, "")

        return s
