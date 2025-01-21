class Solution:
    def missingNumber(self, nums: [int]) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums)+1):
            if i not in nums:
                return i


x = Solution()
result = x.missingNumber([9,6,4,2,3,5,7,0,1])
print(result)