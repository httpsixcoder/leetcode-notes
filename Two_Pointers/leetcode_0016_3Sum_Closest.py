"""
题目：16. 最接近的三数之和 (3Sum Closest)
链接：https://leetcode.cn/problems/3sum-closest/
难度：中等
标签：数组、双指针、排序

思路：
1.先对数组进行排序，利用单调性方便双指针移动。
2.固定一个数 nums[i]，在其右侧用双指针 left 和 right 夹逼寻找最接近 target 的两数之和。
3.每次计算三数之和 s，更新全局最接近值 closest。
4.若 s == target，直接返回 target。
5剪枝：
1.若当前固定元素能组成的最小三数之和 min_sum 已经大于 target，则后续组合只会更大，更新 closest 后直接 break。
2.若当前固定元素能组成的最大三数之和 max_sum 已经小于 target，则当前固定元素下最接近的就是 max_sum，更新 closest 后 continue。

时间复杂度：O(n^2) —— 外层遍历 O(n)，内层双指针 O(n)。
空间复杂度：O(1) —— 不考虑排序所需的栈空间，仅用常数个变量。
"""


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        sorted_nums = sorted(nums)
        n = len(sorted_nums)
        closest = sum(sorted_nums[:3])
        for i in range(n - 2):
            # 剪枝，最小的三个数的和已经大于target，则break
            min_sum = sorted_nums[i] + sorted_nums[i + 1] + sorted_nums[i + 2]
            if min_sum > target:
                if abs(target - min_sum) < abs(target - closest):
                    closest = min_sum
                break
            # 剪枝，最大的三个数的和已经小于target，则continue
            max_sum = sorted_nums[i] + sorted_nums[n - 2] + sorted_nums[n - 1]
            if max_sum < target:
                if abs(target - max_sum) < abs(target - closest):
                    closest = max_sum
                continue
            left, right = i + 1, n - 1
            while left < right:
                s = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                if abs(target - closest) > abs(target - s):
                    closest = s
                if s == target:
                    return s
                elif s > target:
                    right -= 1
                else:
                    left += 1
        return closest
