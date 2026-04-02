class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) == len(set(nums)):     # условие уникальностт всех элементов
            return False
        else:
            return True