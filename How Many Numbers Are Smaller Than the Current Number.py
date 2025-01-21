def smallerNumbersThanCurrent(nums):
    result = []  # This will store the count for each number
    
    for i in range(len(nums)):  # Iterate over each element
        count = 0  # Count numbers smaller than nums[i]
        for j in range(len(nums)):  # Compare with all other elements
            if nums[j] < nums[i]:   # If a number is smaller, increment count
                count += 1
        result.append(count)  # Store the count in the result list
    
    return result

# Example usage:
nums = [7,7,7,7]
print(smallerNumbersThanCurrent(nums))  # Expected Output: [4, 0, 1, 1, 3]
