# 练习 1：字符串反转与检查（初级）
'''
题目描述：
编写一个程序，提示用户输入一个字符串，判断该字符串是否是回文（正读反读相同，如 "radar"），并打印反转后的字符串。

要求：

1. 使用 input() 获取用户输入。
2. 打印反转后的字符串。
3. 判断是否为回文（忽略大小写）。
4. 输出结果格式为："反转后的字符串是：{reversed_str}，是否回文：{is_palindrome}"。
'''

input1 = input().lower()
reversed_str = ""
for i in range(len(input1)):
    reversed_str += input1[-(i+1)]
    if reversed_str == input1:
        is_palindrome = True
print(f"反转后的字符串是：{reversed_str}，是否回文：{is_palindrome}")

'''
问题：
变量名冲突：

你使用了 input 作为变量名，这会覆盖 Python 内置的 input() 函数，导致后续无法调用 input()。建议使用更具体的变量名，如 text 或 s。


回文判断逻辑错误：

在循环中，if reversed_str == input 会在每次迭代检查是否回文，但 reversed_str 是一个逐步构建的字符串，只有最后一次迭代才完整。此时，is_palindrome 可能未定义（如果字符串不是回文，会导致 NameError）。
正确的回文判断应该在反转完成后一次性比较。


未初始化 is_palindrome：

如果输入字符串不是回文，is_palindrome 不会被赋值，运行时会抛出 NameError: name 'is_palindrome' is not defined。


效率问题：

使用 reversed_str += input[-(i+1)] 每次拼接字符串会创建新字符串，效率较低（字符串是不可变的，拼接是 O(n) 操作）。
Python 提供更高效的方法（如切片 [::-1]）来反转字符串。
'''

# 改进后代码
text = input("请输入字符串：").lower()
reversed_str = text[::-1] #使用切片反转
is_palindrome = text == reversed_str #一次比较
print(f"反转后的字符串是：{reversed_str}，是否回文：{is_palindrome}")
