<!--
 * @Author: shaqsnake
 * @Email: shaqsnake@gmail.com
 * @Date: 2019-09-16 15:58:00
 * @LastEditTime: 2019-10-18 18:57:37
 * @Description: Acwing 850
 -->

# 853. 有边数限制的最短路

## 题目

给定一个n个点m条边的有向图，图中可能存在重边和自环， 边权可能为负数。

请你求出从1号点到n号点的最多经过k条边的最短距离，如果无法从1号点走到n号点，输出impossible。

注意：图中可能 存在负权回路 。

#### 输入格式

第一行包含三个整数n，m，k。

接下来m行，每行包含三个整数x，y，z，表示存在一条从点x到点y的有向边，边长为z。

#### 输出格式

输出一个整数，表示从1号点到n号点的最多经过k条边的最短距离。

如果不存在满足条件的路径，则输出“impossible”。

#### 数据范围

![](http://latex.codecogs.com/gif.latex?\\1%20\leq%20n,k%20\leq%20500),

![](http://latex.codecogs.com/gif.latex?\\1%20\leq%20n,m%20\leq%2010000),

任意边长的绝对值不超过10000。

#### 输入样例：

```
3 3 1
1 2 1
2 3 1
1 3 3
```

#### 输出样例：

```
3
```

## 题解

### Bellman-Ford

此题因为存在负权边，所以首先排除Dijkstra算法，同时因为是求有限边k下的最短路，所以用Bellman-Ford算法。

Bellman-Ford算法的过程如下：

1. 先和Dijkstra算法一样保存好所有边和边的权重，比如(a, b, w)表示从a点到b点边权重为w，并用一个数组d[1..n]来表示从起点到每个点的距离，初始时d[1] = 0, d[2..n] = +∞;
2. 如果要求有限边数为k，那就循环k次;
3. 每次循环时遍历所有边更新数组d[1.。n]中的距离，比如边(a, b, w) 满足条件 d[b] > d[a] + w 时，应该更新 d[b] = d[a] + w（松弛操作）;

最终d[n]就表示从起点1到终点n经过k条边的最短路径，注意如果d[n]的值如果变化很小仍接近+∞，我们可以认为不存在最短路径。
