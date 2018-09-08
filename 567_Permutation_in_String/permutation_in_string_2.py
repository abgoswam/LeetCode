class Solution:

    def __init__(self):
        self.dict_s1 = {}
        self.hash_s1 = 0

    def compute_dict_hash_s1(self, s1):

        for c in s1:
            self.hash_s1 += ord(c)

            if c in self.dict_s1:
                self.dict_s1[c] += 1
            else:
                self.dict_s1[c] = 1

    def is_permutation(self, b):
        dict_b = {}

        for c in b:
            if c not in self.dict_s1:
                return False

            if c in dict_b:
                dict_b[c] += 1
                if dict_b[c] > self.dict_s1[c]:
                    return False
            else:
                dict_b[c] = 1

        return True

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if len(s1) > len (s2):
            return False

        self.compute_dict_hash_s1(s1)

        s2_sub = s2[:len(s1)]
        s2_sub_hash = 0
        for c in s2_sub:
            s2_sub_hash += ord(c)

        if s2_sub_hash == self.hash_s1 and self.is_permutation(s2_sub):
            return True

        for i in range(1, len(s2)-len(s1)+1):
            drop = s2_sub[0]
            s2_sub = s2[i: i + len(s1)]
            s2_sub_hash = s2_sub_hash - ord(drop) + ord(s2_sub[-1])

            if s2_sub_hash == self.hash_s1 and self.is_permutation(s2_sub):
                return True

        return False


if __name__ == '__main__':
    s1 = input()
    s2 = input()
    print("{0}, {1}".format(s1, s2))

    soln = Solution()
    print(soln.checkInclusion(s1, s2))
