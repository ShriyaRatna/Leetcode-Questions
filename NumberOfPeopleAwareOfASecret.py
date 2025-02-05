# class Solution:
#     def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
#         counter = {}
#         counter[1] = [delay + 1, forget + 1]
#         for i in range(delay+1, n+1):
#             indices = [k for (k, v) in counter.items() if v[1] == i]
#             for j in indices:
#                 counter.pop(j)
#             num = sum(1 for (k, v) in counter.items() if v[0] <= i < v[1])
#             for j in range(1, num + 1):
#                 counter[i + (j/10)] = [delay + i, forget + i]

#         return len(counter.items())
