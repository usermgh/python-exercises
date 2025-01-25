class Solution:
    def removeDuplicates(self, nums: [int]):

        n = len(nums)
        count = 0
        if not nums:
            return 0
        for i in range(1, n):
            if nums[i] != nums[count]:
                count += 1
                nums[count] = nums[i]

        return count + 1
        
x = Solution()
result = x.removeDuplicates([1,1,2])
print(result)        