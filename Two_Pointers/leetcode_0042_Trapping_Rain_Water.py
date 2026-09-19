"""
题目：42. 接雨水 (Trapping Rain Water)
链接：https://leetcode.cn/problems/trapping-rain-water/
难度：困难
标签：数组、双指针、动态规划、单调栈

思路：
1. 对于每个位置 i，能接的雨水量 = min(左侧最大高度, 右侧最大高度) - height[i]。
2. 动态规划：
    - 对于每个位置 i，它能接的水量取决于：
    - water[i] = min(left_max[i], right_max[i]) - height[i]
3. 双指针优化：
    - 在前面思路上，维护两个指针一起向中间逼近，存放扫过的最大值
    - 当前i能接最大的水，min（左，右，其他不确定）
    - 当 左<右时，无论其他却不确定，结果都是左  【关键】
    - 其他情况下，无论其他却不确定，结果都是右  【关键】

时间复杂度：O(n) —— 双指针仅遍历一次数组。
空间复杂度：O(1) —— 只使用常数个额外变量。
"""


class Solution:
    def trap(self, height: list[int]) -> int:
        # 双指针
        res = 0
        n = len(height)
        left = 0
        right = n - 1
        max_left = 0
        max_right = 0
        while left < right:
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])
            if max_left < max_right:
                res += max_left - height[left]
                left += 1
            else:
                res += max_right - height[right]
                right -= 1
        return res
        # 动态规划
        # n = len(height)
        # water = 0
        # left_max = [height[0]] * n
        # for i in range(1, n):
        #     left_max[i] = max(height[i], left_max[i - 1])
        # right_max = [height[-1]] * n
        # for i in range(n - 2, -1, -1):
        #     right_max[i] = max(height[i], right_max[i + 1])
        # for i in range(n):
        #     water += min(left_max[i], right_max[i]) - height[i]
        # return water
