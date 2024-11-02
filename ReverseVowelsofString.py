class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        order = []
        stri = list(s)
        for i in stri:
            if i in vowels:
                order.append(i)
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if stri[i] in vowels:
                stri[i] = order[count]
                count += 1
        stri = "".join(stri)
        return stri
