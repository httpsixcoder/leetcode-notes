# 双指针（更新中......）Two_Pointers（Updating......）

*文档包含汉字和转义英文两个版本，请你选择合适的详细查看（英文版在文档尾部）*

*The document contains both Chinese characters and translated English versions. Please choose the appropriate one for detailed review (the English version is at the end of the document)*



## 个人定义：

通常在序列中的首尾各添加一个指针，两端操作序列，相互移动靠近，往往是多层嵌套循环的优化解法。

## 适用题型：

在有序的序列中需要操作多个元素，正常解法一般是暴力破解，极其耗时。此时考虑双指针

## 使用注意：

一定先排序！注意判断条件的选择，双指针迭代的边界问题，如果是多个数据需要固定一个数据，操作其他数据以达到更好的效果。

## 代表题目：

### LeetCode：

[88. 合并两个有序数组](https://leetcode.cn/problems/merge-sorted-array/)

[15. 三数之和](https://leetcode.cn/problems/3sum/)

## 错题本：

### [15. 三数之和](https://leetcode.cn/problems/3sum/)【双指针使用前需要排序】

```python
while left<right:
    s=temp[left]+temp[right]+temp[v]
    if s==0:
        res.append([+temp[v],temp[left],temp[right]])
        while left<right and temp[left]==temp[left+1]:
            left+=1
        while left<right and temp[right]==temp[right-1]:
            right-=1
        left+=1
        right-=1
    elif s<0:
        left+=1
    else:
        right-=1
```

优化：巧用0，一般遍历到固定元素大于0，则可以直接结束

陷阱：重复元素添加到答案中，指针越界





------



## Personal definition:

Usually, a pointer is added at the beginning and end of the sequence, and the two ends operate on the sequence, moving closer to each other. This is often an optimized solution for multi-layer nested loops.

## Applicable question types:

When multiple elements need to be operated in an ordered sequence, the normal solution is usually brute force, which is extremely time-consuming. At this time, consider using double pointers

## Usage Notes:

Sorting must be done first! Pay attention to the selection of judgment conditions, the boundary issues of double-pointer iteration, and if there are multiple data points, fix one data point while operating on the other data points to achieve better results.

## Representative topic:

### LeetCode：

[88. Merge Two Sorted Arrays](https://leetcode.cn/problems/merge-sorted-array/)

[15. Three Sum](https://leetcode.cn/problems/3sum/)

## Error Log:

### [15. 三数之和](https://leetcode.cn/problems/3sum/)【The double pointer needs to be sorted before use】

```python
while left<right:
    s=temp[left]+temp[right]+temp[v]
    if s==0:
        res.append([+temp[v],temp[left],temp[right]])
        while left<right and temp[left]==temp[left+1]:
            left+=1
        while left<right and temp[right]==temp[right-1]:
            right-=1
        left+=1
        right-=1
    elif s<0:
        left+=1
    else:
        right-=1
```

Optimization: Make clever use of 0. Generally, if the fixed element encountered during traversal is greater than 0, the process can be directly terminated

Trap: Duplicate elements are added to the answer, causing pointer overflow
