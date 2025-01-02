class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        vowels = ['a', 'e', 'i', 'o', 'u']
        ans = []
        newMap = []
        for i in range(len(words)):
            string = list(words[i])
            if string[0] in vowels and string[len(string)-1] in vowels:
                words[i] = 1
                newMap.append( 1)
            else:
                words[i] = 0
                newMap.append(0)
            if i>0:
                words[i] = words[i] + words[i-1]
        for li in queries:
            ans.append(words[li[1]] - words[li[0]] + newMap[li[0]])

        return ans