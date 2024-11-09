class Solution:
    def intToRoman(self, num: int) -> str:
        nums = {
            1: "I",
            5: "V",    4: "IV",
            10: "X",   9: "IX",
            50: "L",   40: "XL",
            100: "C",  90: "XC",
            500: "D",  400: "CD",
            1000: "M", 900: "CM",
        }
        r = ''
        s = sorted(list(nums.keys()))
        s.reverse()
        for n in s:
            while n <= num:
                r += nums[n]
                num-=n
        return r