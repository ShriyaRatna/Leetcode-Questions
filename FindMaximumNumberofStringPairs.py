class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        for i in range(len(words)):
            words[i] = "".join(sorted(words[i]))
            print(words[i])
        words.sort()
        i = 0
        count = 0
        while True:
            if i >= len(words) - 1:
                break
            if words[i] == words[i + 1]:
                count += 1
                i += 2
            else:
                i += 1
        return count
