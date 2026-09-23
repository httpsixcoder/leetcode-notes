"""
题目：283. 移动零 (Move Zeroes)
链接：https://leetcode.cn/problems/move-zeroes/
难度：简单
标签：数组、双指针

思路：
1. 要求原地将数组中的所有 0 移动到末尾，同时保持非零元素的相对顺序。
2. 方法一：暴力破解。左右指针交换，但逻辑复杂，容易出错，不推荐。
3. 方法二：快慢指针（瑕疵版）。尝试用 slow 和 fast 定位并交换，但边界条件较多，容易遗漏。
4. 方法三：双指针交换。slow 指向已处理好的非零区域末尾，fast 遍历数组，遇到非零元素就与 slow 交换，slow 后移。
5. 方法四：双指针覆盖（推荐）。slow 指向当前应放置非零元素的位置，fast 遍历数组，遇到非零元素就覆盖到 slow 位置，slow 后移；遍历结束后，将 slow 到末尾的元素全部置为 0。
   - 优点：不需要交换，减少赋值次数，思路更清晰。

时间复杂度：O(n) —— fast 遍历一次数组，slow 再遍历一次补零，总计 O(n)。
空间复杂度：O(1) —— 原地修改，只使用常数个额外变量。
"""


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        # 暴力破解
        left = 0
        right = len(nums) - 1
        while left < right:
            while left < right and nums[left] != 0:
                left += 1
            while left < right and nums[right] == 0:
                right -= 1
            if left == right:
                break
            del nums[left]
            nums.append(0)
        # 快慢指针【瑕疵】
        slow = 0
        fast = 0
        n = len(nums)
        while slow < n:
            while slow < n and nums[slow] != 0:
                slow += 1
            while fast < slow or (fast < n and nums[fast] == 0):
                fast += 1
            if fast == n or slow == n:
                break
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
            fast += 1
        # 双指针交换
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        # 双指针覆盖
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        for n in range(slow, len(nums)):
            nums[n] = 0
