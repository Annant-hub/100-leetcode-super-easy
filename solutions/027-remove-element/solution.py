class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=val
        if i not in nums:
            return len(nums)
        else:
            while i in nums:
                nums.remove(i)
            return len(nums)
        
