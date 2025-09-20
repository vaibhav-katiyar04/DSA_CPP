class Solution(object):
    def nextPermutation(self, nums):
# we have 3 methos 1..brute force find all possible permutatiion and linear search for next 
#2...in cpp we have next_permutaion(start,end) function
#optimised way find pattern
        n=len(nums)
        x=0
        m=0
        mini=200
        flag=0
        for i in range(n-2,-1,-1):
            for j in range(i,n-1):
                if(nums[i]<nums[j+1]):
                    flag=1
                    if(mini>nums[j+1]):
                        mini=nums[j+1]
                        m=j+1

            if(flag==1):
                 nums[m],nums[i]=nums[i],nums[m]
                 x=i+1
                 break   

        if(flag==0):
            nums.sort()
        else:
           nums[x:n]=sorted(nums[x:n])
        return nums