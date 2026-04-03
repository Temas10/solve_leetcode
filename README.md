Решение задач с LeetCode
=

1. Two Sum
-----------
Given an array of integers ```nums``` and an integer ```target```, return indices of the two numbers such that they add up to ```target```.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**Example 1:**

>Input: nums = [2,7,11,15], target = 9
>Output: [0,1]
>Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

**Example 2:**

>Input: nums = [3,2,4], target = 6
>Output: [1,2]

**Example 3:**

>Input: nums = [3,3], target = 6
>Output: [0,1]

**Solution:**
```
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        uni_numbers = {}                   # пустой словарь (хеш-таблица)
        for idx, num in enumerate(nums):   # idx — индекс, num — текущее число
            desire = target - num          # какое число нужно, чтобы в сумме с num дать target
            if desire in uni_numbers:      # если это число уже встречалось раньше
                return [uni_numbers[desire], idx]       # возвращаем индексы: сохранённый и текущий
            uni_numbers[num] = idx          # иначе запоминаем текущее число и его индекс
```

217. Contains Duplicate
-----------------------
Given an integer array ```nums```, return ```true``` if any value appears at least twice in the array, and return ```false``` if every element is distinct.

**Example 1:**

>Input: nums = [1,2,3,1]
>
>Output: true
>
>Explanation:
>
>The element 1 occurs at the indices 0 and 3.

**Example 2:**

>Input: nums = [1,2,3,4]
>
>Output: false
>
>Explanation:
>
>All elements are distinct.

**Example 3:**

>Input: nums = [1,1,1,3,3,4,3,2,4,2]
>
>Output: true

**Solution:**
```
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) == len(set(nums)):     # условие уникальностт всех элементов
            return False
        else:
            return True
```

242. Valid Anagram
------------------

Given two strings ```s``` and ```t```, return ```true``` if ```t``` is an anagram of ```s```, and ```false``` otherwise.

**Example 1:**

>Input: s = "anagram", t = "nagaram"
>
>Output: true

**Example 2:**

>Input: s = "rat", t = "car"
>
>Output: false

**Solution:**
```
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):       # Если строки разной длины, они заведомо не могут быть анаграммами
            return False
        
        count_s = {}
        count_t = {}

        for char_s, char_t in zip(s,t):
            count_s[char_s] = count_s.get(char_s, 0) + 1  # считаем количество уникальных букв 
            count_t[char_t] = count_t.get(char_t, 0) + 1  # для каждого слова

        return count_s == count_t
```