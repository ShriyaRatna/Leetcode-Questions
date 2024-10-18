class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s)
        t = list(t)

        track = -1
        for i in range(len(s)):
            if s[i] in t:
                flag = 0
                for j in range(len(t)):
                    if t[j] == s[i] and j > track:
                        track = j
                        flag = 1
                        break
                if not flag:
                    return False
            else:
                return False
        return True
