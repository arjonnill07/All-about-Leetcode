#My solution
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_counter = Counter(s)
        t_counter = Counter(t)

        if s_counter == t_counter:
            return True
        else:
            return False


s,t = map(str,input().split())

Solution = Solution()

result = Solution.isAnagram(s,t)

print(result)