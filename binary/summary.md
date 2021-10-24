#### 二分法介绍
https://mp.weixin.qq.com/s?__biz=MzUxNjY5NTYxNA==&mid=2247488241&idx=2&sn=374ca9d153bf4f0c44da7601013cb180&chksm=f9a221a0ced5a8b6c7142e13b1d18cfb3c9dc407f152fd968d47cc42bd15dd0e5c483247692f&scene=178&cur_album_id=1485825793120387074#rd

#### 关键点
##### 1， 条件：
- 数组有序
- 是否有重复元素
- 关键点
    - while条件
    - right，left的变化
    - 返回值的状态

##### 2， 方法一：定义 target 是在一个在左闭右闭的区间里，也就是[left, right]
- while (left <= right) 要使用 <= ，因为left == right是有意义的，所以使用 <=
- if (nums[middle] > target) right 要赋值为 middle - 1，因为当前这个nums[middle]一定不是target，那么接下来要查找的左区间结束下标位置就是 middle - 1

##### 3， 方法二：定义 target 是在一个在左闭右开的区间里，也就是[left, right) 
- while (left < right)，这里使用 < ,因为left == right在区间[left, right)是没有意义的
- if (nums[middle] > target) right 更新为 middle，因为当前nums[middle]不等于target，去左区间继续寻找，而寻找区间是左闭右开区间，所以right更新为middle，即：下一个查询区间不会去比较nums[middle]