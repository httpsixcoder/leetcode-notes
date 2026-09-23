"""
题目：80. 删除有序数组中的重复项 II (Remove Duplicates from Sorted Array II)
链接：https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/
难度：中等
标签：数组、双指针

思路：
1. 数组有序，重复元素相邻，要求每个元素最多出现两次。
2. 方法一：暴力删除。遍历数组，若连续相同元素超过2个，则从第3个开始删除，时间复杂度 O(n²)，不推荐。
3. 方法二：快慢指针（推荐）。
   - 若数组长度 ≤ 2，直接返回原长度。
   - slow 指向已处理好的数组末尾（初始为2），fast 从索引2开始遍历。
   - 当 nums[fast] != nums[slow-2] 时，说明当前元素未超过两次，将其复制到 slow 位置，slow 后移。
   - 最终 slow 即为新数组长度。

时间复杂度：O(n) —— 快指针遍历一次数组。
空间复杂度：O(1) —— 原地修改，只使用常数个额外变量。
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # 有序，相邻相同元素大于2删除，否则遍历下一个元素
        # sta=0
        # while True:
        #     if sta>=len(nums)-2:
        #         return len(nums)
        #     end=sta+1
        #     while end<len(nums) and nums[sta]==nums[end]:
        #         end+=1
        #     if end-sta<=2:
        #         sta+=1
        #     else :
        #         for i in range(end-sta-2):
        #             del nums[sta]
        #         sta+=2
        # 快慢指针
        # 剪枝
        if len(nums) <= 2:
            return len(nums)
        slow = 2
        for fast in range(2, len(nums)):
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
        return slow
