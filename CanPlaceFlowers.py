class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            elif i == 0 and flowerbed[i+1]!=1:
                flowerbed[i] = 1
                n -= 1

            elif i == len(flowerbed)-1 and flowerbed[i-1] !=1:
                flowerbed[i] = 1
                n -= 1

            elif flowerbed[i-1] !=1 and flowerbed[i+1]!=1:
                flowerbed[i] = 1
                n -= 1

            if n == 0:
                return True

        if n>0:
            return False
