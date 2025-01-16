from collections import defaultdict
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_dict = defaultdict(list)
        no_of_jewels = 0
        s_jewel = tuple(sorted(jewels))

        for j in s_jewel:
            jewels_dict[j].append(j)

        for s in stones:
            if s in jewels_dict:
                no_of_jewels +=1
            else:
                continue
        return no_of_jewels                

jewels, stones = map(str, input().split())        

Solution = Solution()

result = Solution.numJewelsInStones(jewels,stones)

print(result)
