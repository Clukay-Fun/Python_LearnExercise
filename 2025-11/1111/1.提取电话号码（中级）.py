'''
练习 1：提取电话号码（中级）
题目描述：
编写一个函数 extract_phones(text)，从一段文本中提取所有电话号码（格式：123-456-7890 或 (123) 456-7890），返回电话号码列表。
'''

import re
def extract_phones(text):
    pattern = re.compile(r'\(\d{3}\)\s\d{3}-\d{4}|\d{3}-\d{3}-\d{4}')
    result = pattern.findall(text)
    return result

text = "Contact: 123-456-7890 or (987) 654-3210, not 12-34-567"
print(extract_phones(text))  # ['123-456-7890', '(987) 654-3210']

'''
改进点
1.添加 try-except：捕获 TypeError（如 text=None）和AttributeError。
2.优化正则表达式：使用 (?:...) 分组，允许 (123)456-7890（空格可选）。
3.返回空列表在异常情况下。
'''
#改进后代码
import re
def extract_phones(text):
    try:
        pattern = re.compile(r'(?:\d{3}-\d{3}-\d{4}|\(\d{3}\)\s?\d{3}-\d{4})')
        return re.findall(pattern, text)
    except (TypeError, AttributeError):
        print("输入必须是字符串")
        return []

# 测试
text = "Contact: 123-456-7890 or (987) 654-3210, not 12-34-567"
print(extract_phones(text))  # ['123-456-7890', '(987) 654-3210']
