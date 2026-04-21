class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        intme = set()
        for i in nums:
            if i in intme:
                return True
            else:
                intme.add(i)
        return False               

               
        