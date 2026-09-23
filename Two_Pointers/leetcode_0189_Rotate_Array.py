"""
题目：189. 旋转数组 (Rotate Array)
链接：https://leetcode.cn/problems/rotate-array/
难度：中等
标签：数组、双指针、数学

思路：
1. 将数组中的元素向右轮转 k 个位置，要求原地修改。
2. 方法一：使用额外数组，将每个元素放到 (i+k)%n 的位置，空间 O(n)。
3. 方法二：三次反转法。先整体反转，再反转前 k 个，最后反转后 n-k 个。空间 O(1)，推荐。
4. 方法三：环状替换。从起点开始，每次将元素移到 (i+k)%n 的位置，循环 n 次，需处理循环节。
5. 方法四：利用 Python 切片扩展（本代码采用）。先将列表扩展为两倍，再通过删除多余部分得到旋转后的数组。
   - 时间复杂度 O(n)，空间复杂度 O(n)（扩展时临时占用 2n 空间）。
   - 代码简洁，但严格来说并非原地 O(1) 空间，适合 Python 快速实现。

时间复杂度：O(n) —— 扩展和删除操作均只遍历一次数组。
空间复杂度：O(n) —— 扩展列表时临时占用 2n 空间。
"""


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        if k % n == 0:
            return
        else:
            k = k if k < n else k % n
            # 超时
            for _ in range(k):
                nums.insert(0, nums.pop())
            # 反转
            nums.reverse()
            nums[:k] = reversed(nums[:k])
            nums[k:] = reversed(nums[k:])
            # 纯操作无反转切片
            nums.extend(nums)
            del nums[2 * n - k:]
            del nums[0:n - k]
