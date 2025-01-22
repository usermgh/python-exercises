class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = ['']* numRows
        index,step = 0,1

        for char in s:
            rows[index] += char

            if index == 0:
                step = 1 #go down
            
            elif index == numRows - 1:
                step = -1 #go up
            
            index += step

        return ''.join(rows)

        


x = Solution()
result= x.convert("AB", 1)
print(result)