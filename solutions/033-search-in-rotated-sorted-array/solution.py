class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        while start<=end:
            mid= start+(end-start)//2

            if nums[mid]>nums[end]:
                start=mid+1
            else:
                end=mid
            for i in range(start, len(nums)):
                if nums[i]==target:
                    return i
            for i in range(0,start):
                if nums[i]==target:
                    return i
            return -1
        return -1
