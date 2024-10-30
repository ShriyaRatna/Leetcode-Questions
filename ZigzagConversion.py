class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        arr = [["" for _ in range(len(s))] for row in range(numRows)]
        row = 0
        column = 0
        add = 1
        for i in range(len(s)):
            arr[row][column] = s[i]
            if row == numRows - 1:
                add = -1
            elif row == 0:
                add = 1
            row += add
            column += 1

        return "".join(sum(arr, []))
