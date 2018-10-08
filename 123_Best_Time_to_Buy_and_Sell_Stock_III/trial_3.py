import numpy as np

# with help from
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/135704/Detail-explanation-of-DP-solution

class Solution:
    def maxProfit(self, prices):
        K = 2 # max number of transactions
        n = len(prices)
        prices_1_idx = [-1]
        prices_1_idx.extend(prices)

        L = np.zeros((K+1, n+1))
        # print(prices_1_idx)

        for k in range(1, K+1):
            for i in range(1, n+1):
                term_2 = L[k-1, i] - prices_1_idx[i]
                if i == 1:
                    _max = term_2
                else:
                    _max = max(_max, term_2)

                L[k, i] = max(L[k, i-1], prices_1_idx[i] + _max)

        return int(L[K, n])


if __name__ == '__main__':
    prices = [int(x) for x in input().split()]
    print(prices)

    sol = Solution()
    print(sol.maxProfit(prices))