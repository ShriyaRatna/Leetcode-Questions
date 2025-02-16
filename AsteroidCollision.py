class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for i in asteroids:
            while ans and i < 0 < ans[-1]:
                if -i > ans[-1]:
                    ans.pop()
                    continue
                elif -i == ans[-1]:
                    ans.pop()
                break
            else:
                ans.append(i)
        return ans
