class Solution:
    def firstUniqChar(self, s: str) -> int:
        news = s
        for i in news:
            if news.count(i) == 1:
                return s.find(i)
            else:
                news = news.replace(i, "")
        return -1


# class Solution:
#     def firstUniqChar(self,s:str)->int:
#         freq=[0]*26
#         for c in s:
#             freq[ord(c)-ord('a')]+=1
#         for i,c in enumerate(s):
#             if freq[ord(c)-ord('a')]==1:
#                 return i
#         return -1
