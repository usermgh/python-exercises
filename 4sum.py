
class Solution:
    def fourSum(self, nums:[int], target: int):
        nums.sort()  # Step 1: Sort the array
        n = len(nums)
        result = []
    
        for i in range(n - 3):  # First number
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate numbers
                continue

            for j in range(i + 1, n - 2):  # Second number
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicate numbers
                    continue
            
                left, right = j + 1, n - 1  # Two-pointer initialization
            
                while left < right:  # Step 3: Two-pointer search
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                    # Skip duplicate numbers
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1
                
                    elif total < target:
                        left += 1  # Move left pointer to increase sum
                    else:
                        right -= 1  # Move right pointer to decrease sum
    
        return result

x = Solution()
result = x.fourSum([2,2,2,2,2], 8)  
print(result)