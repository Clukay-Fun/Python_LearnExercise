'''
练习 1：提取电话号码（中级）
题目描述：
编写一个函数 extract_phones(text)，从一段文本中提取所有电话号码（格式：123-456-7890 或 (123) 456-7890），返回电话号码列表。

要求：
1.使用 re 模块的正则表达式。
2.处理两种格式：XXX-XXX-XXXX 和 (XXX) XXX-XXXX。
3.返回列表，若无电话号码返回空列表。
4.使用 try-except 捕获潜在错误（如无效输入）。

示例：
text = "Contact: 123-456-7890 or (987) 654-3210, not 12-34-567"
print(extract_phones(text))  # ['123-456-7890', '(987) 654-3210']

提示：
- 正则表达式：r'\(\d{3}\)\s\d{3}-\d{4}|\d{3}-\d{3}-\d{4}'
- 使用 re.findall(pattern, text)。
'''

import re
def extract_phones(text):
    pattern = re.compile(r'\(\d{3}\)\s\d{3}-\d{4}|\d{3}-\d{3}-\d{4}')
    result = pattern.findall(text)
    return result

text = "Contact: 121212121xxx21212121"
print(extract_phones(text))  # ['123-456-7890', '(987) 654-3210']