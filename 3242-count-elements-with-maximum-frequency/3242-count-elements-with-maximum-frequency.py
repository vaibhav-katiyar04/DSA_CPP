class Solution(object):
    def maxFrequencyElements(self, nums):
        freq=[0]*101 # we need size 100 but problem is that freq list index start from 0,for100 is goes on 99
        mx=0
        ans=0
        for i in nums:
            freq[i]+=1
            f=freq[i]
            if f>mx:
                mx=f
                ans=f
            elif f==mx:
                ans+=mx
        return ans
        