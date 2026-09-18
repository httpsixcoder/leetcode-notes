"""
题目：18. 四数之和 (4Sum)
链接：https://leetcode.cn/problems/4sum/
难度：中等
标签：数组、双指针、排序

思路：
1. 先对数组进行排序，利用单调性方便去重和指针移动。
2. 使用两层循环分别固定前两个数 nums[i] 和 nums[j]。
3. 在剩余区间内使用双指针 left 和 right 夹逼寻找 target - nums[i] - nums[j]。
4. 每层循环都进行剪枝：
   - 最小值剪枝：如果当前区间最小的组合都大于 target，说明后面更大，直接 break 结束当前循环。
   - 最大值剪枝：如果当前区间最大的组合都小于 target，说明当前元素太小，直接 continue 跳过。
   - 去重剪枝：遇到与上一个相同的元素，直接跳过。
5. 在内层双指针找到答案后，左右指针都要跳过所有重复元素。

时间复杂度：O(n^3) —— 两层循环 O(n^2)，内层双指针 O(n)，总共 O(n^3)。
空间复杂度：O(1) —— 不考虑排序所需的栈空间和结果数组，仅用常数个变量。
"""


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        sort_num = sorted(nums)
        res = []
        n = len(sort_num)
        fir = 0
        while fir < n - 3:
            # 剪枝min
            min_all = sort_num[fir] + sort_num[fir + 1] + sort_num[fir + 2] + sort_num[fir + 3]
            if min_all > target:
                break
            # 剪枝max 并且去重
            max_all = sort_num[fir] + sort_num[n - 1] + sort_num[n - 2] + sort_num[n - 3]
            if max_all < target or (fir > 0 and sort_num[fir] == sort_num[fir - 1]):
                fir += 1
                continue
            sec = fir + 1
            while sec < n - 2:
                # 剪枝min
                min_all = sort_num[fir] + sort_num[sec] + sort_num[sec + 1] + sort_num[sec + 2]
                if min_all > target:
                    break
                # 剪枝max 并且去重
                max_all = sort_num[fir] + sort_num[sec] + sort_num[n - 1] + sort_num[n - 2]
                if max_all < target or (sec > fir + 1 and sort_num[sec] == sort_num[sec - 1]):
                    sec += 1
                    continue
                left = sec + 1
                right = n - 1
                while left < right:
                    s = sort_num[fir] + sort_num[sec] + sort_num[left] + sort_num[right]
                    if s == target:
                        res.append([sort_num[fir], sort_num[sec], sort_num[left], sort_num[right]])
                        # 去重
                        while left < right and sort_num[left] == sort_num[left + 1]:
                            left += 1
                        # 去重
                        while right > right and sort_num[right] == sort_num[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif s > target:
                        right -= 1
                    else:
                        left += 1
                sec += 1
            fir += 1
        return res
        # return list(set(res))  # res里面的每一个元素都是list是不可哈希的，所以会报错
