nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
i=0
j=len(nums2)
k= len(nums1)-1
while nums1[i]!=0:
    i=i+1
pointer1=i-1
pointer2=j-1

while pointer2>=0:
    if pointer1>=0 and nums1[pointer1]>nums2[pointer2]:
        nums1[k]=nums1[pointer1]
        pointer1-=1
    else:
        nums1[k]=nums2[pointer2]
        pointer2-=1
    k-=1
print(nums1)

# actual solution

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last = m + n - 1
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1
