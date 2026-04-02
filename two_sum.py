class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        uni_numbers = {}                   # пустой словарь (хеш-таблица)
        for idx, num in enumerate(nums):   # idx — индекс, num — текущее число
            desire = target - num          # какое число нужно, чтобы в сумме с num дать target
            if desire in uni_numbers:      # если это число уже встречалось раньше
                return [uni_numbers[desire], idx]       # возвращаем индексы: сохранённый и текущий
            uni_numbers[num] = idx          # иначе запоминаем текущее число и его индекс