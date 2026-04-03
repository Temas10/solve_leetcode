class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        result = 0                      # максимальная найденная прибыль

        lowest = prices[0]              # запоминаем цену в первый день как наименьшую цену
        for price in prices:
            if price < lowest:
                lowest = price

            result = max(result, price - lowest)     # определяем максимальную прибыль

        return result