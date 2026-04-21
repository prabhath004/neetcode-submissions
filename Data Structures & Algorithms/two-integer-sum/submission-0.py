class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        intme = {}
        for i,j in enumerate(nums):
            diffme = target - j
            if diffme not in intme:
                intme[j] = i 
            else:
                return [intme[diffme], i]
        return     
         
        
        
        