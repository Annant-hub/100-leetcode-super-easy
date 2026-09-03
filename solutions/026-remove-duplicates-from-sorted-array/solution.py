nums=[0,0,1,1,1,2,2,3,3,4]
num1=[]
i=0
for j in range(1, len(nums)):
    if nums[i]==nums[j]:
        i=j
    else:
        num1.append(nums[i])
        i=j
num1.append(nums[i])
nums=num1
print(len(nums))  
print(num1)
