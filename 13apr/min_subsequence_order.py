def minSubsequence(self, nums):
sa=sum(nums)
n1=[]
sn=0
nums.sort()
nums=nums[::-1]
i=0
n=len(nums)
while(i<n):
    n1.append(nums[i])
    sa=sa-nums[i]
    sn=sn+nums[i]
    if sn>sa:
        return n1
    else:
        i=i+1
nums=list(map(int,input().split()))
print(minSubsequence(nums))