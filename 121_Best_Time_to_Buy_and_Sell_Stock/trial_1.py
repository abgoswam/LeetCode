class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if prices is None or len(prices) <= 1:
            return 0

        min_so_far = prices[0]
        max_profit = 0
        for i in range (1, len(prices)):
            max_profit = max(max_profit, prices[i] - min_so_far)
            min_so_far = min(min_so_far, prices[i])

        return max_profit


if __name__ == '__main__':
    prices = [int(x) for x in input().split()]
    print(prices)

    sol = Solution()
    print(sol.maxProfit(prices))
