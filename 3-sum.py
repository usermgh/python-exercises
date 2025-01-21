class Solution:
    def threeSum(self, nums):
        # Sort the array first (to make it easier to avoid duplicates)
        nums.sort()

        # List to store valid triplets
        result = []
        
        # Iterate through the array using i as the first index
        for i in range(len(nums) - 2):
            
            # Skip duplicates for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Now use two-pointer technique for the remaining part of the list
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    
                    result.append([nums[i], nums[left], nums[right]])

                    # Move the left pointer to avoid duplicates for the second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Move the right pointer to avoid duplicates for the third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Update both pointers after finding a valid triplet
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1  # If the sum is too small, move the left pointer to the right
                else:
                    right -= 1  # If the sum is too large, move the right pointer to the left

        return result


# Create an instance of the Solution class
x = Solution()

# Call the threeSum method with a sample input list
result = x.threeSum([0,0,0])

# Print the result
print(result)
