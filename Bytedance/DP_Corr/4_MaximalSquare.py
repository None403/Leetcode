"""
题目三、最大正方形

在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4


"""

"""
解题思路：

此题可用动态规划的思路进行

对于可构成最小正方形，形态为
1 1 
1 1

我们将以上最小正方形用dp[i][j]表示，则
1(dp[0][0]) 1(dp[0][1])
1(dp[1][0]) 1(dp[1][1])

当dp[1][1] = 1 时，我们需要判断在dp[1][1]上边、左边、以及前一行对角线上的元素最小值

1. 若都为1，则构成一个正方形，dp[1][1] = min(元素上，元素左，元素斜对角) + 1.依次递推

手动进行递推：

对于可构成的最小正方形，形态为：
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1

那么dp[i][j]应对应的值为：
第一次迭代：
1 1 1 1 
1 2 2 2
1 2 2 2
1 2 2 2
第二次迭代：
1 1 1 1
1 2 2 2
1 2 3 3
1 2 3 4
对角线上dp[i][j]对应的值，即代表构成正方形的最大边长
"""

def maximalSquare(matrix):
    if not matrix or not matrix[0]:
        return 0

    # 矩阵 行数rows，列数cols
    rows,cols = len(matrix), len(matrix[0])

    if rows==0 or cols==0:
        return 0
    if rows<2:
        return max(matrix[0])
    if cols<2:
        return max(matrix[r][0] for r in range(0,rows))

    max_side = 0                         # 用于记录matrix中最大正方形的边长
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = int(matrix[i][j])	# 直接在原矩阵上进行计算遍历
            if i and j and matrix[i][j]:
                matrix[i][j] = min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1]) + 1

            max_side = max(max_side,matrix[i][j])
    return max_side * max_side

    # dp = [[0]*cols for _ in range(rows)] # dp数组用于记录每个位置能够渠道的正方形的最大边长，与matrix矩阵大小相同


# leetcode运行优化后的代码
def maximalSquare_leetcode(matrix) -> int:
    imax = 0
    dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]	# 初始化dp，大小为m*n，值为0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '0': continue
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
            imax = max(imax, dp[i][j])
    # print(dp)
    return imax ** 2

def main():
    # m = [
    #     [1,0,1,0,0],
    #     [1,0,1,1,1],
    #     [1,1,1,1,1],
    #     [1,0,0,1,0],
    # ]
    m1 = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
    print(maximalSquare(m1))
    # print(maximalSquare_leetcode(m1))


if __name__ == '__main__':
    main()

