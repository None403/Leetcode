

"""
题目四、字符串相乘

给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
"""

"""
java参考链接:https://www.youtube.com/watch?v=q3vpdwWR0ag

"""


def multiply(num1,num2):
    return str(str2int(num1) * str2int(num2))

def str2int(s):
    s = s[::-1]
    num = 0
    for i,v in enumerate(s):
        offset = ord(v) - ord('0') # str转int
        num += offset * (10 ** i)
    return num

# 方法二： leetcode最优方式
# def multiply(num1,num2):
#     return str(int(num1) * int(num2))


def main():
    n1,n2 = '13','11'
    print(multiply(n1,n2))


if __name__ == '__main__':
    main()