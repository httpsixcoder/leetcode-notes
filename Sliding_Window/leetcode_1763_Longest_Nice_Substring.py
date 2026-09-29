"""
题目：1763. 最长的美好子字符串 (Longest Nice Substring)
链接：https://leetcode.cn/problems/longest-nice-substring/
难度：简单
标签：字符串、分治、滑动窗口、位运算

思路：
1. 美好子字符串的定义：对于子串中的每个字母，其大写和小写形式都同时出现在该子串中。
2. 方法一：暴力枚举所有子串，判断是否为美好子字符串，记录最长的一个。
3. 方法二：分治（推荐）。
   - 遍历字符串，若某个字符的大小写变体不在整个字符串中，则该字符一定不属于任何美好子字符串。
   - 以该字符为分隔符，将字符串分成左右两部分，递归求解。
   - 返回左右结果中更长的一个。
   - 若整个字符串中所有字符的大小写变体都存在，则整个字符串就是美好子字符串，直接返回。

时间复杂度：O(n log n) ~ O(n^2) —— 分治平均情况，最坏退化为 O(n^2)。
空间复杂度：O(n) —— 递归调用栈深度最多为 n。
"""


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        max_num = 0
        start = 0
        end = 0
        for left in range(len(s)):
            for right in range(len(s) - 1, left, -1):
                flag = True
                for c in set(s[left:right + 1]):
                    if c.swapcase() not in set(s[left:right + 1]):
                        flag = False
                        break
                if flag and len(s[left:right + 1]) > max_num:
                    max_num = len(s[left:right + 1])
                    start = left
                    end = right
        if start == 0 and end == 0:
            return ""
        return s[start:end + 1]
        # 分治
        if len(s) < 2:
            return ""
        chars = set(s)
        for i, c in enumerate(s):
            if c.swapcase() not in chars:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i + 1:])
                return left if len(left) >= len(right) else right
        return s
