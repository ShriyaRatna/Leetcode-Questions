# solution 1
class Solution:
    def reverseWords1(self, s: str) -> str:
        words = s.split()
        res = []

        for i in range(len(words) - 1, -1, -1):
            res.append(words[i])
            if i != 0:
                res.append(" ")

        return "".join(res)

    # solution 2
    def reverseWords2(self, s: str) -> str:
        words = list(s.split())
        words.reverse()
        return " ".join(words)
