'''
练习 1：读取文件并统计单词（中级）
题目描述：
编写一个函数 count_words(filename)，读取一个文本文件（假设文件内容是英文句子），统计每个单词出现的次数，返回一个字典。忽略大小写，单词以空格分隔。
要求：

函数接收文件名（如 "input.txt"）。
使用 with open() 读取文件。
返回字典：键是单词，值是出现次数。
使用 try-except 处理文件不存在的情况。
测试文件内容（新建 input.txt）：
Hello world
This is a hello world example

示例：
result = count_words("input.txt")
print(result)  # {'hello': 2, 'world': 2, 'this': 1, 'is': 1, 'a': 1, 'example': 1}

提示：
使用 file.read().lower().split() 分割单词。
用字典存储计数：word_dict[word] = word_dict.get(word, 0) + 1。
捕获 FileNotFoundError。
'''
word_dict = {}
def count_words(filename):
    with open(filename,'r',encoding='utf-8') as file:
        try:
            for line in file:
                words = line.strip().lower().split()
                for word in words:
                    word_dict[word] = word_dict.get(word,0)+1
        except FileNotFoundError:
            print("文件不存在")
    return dict(sorted(word_dict.items(),key=lambda x:x[1], reverse=True))
result = count_words("G:/.Program/Python/Python_LearnExercise-1/2025-11/input.txt")        
print(result)

'''改进点
将 word_dict 移到函数内，避免全局变量问题。
在 FileNotFoundError 时返回空字典，增加健壮性。
移除排序，简化代码（但如果你想保留排序，可以用 sorted()）。
使用相对路径 "input.txt"，更通用。。
'''

#改进后的代码
def count_words(filename):
    word_dict = {}  # 定义在函数内
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.strip().lower().split()
                for word in words:
                    word_dict[word] = word_dict.get(word, 0) + 1
    except FileNotFoundError:
        print("文件不存在")
        return {}  # 返回空字典
    return word_dict  # 按题目要求直接返回字典

result = count_words("input.txt")
print(result)