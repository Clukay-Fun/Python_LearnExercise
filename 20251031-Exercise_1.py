'''
练习 1：封装回文判断函数（中级）
题目：
编写一个函数 is_palindrome(s)，接收一个字符串，返回 True 或 False，判断是否为回文（忽略大小写和空格）。
要求：

函数名必须为 is_palindrome
忽略大小写和所有空格
使用切片或循环均可

示例：
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("race a car"))                  # False
print(is_palindrome("No lemon no melon"))           # True

提示：
s = s.lower().replace(" ", "")  # 去空格 + 小写
'''

def is_palindrome(s):
    text = s.lower().replace(' ', '')
    reversed_str = text[::-1] #使用切片反转
    is_palindrome = text == reversed_str #一次比较
    return is_palindrome

print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("race a car"))                  # False
print(is_palindrome("No lemon no melon"))           # True