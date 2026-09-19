"""
题目：31. 下一个排列 (Next Permutation)
链接：https://leetcode.cn/problems/next-permutation/
难度：中等
标签：数组、双指针

思路：
1. 从右向左找到第一个相邻升序对 (i, i+1)，即 nums[i] < nums[i+1]，令 left = i。
2. 如果找不到，说明当前排列是降序（最大排列），直接反转整个数组得到升序。
3. 如果找到 left，从右向左找到第一个大于 nums[left] 的元素 nums[right]。
4. 交换 nums[left] 和 nums[right]。
5. 将 left+1 到末尾的子数组反转（原来这部分是降序，反转后变成升序）。

时间复杂度：O(n) —— 最多遍历数组三次，n 为数组长度。
空间复杂度：O(1) —— 原地修改，只使用常数个额外变量。
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        left = n - 2
        while left >= 0 and nums[left] >= nums[left + 1]:
            left -= 1
        if left == -1:
            nums.reverse()
        else:
            right = n - 1
            while nums[left] >= nums[right]:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
            # 方法一：内置反转函数【注意要原地修改】
            nums[left + 1:] = nums[left + 1:][::-1]
            # 方法二：双指针实现反转
            # left += 1
            # right = n - 1
            # while left < right:
            #     nums[left], nums[right] = nums[right], nums[left]
            #     left += 1
            #     right -= 1
