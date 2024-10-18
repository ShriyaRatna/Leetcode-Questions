class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        li = {}
        for i in set(nums):
            li[i] = nums.count(i)
        li = sorted(li.items(), key=lambda x: x[1])
        li.reverse()
        print(li)
        ans = []
        for i in range(k):
            ans.append(li[i][0])
        return ans
