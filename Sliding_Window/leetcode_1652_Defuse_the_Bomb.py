"""
题目：1652. 拆炸弹 (Defuse the Bomb)
链接：https://leetcode.cn/problems/defuse-the-bomb/
难度：简单
标签：数组、滑动窗口

思路：
根据 k 的符号分三种情况处理：
k == 0：返回全 0 数组。
k > 0：对每个位置 i，计算其后 k 个元素之和。
k < 0：对每个位置 i，计算其前 |k| 个元素之和。
使用滑动窗口优化：先计算第一个窗口的和，之后每次移动窗口时，加上新进入的元素，减去离开的元素。
由于数组是环形的，索引通过取模运算 (i + k + 1) % n 和 (i + 1) % n 处理越界。
时间复杂度 O(n)，空间复杂度 O(n)（结果数组）。

时间复杂度：O(n) —— 只需遍历一次数组，每个窗口的和更新为 O(1)。
空间复杂度：O(n) —— 需要返回长度为 n 的结果数组。
"""


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # 方法一：
        # n = len(code)
        # res = [0] * n
        # temp = code + code
        # if k == 0:
        #     return [0] * n
        # elif k > 0:
        #     for i in range(n):
        #         res[i] = sum(temp[i + 1:i + k + 1])
        # else:
        #     for i in range(n):
        #         if i + k > 0:
        #             res[i] = sum(temp[i + k:i])
        #         else:
        #             res[i] = sum(temp[n + i + k:n + i])
        # return res
        # 方法二
        # n = len(code)
        # if k == 0:
        #     return [0] * n
        # elif k > 0:
        #     temp = code + code
        #     for i in range(n):
        #         code[i] = sum(temp[i + 1:i + 1 + k])
        # else:
        #     temp = code + code
        #     for i in range(n, n * 2):
        #         code[i - n] = sum(temp[i + k:i])
        # return code
        # 方法三 滑动窗口
        n = len(code)
        if k == 0:
            return [0] * n
        res = [0] * n
        if k > 0:
            window_sum = sum(code[1:k + 1])
            for i in range(n):
                res[i] = window_sum
                window_sum += code[(i + k + 1) % n] - code[(i + 1) % n]
        else:
            m = -k
            window_sum = sum(code[n - m:])
            for i in range(n):
                res[i] = window_sum
                window_sum += code[i % n] - code[(i - m) % n]
        return res
