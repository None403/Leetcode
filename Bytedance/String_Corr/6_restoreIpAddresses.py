"""
题目六、复原IP地址

给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
"""
# def restoreIpAddresses(s):
#     res = []
#     def isval(s):
#         a = int(s)
#         # a在（0，255]内，且len(s)==1 保证没有单个0的出现；a在（0，255]内，且s[0]!='0',保证没有01，001，011的情况出现
#         if 0<=a<=255 and (len(s)==1 or s[0]!='0'):
#         # if 0 <= int(a) <= 255 and str(a) == s:
#             return True
#         return False
#
#     def dfs(a,s,k): # a存num+.   s存储str、k存 第几个 .
#         # k==3,判断s被划分后的最后一个. 后的数值，是否符合要求，符合，则append()到res列表中
#         if k==3:
#             if isval(s):
#                 res.append(a+s)
#             return
#         else:
#             for i in range(1,min(4,len(s))): # min(4,len(s)) 的目的是，len(s) >=4的范围内，即起码为1.1.1.1四个数，才能被三个.划分为ip地址
#                 tmp=s[:i]
#                 if isval(tmp):
#                     dfs(a+tmp+'.',s[i:],k+1)
#     dfs('',s,0)
#     return res

"""
Leetcode较优代码

运行内存：48ms
"""

def restoreIpAddresses_leetcode(s):
    def dfs(results, res, s, level):
        # print(results,s)
        if len(s) == 0 and level == 4:
            results.add(".".join(res))  # add()用于给集合添加元素
            return  None
        if level >= 4:  # 超出4段ip的话就跳过
            return None
        for i in range(1, 4):  # 每个ip地址最多三位数字
            if s[:i] != "" and 0 <= int(s[:i]) <= 255:  # 保证每段ip不为空 且在0-255
                if len(s[:i]) >= 2 and s[0] == "0": continue  # 保证每段ip没有 01.011.010这样的
                dfs(results, res + [s[:i]], s[i:], level + 1)

    results = set() # 创建无序不重复元素集
    dfs(results, [], s, 0)
    return list(results)    # set()集合转list


def main():
    s1 = '25002102'
    # print(restoreIpAddresses(s1))
    print(restoreIpAddresses_leetcode(s1))


if __name__ == '__main__':
    main()

#
# 六、五写完
# 上传github
# bert代码，例子看完。
# 李彦宏、异常检测视频，学习完。公众号。
#
# Question?
# 1. 什么时候用回溯法、
# 2. 什么时候用窗口滑动法

