class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        top = -1
        s = list(s)
        for i in range(len(s) - 1, -1, -1):
            if s[i] != "*" and top != -1 and stack[top] == "*":
                stack.pop()
                top -= 1
            else:
                stack.append(s[i])
                top += 1
        s = []
        while len(stack) != 0:
            s.append(stack.pop())
        return "".join(s)
