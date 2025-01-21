class Solution:
    def merge(self, nums1:[int], m: int, nums2: [int], n: int):

        nums1.extend(nums2)
        nums1.sort()
        for i in range(len(nums2)):
            if len(nums1) > m+n:
                nums1.remove(0)

        return nums1


Solution = Solution()
result = Solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
print(result)