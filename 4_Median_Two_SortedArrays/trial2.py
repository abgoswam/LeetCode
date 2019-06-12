import random as r

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        print(nums1)
        print(nums2)



m = random.randint(1,5)
n = random.randint(1,5)
nums1 = sorted([r.randint(0, 100) for _ in range(m)])
nums2 = sorted([r.randint(0, 100) for _ in range(n)])
merged = sorted(nums1 + nums2)

print(nums1)
print(nums2)
print(merged)

i = (m+n) // 2
print("median {0}".format(merged[i]))


# if __name__ == '__main__':
#     s = Solution()
#     nums1 = [1, 3]
#     nums2 = [2]
#
#     print(s.findMedianSortedArrays(nums1, nums2))