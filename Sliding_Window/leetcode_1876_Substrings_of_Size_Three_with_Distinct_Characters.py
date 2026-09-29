"""
题目：1876. 长度为三且各字符不同的子字符串 (Substrings of Size Three with Distinct Characters)
链接：https://leetcode.cn/problems/substrings-of-size-three-with-distinct-characters/
难度：简单
标签：字符串、滑动窗口、哈希表

思路：
1. 遍历字符串中每个长度为 3 的子串，判断该子串内三个字符是否互不相同。
2. 方法一：暴力比较（推荐）。每次比较 s[right]、s[right-1]、s[right-2] 两两是否相等。
3. 方法二：集合去重。利用 set() 自动去重的特性，将子串转为集合。若集合长度为 3，说明三个字符各不相同。
4. 本题也可以理解为固定长度为 3 的滑动窗口，每次窗口右移一格，判断窗口内元素是否唯一。

时间复杂度：O(n) —— 遍历一次字符串，每次集合操作最多处理 3 个字符。
空间复杂度：O(1) —— 集合大小最多为 3，常数空间。
"""


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # 暴力破解
        res = 0
        for right in range(2, len(s)):
            if s[right] != s[right - 1] and s[right] != s[right - 2] and s[right - 1] != s[right - 2]:
                res += 1
        return res
        # 滑动窗口
        res = 0
        for i in range(len(s) - 2):
            if len(set(s[i:i + 3])) == 3:
                res += 1
        return res
        # 优雅 滑动窗口
        return sum(1 for i in range(len(s) - 2) if len(set(s[i:i + 3])) == 3)
