class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        highest_count= max(freq.values())

        for i in freq:
            if freq[i]==highest_count:
                return i
                

