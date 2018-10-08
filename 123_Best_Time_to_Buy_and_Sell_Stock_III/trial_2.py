import numpy as np

class Solution:
    def maxProfit(self, prices):
        K = 2 # max number of transactions
        n = len(prices)
        prices_1_idx = [-1]
        prices_1_idx.extend(prices)

        L = np.zeros((n+1, K+1))
        # print(prices_1_idx)

        for i in range(1, n+1):
            for k in range(1, K+1):
                possible_profits = [L[i-1, k]]
                for j in range(1, i):
                    t2 = L[j, k - 1] + prices_1_idx[i] - prices_1_idx[j]
                    # print(t2)
                    possible_profits.append(t2)

                L[i, k] = max(possible_profits)

        return int(L[n, K])


if __name__ == '__main__':
    prices = [int(x) for x in input().split()]
    print(prices)

    sol = Solution()
    print(sol.maxProfit(prices))