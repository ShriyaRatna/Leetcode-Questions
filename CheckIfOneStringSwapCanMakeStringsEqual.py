class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        if len(s1) != len(s2):
            return False

        if sorted(list(s1)) != sorted(list(s2)):
            return False

        count = 0
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            else:
                count += 1

        if count == 2:
            return True
        return False
