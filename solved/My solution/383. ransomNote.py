#My Solution
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:



        ransomecounter = Counter(ransomNote)
        print(sorted(ransomecounter))
        print(ransomecounter)
        magcounter = Counter(magazine)
        print(sorted(magcounter))
        print(magcounter)
        commonkeys = set(ransomecounter.keys()) & set(magcounter.keys())
        print(commonkeys)

        if len(commonkeys) != 0:
            for key in commonkeys:
                if ransomecounter[key] <= magcounter[key]:
                    return True
                else:
                    return False
        else:
            return False

ransomNote, magazine = map(str, input().split())

Solution = Solution()

result = Solution.canConstruct(ransomNote,magazine)

print(result)



