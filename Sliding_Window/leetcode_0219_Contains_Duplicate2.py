"""
题目：219. 存在重复元素 II (Contains Duplicate II)
链接：https://leetcode.cn/problems/contains-duplicate-ii/
难度：简单
标签：数组、哈希表、滑动窗口

思路：
1. 需要在数组中找到两个相同的元素，且它们的下标差不超过 k。
2. 方法一：哈希表。遍历数组，用字典记录每个元素最近一次出现的下标。如果当前元素已在字典中且下标差 ≤ k，返回 True；否则更新下标。
3. 方法二：定长滑动窗口（推荐）。维护一个大小为 k 的 set 窗口，遍历数组：
   - 若当前元素已在窗口内，说明存在满足条件的重复元素，返回 True。
   - 将当前元素加入窗口。
   - 若窗口大小超过 k，移除窗口最左侧的元素（下标 i - k）。

时间复杂度：O(n) —— 遍历一次数组，set 的查找、添加、删除平均 O(1)。
空间复杂度：O(k) —— 窗口大小最多为 k + 1。
"""


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # 滑动窗口
        win = set()
        for i, v in enumerate(nums):
            if v in win:
                return True
            win.add(v)
            if i >= k:
                win.remove(nums[i - k])
        return False
        # hash表字典
        dict1 = {}
        for i, v in enumerate(nums):
            if v in dict1 and i - dict1[v] <= k:
                return True
            dict1[v] = i
        return False
