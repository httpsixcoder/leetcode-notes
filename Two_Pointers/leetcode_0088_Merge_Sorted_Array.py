"""
题目：88. 合并两个有序数组 (Merge Sorted Array)
链接：https://leetcode.cn/problems/merge-sorted-array/
难度：简单
标签：数组、双指针、排序

思路：
1. 从后往前遍历，避免覆盖 nums1 中尚未处理的元素。
2. 使用三个指针：end1 指向 nums1 有效部分的末尾（m-1），end2 指向 nums2 的末尾（n-1），end3 指向合并后的末尾（m+n-1）。
3. 每次比较 nums1[end1] 和 nums2[end2]，将较大者放到 nums1[end3] 位置，然后对应指针左移。
4. 循环结束条件是 end2 < 0，即 nums2 全部合并完成。此时如果 nums1 还有剩余，它们本身就在正确位置，无需处理。

时间复杂度：O(m + n) —— 每个元素最多被处理一次。
空间复杂度：O(1) —— 原地修改，只使用常数个额外变量。
"""


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        end1 = m - 1
        end2 = n - 1
        end3 = m + n - 1
        while end2 >= 0:
            if end1 >= 0 and nums1[end1] > nums2[end2]:
                nums1[end3] = nums1[end1]
                end1 -= 1
            else:
                nums1[end3] = nums2[end2]
                end2 -= 1
            end3 -= 1
