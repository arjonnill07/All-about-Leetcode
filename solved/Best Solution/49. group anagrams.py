from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        annagram_dict = defaultdict(list)
        result = []

        for s in strs:
            sorted_s = tuple(sorted(s))
            annagram_dict[sorted_s].append(s)
        for i in annagram_dict.values():
            result.append(i)

        return result      

strs = list(map(str,input("list of strings: ").split()))


Solution = Solution()

result = Solution.groupAnagrams(strs)

print(result)
    

        