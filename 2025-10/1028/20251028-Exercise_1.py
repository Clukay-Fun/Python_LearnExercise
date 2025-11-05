# 练习 1：列表去重并保留顺序
'''
题目描述：
编写一个程序，提示用户输入一串用逗号分隔的单词（如 "apple,banana,apple,cherry"），将其转换为列表并去重但保留首次出现的顺序，最后输出去重后的列表。
要求：

使用 input() 获取输入。
使用 split(",") 分割字符串为列表。
不能使用 set（因为 set 会打乱顺序）。
输出格式：去重后的列表：['apple', 'banana', 'cherry']

提示：

使用一个空列表 seen 记录已出现的元素。
遍历原列表，只添加不在 seen 中的元素，并加入 seen。
'''
seen = []
lst = []
str1 = str(input())
seen = str1.split(",")
# apple,banana,apple,cherry
len1 = len(seen)
for i in range(len(seen)):
    for y in seen[i:len1]:
        print(y)
print(lst)
    
# 答案

# 获取用户输入
raw = input("请输入单词（用逗号分隔）：")

# 用逗号分割成列表
words = raw.split(",")

# 去重并保持首次出现顺序
seen = []          # 用来记录已经出现过的元素
unique = []        # 去重后的结果列表

for w in words:
    # 去掉首尾空格（防止 "apple " 与 "apple" 被视为不同）
    w = w.strip() # 去除每个单词前后可能的多余空格
    if w not in seen:          # 只在第一次出现时加入
        seen.append(w)
        unique.append(w)

# 输出
print(f"去重后的列表：{unique}")
