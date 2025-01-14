from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        if len(set(nums)) == len(nums):
            return False
        else:
            return True  

nums = list(map(int,input("nums: ").split()))

Solution = Solution()

if Solution.containsDuplicate(nums):
    print("true")
else:
    print("false")    
        