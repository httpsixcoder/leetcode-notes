"""
题目：15. 三数之和 (3Sum)
链接：https://leetcode.cn/problems/3sum/
难度：中等
标签：数组、双指针、排序

思路：
1. 先对数组进行排序，利用单调性方便去重和指针移动。
2. 固定一个数 nums[i]，在其右侧用双指针 left 和 right 夹逼寻找 -nums[i]。
3. 三数之和等于 0 时记录答案，并跳过左右两侧的重复元素。
4. 剪枝：若固定元素 nums[i] > 0，则三数之和必然 > 0，直接结束。

时间复杂度：O(n^2) —— 外层遍历 O(n)，内层双指针 O(n)。
空间复杂度：O(1) —— 不考虑排序所需的栈空间，仅用常数个变量。
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 排序：为去重和双指针移动提供单调性
        temp = sorted(nums)
        n = len(temp)
        res = []

        for v in range(n - 2):
            # 剪枝1：排序后若固定元素 > 0，后面的元素都 > 0，三数之和不可能为 0
            if temp[v] > 0:
                break

            # 剪枝2：跳过重复的固定元素，避免产生重复三元组
            if v > 0 and temp[v] == temp[v - 1]:
                continue

            left, right = v + 1, n - 1

            while left < right:
                s = temp[v] + temp[left] + temp[right]

                if s == 0:
                    # 找到一组解
                    res.append([temp[v], temp[left], temp[right]])

                    # 去重：跳过左侧重复元素
                    while left < right and temp[left] == temp[left + 1]:
                        left += 1
                    # 去重：跳过右侧重复元素
                    while left < right and temp[right] == temp[right - 1]:
                        right -= 1

                    # 指针同时收缩，进入下一轮查找
                    left += 1
                    right -= 1

                elif s < 0:
                    # 和偏小，左指针右移增大和
                    left += 1
                else:
                    # 和偏大，右指针左移减小和
                    right -= 1

        return res
