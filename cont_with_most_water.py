class Solution:
    def maxArea(self, nums: List[int]) -> int:
        

        left = 0
        right = len(nums) - 1

        summ = 0

        while left <= right:
            s = abs(right - left) * min(nums[left], nums[right])
            summ = max(summ, s)

            if nums[left] > nums[right]:
                right -= 1
            else:
                left += 1

        return(summ)