class Solution(object):
    def isValid(self, s):
        stack = []
        di = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i in di.values():
                stack.append(i)
            if i in di.keys():
                if len(stack) != 0 and di[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack) != 0:
            return False
        return True
