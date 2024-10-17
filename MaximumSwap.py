class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        number = num
        li = []
        while number > 0:
            li.append(number % 10)
            number = number // 10

        li.reverse()
        x = max(li)
        # print(li)
        if li[0] != x:
            for i in range(len(li) - 1, -1, -1):
                if x == li[i]:
                    li[i] = li[0]
                    li[0] = x
            # print(li)
            li = int("".join(map(str, li)))
            return li

        else:
            new_li = sorted(li)
            new_li.reverse()
            # print(li)
            # print(new_li)
            for i in range(len(li)):
                if li[i] == new_li[i]:
                    continue
                else:
                    large = i + 1
                    for j in range(i + 1, len(li)):
                        if li[large] <= li[j]:
                            large = j
                    x = li[i]
                    li[i] = li[large]
                    li[large] = x
                    # print(li)
                    break
            li = int("".join(map(str, li)))
            return li
