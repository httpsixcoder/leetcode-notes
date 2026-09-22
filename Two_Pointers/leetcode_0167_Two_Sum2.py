"""
题目：167. 两数之和 II - 输入有序数组 (Two Sum II - Input Array Is Sorted)
链接：https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/
难度：中等
标签：数组、双指针、二分查找

思路：
双指针（最优）。


时间复杂度：O(n) —— 双指针最多遍历一次数组。
空间复杂度：O(1) —— 只使用常数个额外变量。
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # 双指针
        i, j = 0, len(numbers) - 1
        while i < j:
            res = numbers[i] + numbers[j]
            if res < target:
                i += 1
            elif res > target:
                j -= 1
            else:
                return [i + 1, j + 1]
        return []
