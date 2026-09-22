"""
题目：75. 颜色分类 (Sort Colors)
链接：https://leetcode.cn/problems/sort-colors/
难度：中等
标签：数组、双指针、排序

思路：
1. 本题要求原地对包含 0、1、2 的数组排序，且不能使用库排序函数。
2. 方法一：库函数排序。直接调用 nums.sort()，面试中通常不允许使用。
3. 方法二：冒泡排序。双重循环，每次比较相邻元素并交换，时间复杂度 O(n²)，仅作对比。
4. 方法三：计数排序。先统计 0、1、2 各自出现的次数，再按次数重新填充数组。
5. 方法四：三个指针（荷兰国旗问题，推荐）。
   - 维护三个指针：left（0 区右边界）、mid（当前遍历位置）、right（2 区左边界）。
   - 当 nums[mid] == 0：与 nums[left] 交换，left++，mid++。
   - 当 nums[mid] == 1：mid++。
   - 当 nums[mid] == 2：与 nums[right] 交换，right--（注意：不移动 mid，交换过来的元素还需判断）。

时间复杂度：O(n) —— 三个指针仅遍历一次数组。
空间复杂度：O(1) —— 原地修改，只使用常数个额外变量。
"""


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        # 排序
        # nums.sort()
        # 冒泡
        # n=len(nums)
        # for i in range(n):
        #     for j in range(n-1):
        #         if nums[j]>nums[j+1]:
        #             nums[j],nums[j+1]=nums[j+1],nums[j]
        # 计数
        # a=nums.count(0)
        # b=nums.count(1)
        # c=len(nums)-a-b
        # for i in range(len(nums)):
        #     if i<a:
        #         nums[i]=0
        #     elif i<a+b:
        #         nums[i]=1
        #     else:
        #         nums[i]=2
        # 先找0再找2
        # left=0
        # right=len(nums)-1
        # while left <right:
        #     while left<right and nums[left]==0:
        #         left+=1
        #     while left <right and nums[right]!=0:
        #         right-=1
        #     nums[left],nums[right]=nums[right],nums[left]
        # left=0
        # right=len(nums)-1
        # while left <right:
        #     while left<right and nums[left]!=2:
        #         left+=1
        #     while left <right and nums[right]==2:
        #         right-=1
        #     nums[left],nums[right]=nums[right],nums[left]
        # 三指针
        left = 0
        mid = 0
        right = len(nums) - 1
        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                mid += 1
                left += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1
        # 三指针模板
        """
        low, mid, high = 0, 0, n - 1
        while mid <= high:
            if nums[mid] == 0:
                swap(low, mid); low += 1; mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                swap(mid, high); high -= 1
        """

