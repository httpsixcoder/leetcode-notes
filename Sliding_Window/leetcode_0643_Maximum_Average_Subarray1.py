"""
题目：643. 子数组最大平均数 I (Maximum Average Subarray I)
链接：https://leetcode.cn/problems/maximum-average-subarray-i/
难度：简单
标签：数组、滑动窗口

思路：滑动数组

时间复杂度：O(n) —— 只需遍历一次数组，每次滑动窗口更新和为 O(1)。
空间复杂度：O(1) —— 只使用了常数个变量。
"""


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        win_num = sum(nums[:k])
        max_win = win_num
        for i in range(k, len(nums)):
            win_num += nums[i] - nums[i - k]
            # max_win=max(max_win,win_num)
            max_win = max_win if max_win > win_num else win_num
        return max_win / k
