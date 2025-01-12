class Solution:
    def firstUniqChar(self, s: str) -> int:
        news = s
        for i in news:
            if news.count(i) == 1:
                return s.find(i)
            else:
                news = news.replace(i, "")
        return -1
