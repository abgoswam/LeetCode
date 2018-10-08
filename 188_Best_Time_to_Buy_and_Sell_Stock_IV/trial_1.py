import numpy as np

# with help from
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/135704/Detail-explanation-of-DP-solution

class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)
        prices_1_idx = [-1]
        prices_1_idx.extend(prices)

        # L = np.zeros((k+1, n+1))
        L = [[0 for _ in range(n+1)] for _ in range(k+1)]
        # print(prices_1_idx)

        for p in range(1, k+1):
            for i in range(1, n+1):
                term_2 = L[p-1][i] - prices_1_idx[i]
                if i == 1:
                    _max = term_2
                else:
                    _max = max(_max, term_2)

                L[p][i] = max(L[p][i-1], prices_1_idx[i] + _max)

        return L[k][n]


if __name__ == '__main__':
    prices = [int(x) for x in input().split()]
    print(prices)

    sol = Solution()
    print(sol.maxProfit(prices[-1], prices[:-1]))