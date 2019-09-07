"""
题目 二、：最长公共前缀 https://leetcode-cn.com/explore/interview/card/bytedance/242/string/1014/
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
"""
# 方法一：zip+set函数
def longestCommonPrefix(str):
    """
    :param str:
    :return: res,最长公共前缀
    :solution idea:zip()函数将对象中对应位置的函数，打包成元组，利用len(set())给出元素数目，==1说明有重复元素，元素为1个
    :example:
        s = ["flower","flow","flight"]
        a = zip(*s)
        a为一个zip object，可用list将a转换为列表。
        print(list(a)) # [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
        set(a[0]) == 1
    : Evaluation:此方法为最高效率方式
    """
    res = ""
    if len(str)==0:
        return ""
    for i in zip(*str):
        if len(set(i)) == 1:
            res += i[0]
        else:
            return res
    return res
"""
input:
print(set(i), i)

output:
{'f'} ('f', 'f', 'f')
{'l'} ('l', 'l', 'l')
"""

# leetcode最优方式：
"""
解题思路：
通过使用find()函数，将字符串从右向左依次寻找是否有子串
"""
def longestCommonPrefix_leetcode(str):
    if len(str) == 0: return ""
    prefix = str[0]
    for i in range(1,len(str)):
        while str[i].find(prefix) !=0:
            prefix = prefix[::-1]
            if len(prefix) == 0: return ''
    return prefix

# 方法二：enumerate
def longestCommonPrefix2(str):
    """
    :solution idea：enumerate()函数解决
    :参考链接：https://blog.csdn.net/chenhua1125/article/details/80542344
    """
    res = ""
    if len(str)==0:
        return ""
    s1 = min(str)
    s2 = max(str)
    for i,c in enumerate(s1):
        if c!=s2[i]:
            return s1[:i]
    return print(s2)


def main():
    s2 = ["flower","flow","flight"]
    print(longestCommonPrefix(s2))  # zip()实现
    print(longestCommonPrefix2(s2)) # enumerate()实现


if __name__ == '__main__':
    main()