class Solution(object):
    def twoSum(self, nums, target):
        ans = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
        return ans
    
print(Solution().twoSum([3,2,4],6))
#sol = Solution()
#sol.twoSum([2,7,11,15],9)


