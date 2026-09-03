class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow=0
        for fast in range(len(nums)):
            if nums[fast]!=0:
                nums[slow]=nums[fast]
                slow+=1
        for i in range(slow, len(nums)):
            if nums[i] in nums:
                nums[i]=0
        return nums




class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        r = 0

        while r<len(nums):
            
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
            r+=1
                

