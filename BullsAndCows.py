class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        A = B = 0
        guess_list = list(guess)

        for i in range(n):
            if secret[i] == guess[i]:
                A += 1
                guess_list[i] = ""

        for i in range(n):
            if secret[i] != guess[i] and secret[i] in guess_list:
                B += 1
                guess_list[guess_list.index(secret[i])] = ""

        return f"{A}A{B}B"
