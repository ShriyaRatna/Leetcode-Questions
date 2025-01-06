class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        fren = []
        for i in range(1,n+1):
            fren.append(i)
        i = 0
        while(len(fren)>1):
            i = (i + k - 1)%(len(fren)) 
            fren.pop(i)
        return fren[0]