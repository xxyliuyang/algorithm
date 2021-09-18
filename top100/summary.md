### 1, 滑动窗口
- L3，求最长的不重复子串
- 一般针对数组：left，right两个标识窗口；需要控制left和right的变化，以及变化后的对应状态的改变。


### 2，字符ascll码控制
- 主要是一种hash隐射控制。

### 3，二分法
- 一般应对有序数组的问题
- 关注问题：a.满足二分的条件，状态；b. 注意边界条件（用几个case测一下）；。
- 如何返回：可以在while循环中判断返回，也可以循环结束返回。
- 固定写法：
`int left = 0, right = nums.size();
while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] <= target) left = mid + 1;
        else right = mid;
    }
    return right;`

#### 3.1 需查找和目标值完全相等的数：
- 比较简单：比如我们有数组 [2, 4, 5, 6, 9]，target = 6
- 条件：nums[mid] == targe
- left = mid + 1; right = mid;
- 若 right 初始化为了 nums.size()，那么就必须用 left < right，而最后的 right 的赋值必须用 right = mid。
但是如果我们 right 初始化为 nums.size() - 1，那么就必须用 left <= right，并且right的赋值要写成 right = mid - 1，不然就会出错。

#### 3.2  查找第一个不小于目标值的数，可变形为查找最后一个小于目标值的数：
- 条件：if (nums[mid] < target) left = mid + 1;else right = mid;

#### 3.3  用子函数当作判断关系（通常由 mid 计算得出）
#### 3.4 其他（通常 target 值不固定）

        
