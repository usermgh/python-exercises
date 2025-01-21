class Solution:
    def findNumbers(self, nums: [int]):
        count = 0
        
        for i in nums:
            digit_nums = len(str(abs(i)))
            if digit_nums % 2 == 0:
                count += 1
        return count
           






x = Solution()
result = x.findNumbers([555,901,482,1771])
print(result)