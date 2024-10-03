class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ans = []
        for i in range(min(len(word1), len(word2))):
            ans.append(word1[i])
            ans.append(word2[i])
        for j in range(i + 1, len(word1)):
            ans.append(word1[j])
        for j in range(i + 1, len(word2)):
            ans.append(word2[j])

        ans = "".join(ans)
        return ans
