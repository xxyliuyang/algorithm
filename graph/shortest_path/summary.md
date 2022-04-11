图最短路径算法：https://leetcode-cn.com/problems/network-delay-time/solution/dirkdtra-by-happysnaker-vjii/
https://blog.csdn.net/nuist_NJUPT/article/details/123371850?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EOPENSEARCH%7ERate-1.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EOPENSEARCH%7ERate-1.pc_relevant_default&utm_relevant_index=2

### 1, 单源算法 ——Dirkdtra 算法
https://chinese.freecodecamp.org/news/dijkstras-shortest-path-algorithm-visual-introduction/
- Dijkstra 算法从指定的节点（源节点）出发，寻找它与图中所有其它节点之间的最短路径。
###### 算法过程
- Dijkstra 算法会记录当前已知的最短路径，并在寻找到更短的路径时更新。
- 一旦找到源节点与其他节点之间的最短路径，那个节点会被标记为 “已访问” 并添加到路径中。
- 重复寻找过程，直到图中所有节点都已经添加到路径中。这样，就可以得到从源节点出发访问所有其他节点的最短路径方案。

###### 数据结构
- 图表示
- 源点到其他点的距离数组
- 未访问点的集合


