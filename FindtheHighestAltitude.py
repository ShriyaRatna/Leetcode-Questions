class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        new = []
        new.append(0)
        for i in range(len(gain)):
            new.append(gain[i] + new[i])

        return max(new)
