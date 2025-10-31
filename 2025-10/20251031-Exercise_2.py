'''
练习 2：用列表推导式过滤及转换（中级）
题目：
给定一个数字列表 nums = [1, -2, 3, -4, 5, 6, -7]，用 一行列表推导式 完成：

取出所有正数，并乘以 2，得到新列表

要求：

只能用 一行代码
不能用 for 循环
结果：[2, 6, 10, 12]

doubled_positives = [???]
'''
nums = [1, -2, 3, -4, 5, 6, -7]
doubled_positives = [x*2 for x in nums if x>0]
print(doubled_positives)