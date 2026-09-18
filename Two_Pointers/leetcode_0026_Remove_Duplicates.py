"""
题目：26. 删除有序数组中的重复项 (Remove Duplicates from Sorted Array)
链接：https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
难度：简单
标签：数组、双指针

思路：
1. 数组是非严格递增排列的，因此重复元素一定相邻。
2. 使用快慢指针（slow 和 fast）：
   - slow 指向当前已经去重后的最后一个元素的位置。
   - fast 负责遍历整个数组。
3. 当 nums[fast] != nums[slow] 时，说明遇到了一个新的不重复元素，
   将 nums[fast] 复制到 nums[slow + 1] 的位置，然后 slow 向后移动一位。
4. 遍历结束后，slow + 1 即为去重后数组的新长度 k。
5. 题目要求原地修改，不需要考虑数组中超出新长度后面的元素。

时间复杂度：O(n) —— fast 指针遍历一次数组，n 为数组长度。
空间复杂度：O(1) —— 只使用了常数个额外变量，原地修改。
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for fast in range(1, len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
