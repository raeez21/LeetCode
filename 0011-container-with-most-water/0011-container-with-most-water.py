class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        #print(height)
        left = 0
        right  = len(height) - 1
        
        max_val = 0
        
        while left < right:
            curr_val = min(height[left],height[right]) * (right-left)
            max_val = max(curr_val, max_val)
            
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return max_val
            
        