"""
题目：594. 最长和谐子序列 (Longest Harmonious Subsequence)
链接：https://leetcode.cn/problems/longest-harmonious-subsequence/
难度：简单
标签：数组、哈希表、滑动窗口、排序

思路：
方法一：哈希表统计频数（推荐）。遍历数组，用字典统计每个元素的出现次数。
然后遍历哈希表，对于每个元素 x，如果 x+1 也存在，则包含 x 和 x+1 的最长和谐子序列长度为
count[x] + count[x+1]。取所有可能的最大值即可。
方法二：排序 + 滑动窗口。先对数组排序，然后用双指针维护一个窗口，保证窗口内最大值与最小值之差不超过 1。
当差恰好为 1 时，窗口长度就是一个和谐子序列的长度，更新最大值。【遍历右侧，更新左侧】
方法三：双指针 + 集合（不推荐）。排序后对每个左端点向右扩展，用集合判断是否恰好两种元素，


时间复杂度：
哈希表法：O(n) —— 遍历一次数组统计频数，再遍历一次哈希表。
滑动窗口法：O(n log n) —— 排序 O(n log n)，滑动窗口 O(n)。
空间复杂度：
哈希表法：O(n) —— 存储不同元素的频数。
滑动窗口法：O(1) —— 不考虑排序所需的栈空间，仅用常数个变量。
"""


class Solution:
    def findLHS(self, nums: list[int]) -> int:
        # 哈希表
        dict1 = {}
        max_num = 0
        for i in nums:
            if i in dict1.keys():
                dict1[i] += 1
            else:
                dict1[i] = 1
        for i in dict1.keys():
            if i + 1 in dict1.keys():
                max_num = max(max_num, dict1[i + 1] + dict1[i])
        return max_num
        # 滑动窗口【遍历右侧，更新左侧】
        nums.sort()
        max_win = 0
        left = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > 1:
                left += 1
            if nums[right] - nums[left] == 1:
                max_win = max(max_win, right - left + 1)
        return max_win
        双指针
        if len(set(nums)) == 1:
            return 0
        max_len = 0
        nums.sort()
        for left in range(len(nums)):
            right = left + 1
            while right < len(nums) and nums[right] - nums[left] < 2:
                right += 1
            if len(set(nums[left:right])) == 2:
                max_len = max_len if max_len > right - left else right - left
        return max_len if max_len != 1 else 0
