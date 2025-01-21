class Solution:
    def threeSumClosest(self, nums:[int], target: int) -> int:
        result = []
        for i in range(len(nums) -2 ):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    sum = nums[i] + nums[j] +nums[k]
                    if sum < target:
                          
                    return sum