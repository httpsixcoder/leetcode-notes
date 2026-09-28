"""
题目：3. 无重复字符的最长子串 (Longest Substring Without Repeating Characters)
链接：https://leetcode.cn/problems/longest-substring-without-repeating-characters/
难度：中等
标签：字符串、滑动窗口、哈希表

思路：【字典】
使用滑动窗口 [left, right] 维护当前无重复字符的子串。
用字典 last 记录每个字符最后出现的索引。
遍历字符串，right 为当前右指针：
如果当前字符 c 已经在窗口内出现过（即 last[c] >= left），说明窗口内出现了重复，
需要将 left 移动到重复字符的下一个位置，即 left = last[c] + 1。
更新 last[c] = right，记录当前字符最新出现的位置。
此时窗口 [left, right] 内无重复字符，长度为 right - left + 1，更新最大值 max_len。
遍历结束返回 max_len。

时间复杂度：O(n) —— 每个字符只被遍历一次，left 最多移动 n 次。
空间复杂度：O(min(n, 字符集大小)) —— 字典 last 最多存储所有不同字符。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口 + 集合（推荐）
        # max_win = 0
        # set1 = set()
        # l = 0
        # for r in range(0, len(s)):
        #     while s[r] in set1:
        #         set1.remove(s[l])
        #         l += 1
        #     set1.add(s[r])
        #     max_win = max(max_win, r - l + 1)
        # return max_win

        last = {}  # 字符 -> 最后出现的索引
        left = 0
        max_len = 0
        for right, c in enumerate(s):
            if c in last and last[c] >= left:
                left = last[c] + 1
            last[c] = right
            max_len = max(max_len, right - left + 1)

        return max_len
