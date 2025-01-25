class Solution:
    def letterCombinations(self, digits: str) :
        if not digits:
            return []
        phone_number={'2':'abc', '3':'def','4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        result = []
        def backtrack(index:int, path:str):

            if index == len(digits):

                result.append(path)
                return

            for letter in phone_number[digits[index]]:

                backtrack(index + 1, path + letter)
        backtrack(0,'')
        return result

x = Solution()
result = x.letterCombinations('2')
print(result)