''' My solution '''

from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
      for i in range (len(nums)):
        left ,right = i, len(nums)-1
        #print(left,right)
        while left < right :
            '''print(nums[left],nums[right])'''
            if nums[left] == nums[right] and abs(left-right)<=k:
              
                return True
            else:
                right -= 1
                
            

            
               
              

      return False 
        


        
                    
               
                    


nums = list(map(int,input("nums: ").split()))
k = int(input("k: "))

Solution = Solution()

if Solution.containsNearbyDuplicate(nums,k):
    print("true")
else:
    print("false")    
        