class Solution:
    def reverse(self, x: int) -> int:
        x = list(str(x))
        if x[0] != "":
            return int("".join(x.reverse()))
        else:
            x.remove("-")
            return int("".join(x.reverse())) * -1
