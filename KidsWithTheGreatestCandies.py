# Kids With The Greatest Number of Candies


class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maximum = max(candies)
        li = []
        for i in candies:
            if i + extraCandies >= maximum:
                li.append(True)
            else:
                li.append(False)

        return li
