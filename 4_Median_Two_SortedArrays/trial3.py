import random as r

class Solution(object):

    def binarySearch(self, a, start, end, b):

        if start > end:
            return None

        i = (start + end) // 2
        j = (len(a) + len(b) -1) // 2
        k = (j-i)

        if k < 0:
            return self.binarySearch(a, start, i-1, b)
        if k == 0:
            if a[i] <= b[0]:
                return a[i], i, k
            else:
                return self.binarySearch(a, start, i-1, b)
        if k == len(b):
            if b[k-1] <= a[i]:
                return a[i], i, k
            else:
                return self.binarySearch(a, i+1, end, b)
        if k > len(b):
            return self.binarySearch(a, i+1, end, b)

        if b[k-1] <= a[i] <= b[k]:
            return a[i], i, k
        elif a[i] < b[k-1]:
            return self.binarySearch(a, i+1, end, b)
        else:
            return self.binarySearch(a, start, i-1, b)

    def findMedianSingleArray(self, nums):
        idx = (len(nums) - 1) // 2
        if len(nums) % 2 == 1:
            m = nums[idx] * 1.0
        else:
            m = (nums[idx] + nums[idx + 1]) / 2

        return m

    def findMedianSortedArrays(self, nums1, nums2) -> float:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # print(nums1)
        # print(nums2)

        m = len(nums1)
        n = len(nums2)

        if m == 0:
            return self.findMedianSingleArray(nums2)
        elif n == 0:
            return self.findMedianSingleArray(nums1)

        ret_val = self.binarySearch(nums1, 0, m-1, nums2)
        if ret_val is not None:
            median, i, k = ret_val
            # compare between a[i+1] and b[k]
            # (i+1) < m
            # k < n, because i need to do b[k]
            next_val_1 = nums1[i + 1] if (i + 1) < m else None
            next_val_2 = nums2[k] if (k) < n else None
        else:
            median, i, k = self.binarySearch(nums2, 0, n-1, nums1)
            # compare between a[i+1] and b[k]
            # (i+1) < m
            # k < n, because i need to do b[k]
            next_val_1 = nums2[i + 1] if (i + 1) < n else None
            next_val_2 = nums1[k] if (k) < m else None


        # assert (next_val_1 is None) and (next_val_2 is None)

        if next_val_1 is None:
            next_val = next_val_2
        elif next_val_2 is None:
            next_val = next_val_1
        else:
            next_val = min(next_val_1, next_val_2)

        if (m+n) % 2 == 1:
            return median
        else:
            return (median + next_val) / 2

#
s = Solution()
while True:
    m = r.randint(1, 5)
    n = r.randint(1, 5)
    nums1 = sorted([r.randint(0, 100) for _ in range(m)])
    nums2 = sorted([r.randint(0, 100) for _ in range(n)])

    print("nums1 : {0}".format(nums1))
    print("nums2 : {0}".format(nums2))

    nums_merged = sorted(nums1 + nums2)

    idx = (m+n-1) // 2
    if (m+n) % 2 == 1:
        m1 = nums_merged[idx]
    else:
        m1 = (nums_merged[idx] + nums_merged[idx+1]) / 2

    m2 = s.findMedianSortedArrays(nums1, nums2)

    print("m1 : {0}".format(m1))
    print("m2 : {0}".format(m2))

    assert m1 == m2

# if __name__ == '__main__':
#     s = Solution()
#
#     nums1 = [1,2,3,5,6,7]
#     nums2 = [4]
#
#     print(s.findMedianSortedArrays(nums1, nums2))
