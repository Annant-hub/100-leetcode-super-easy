class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        j = 0
        n = len(nums)
        nums.sort()
        
        for i in range(1,n):
            if nums[j] == nums[i]:
                return True
            else:
                j += 1
        return False



```````````````````````````Best_Solution``````````````````````````


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))   
