class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        target = 0 
        s = set()
        
        for i in range(len(nums)):
            j = i+1
            k = len(nums) - 1
            
            while(j < k):
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    s.add((nums[i],nums[j],nums[k]))
                    j += 1
                    k -= 1
                elif sum < target:
                    j += 1
                else:
                    k -= 1
        out = list(s)
        print(out)
        return out
   
    
  
                    
                    
        