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
str1 = str(input())
seen = str1.split(",")
x = 0
# 遍历一遍所有字符串
for i in seen:
    # 比较一遍剩余字符串，统计重复的字符串位置
    for y in range(len(seen)):
        
        print(i)
while 1:
    num = 0
    
    break