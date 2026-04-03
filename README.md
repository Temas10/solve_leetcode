Решение задач с LeetCode
=

**1. Two Sum**
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

**217. Contains Duplicate**
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

**242. Valid Anagram**
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

**49. Group Anagrams**
------------------

Given an array of strings ```strs```, group the anagrams together. You can return the answer in any order.

**Example 1:**

>Input: strs = ["eat","tea","tan","ate","nat","bat"]
>
>Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
>
>Explanation:
>
>There is no string in strs that can be rearranged to >form "bat".
>The strings "nat" and "tan" are anagrams as they can be >rearranged to form each other.
>The strings "ate", "eat", and "tea" are anagrams as >they can be rearranged to form each other.

**Example 2:**

>Input: strs = [""]
>
>Output: [[""]]

**Example 3:**

>Input: strs = ["a"]
>
>Output: [["a"]]

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

**167. Two Sum II - Input Array Is Sorted**
----------------------------------------

Given a 1-indexed array of integers ```numbers``` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific ```target``` number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers ```index1``` and ```index2```, each incremented by one, as an integer array ```[index1, index2]``` of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

**Example 1:**

>Input: numbers = [2,7,11,15], target = 9
>Output: [1,2]
>Explanation: The sum of 2 and 7 is 9. Therefore, index1 >= 1, index2 = 2. We return [1, 2].

**Example 2:**

>Input: numbers = [2,3,4], target = 6
>Output: [1,3]
>Explanation: The sum of 2 and 4 is 6. Therefore index1 >= 1, index2 = 3. We return [1, 3].

**Example 3:**

>Input: numbers = [-1,0], target = -1
>Output: [1,2]
>Explanation: The sum of -1 and 0 is -1. Therefore >index1 = 1, index2 = 2. We return [1, 2].

**Solution:**
```
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:                             # алгоритм: два указателя
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            
            if total > target:
                right -= 1
            else:
                left += 1
```

**121. Best Time to Buy and Sell Stock**
------------------------------------

You are given an array ```prices``` where ```prices[i]``` is the price of a given stock on the ``i^th`` day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return ```0```.

**Example 1:**

>Input: prices = [7,1,5,3,6,4]
>Output: 5
>Explanation: Buy on day 2 (price = 1) and sell on day 5 >(price = 6), profit = 6-1 = 5.
>Note that buying on day 2 and selling on day 1 is not >allowed because you must buy before you sell.

**Example 2:**

>Input: prices = [7,6,4,3,1]
>Output: 0
>Explanation: In this case, no transactions are done and >the max profit = 0.

**Solution:**
```
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        result = 0                      # максимальная найденная прибыль

        lowest = prices[0]              # запоминаем цену в первый день как наименьшую цену
        for price in prices:
            if price < lowest:
                lowest = price

            result = max(result, price - lowest)     # определяем максимальную прибыль

        return result
```

 **374. Guess Number Higher or Lower**
 ----------------------------------

We are playing the Guess Game. The game is as follows:

I pick a number from ```1``` to ```n```. You have to guess which number I picked (the number I picked stays the same throughout the game).

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API ```int guess(int num)```, which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. ```num > pick```).
1: Your guess is lower than the number I picked (i.e. ```num < pick```).
0: your guess is equal to the number I picked (i.e. ```num == pick```).
Return the number that I picked.

**Example 1:**

>Input: n = 10, pick = 6
>Output: 6

**Example 2:**

>Input: n = 1, pick = 1
>Output: 1

**Example 3:**

>Input: n = 2, pick = 1
>Output: 1

**Solution:**
```
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            res = guess(mid)   # вызов API, который возвращает -1, 1 или 0
            if res == 0:
                return mid
            elif res == -1:    # mid > pick, нужно искать левее
                right = mid - 1
            else:              # res == 1, mid < pick, нужно правее
                left = mid + 1
        return -1  # по условию задачи всегда найдётся
```

**155. Min Stack**
--------------
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the ```MinStack``` class:

- ```MinStack()``` initializes the stack object.
- ```void push(int val)``` pushes the element ```val``` onto the stack.
- ```void pop()``` removes the element on the top of the stack.
- ```int top()``` gets the top element of the stack.
- ```int getMin()``` retrieves the minimum element in the stack.

You must implement a solution with ```O(1)``` time complexity for each function.

**Example 1:**

>Input
>["MinStack","push","push","push","getMin","pop","top",>"getMin"]
>[[],[-2],[0],[-3],[],[],[],[]]
>
>Output
>[null,null,null,null,-3,null,0,-2]
>
>Explanation
>MinStack minStack = new MinStack();
>minStack.push(-2);
>minStack.push(0);
>minStack.push(-3);
>minStack.getMin(); // return -3
>minStack.pop();
>minStack.top();    // return 0
>minStack.getMin(); // return -2

**Solution:**
```
class MinStack:

    def __init__(self):
        self.stack = []                    # создаем два стека
        self.stack_min = []                # основной и для миннимальных значений
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.stack_min:                      
            val = min(val, self.stack_min[-1])
        self.stack_min.append(val)

        
    def pop(self) -> None:
        self.stack.pop()
        self.stack_min.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_min[-1]
       


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

**1704. Determine if String Halves Are Alike
--------------------------------------------

You are given a string ```s``` of even length. Split this string into two halves of equal lengths, and let ```a``` be the first half and ```b``` be the second half.

Two strings are alike if they have the same number of vowels (```'a'```, ```'e'```, ```'i'```, ```'o'```, ```'u'```, ```'A'```, ```'E'```, ```'I'```, ```'O'```, ```'U'```). Notice that ```s``` contains uppercase and lowercase letters.

Return ```true``` if ```a``` and ```b``` are alike. Otherwise, return ```false```.

**Example 1:**

>Input: s = "book"
>Output: true
>Explanation: a = "bo" and b = "ok". a has 1 vowel and b >has 1 vowel. Therefore, they are alike.

**Example 2:**

>Input: s = "textbook"
>Output: false
>Explanation: a = "text" and b = "book". a has 1 vowel >whereas b has 2. Therefore, they are not alike.
>Notice that the vowel o is counted twice.

**Solution:**
```
# первое решение
class Solution:
    vowels = frozenset({'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'})
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s) // 2
        count = sum(s[idx] in self.vowels for idx in range(mid))
        count -= sum(s[idx] in self.vowels for idx in range(mid, len(s)))   
        return not count
    
# второе решение
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        v='aeiou'
        x = int(len(s)/2)
        a = s[0:x]
        b = s[x:]
        aa, bb = 0,0
        for i,j in zip(a,b):
            if i in v:
                aa += 1
            if j in v:
                bb += 1
        if aa == bb:
            return True
        else:
            return False 
```