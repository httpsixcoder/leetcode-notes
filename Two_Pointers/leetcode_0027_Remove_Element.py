"""
题目：27. 移除元素 (Remove Element)
链接：https://leetcode.cn/problems/remove-element/
难度：简单
标签：数组、双指针

思路：
1. 本题要求原地移除数组中所有等于 val 的元素，并返回新的长度。
2. 方法一：快慢指针。slow 指向新数组末尾，fast 遍历数组，遇到不等于 val 的元素就复制到 slow 位置。
3. 方法二：左右双指针（交换法）。left 从前往后，right 从后往前，当 nums[left] == val 时用 nums[right] 覆盖它。
4. 方法三：暴力移除（不推荐，仅作对比）。循环调用 remove()，时间复杂度 O(n^2)。

时间复杂度：O(n) —— 每个元素最多被遍历一次。
空间复杂度：O(1) —— 原地修改，只使用常数个额外变量。
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 方法1：快慢指针
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow
        # 方法2：左右双指针（交换法）
        # left = 0
        # right = len(nums) - 1
        # while left <= right:
        #     if nums[left] == val:
        #         nums[left] = nums[right]
        #         right -= 1
        #     else:
        #         left += 1
        # return left
        # 方法3：移除每一个val（不推荐）
        # while val in nums:
        #     nums.remove(val)
        # return len(nums)
