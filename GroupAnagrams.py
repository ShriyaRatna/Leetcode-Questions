class Solution:
    def groupAnagrams(self, strs) -> list[list[str]]:
        dic = {}
        for i in strs:
            x = str(sorted(i))
            if x in dic.keys():
                dic[x].append(i)
            else:
                dic[x] = [i]
        return list(dic.values())
