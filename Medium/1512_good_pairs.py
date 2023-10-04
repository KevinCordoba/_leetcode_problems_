class Solution(object):
    def numIdenticalPairs(self, nums):
        cont = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(nums[i] == nums[j] and i < j):
                    cont += 1
        return cont