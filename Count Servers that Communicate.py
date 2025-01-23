class Solution:
    def countServers(self, grid: [int]) -> int:
        m = len(grid)
        n= len(grid[0])
        row = [0] * m
        clum = [0] * n
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row[i] += 1
                    clum[j] +=1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row[i]>1 or clum[j]>1):
                    count +=1 
        return count
x = Solution()
result= x.countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]])
print(result)
        
        
