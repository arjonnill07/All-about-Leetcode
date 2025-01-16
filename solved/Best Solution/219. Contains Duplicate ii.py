''' Best Solution '''
#219.Find Duplicates ii


from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
      dict = {}
      for i in range((len(nums))):
        if nums[i] in dict and abs(i-dict[nums[i]])<=k:
          return True
        else:
          dict[nums[i]] = i
      return False

        
                    
               
                    


nums = list(map(int,input("nums: ").split()))
k = int(input("k: "))

Solution = Solution()

if Solution.containsNearbyDuplicate(nums,k):
    print("true")
else:
    print("false")    
        
