class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.max = maxSize
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.max != len(self.stack):
            self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            top = -1
        else:
            top = self.stack.pop()

        return top

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        for i in range(min(k, len(self.stack))):
            if self.stack[i]:
                self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
