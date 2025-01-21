#max number of int to choosen from range
class Solution:
    def maxCount(self, banned:[int], n: int, maxSum: int) -> int:
        maxNumber=0
        count= 0
        for i in range(1, n+1):
            if i in banned:
                continue
            maxNumber+=i
            if maxNumber > maxSum:
                break
            count+=1

        
        return count
solution = Solution()
result= solution.maxCount([1,5,6], 5, 6)
print(f"result is {result}")