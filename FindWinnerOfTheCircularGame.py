class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        fren = []
        for i in range(1, n + 1):
            fren.append(i)

        i = 0
        while len(fren) > 1:
            # print(fren)
            if i > len(fren) - k:
                i = (i + k - 1) % (len(fren))
            else:
                i = i + k - 1
            # print(i)
            fren.pop(i)
        # print(fren)
        return fren[0]
