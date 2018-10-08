class Solution:
    def maxProfit_range(self, prices):
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

    def maxProfit(self, prices):
        profit_at_most_1 = self.maxProfit_range(prices)

        max_profit = 0
        for i in range(len(prices)):
            potential_profit = self.maxProfit_range(prices[:i]) + self.maxProfit_range(prices[i:])
            if potential_profit > max_profit:
                max_profit = potential_profit

        return max_profit


if __name__ == '__main__':
    prices = [int(x) for x in input().split()]
    print(prices)

    sol = Solution()
    print(sol.maxProfit(prices))