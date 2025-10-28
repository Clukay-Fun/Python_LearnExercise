# 练习 2：成绩等级分类（初级）
'''
题目描述：
编写一个程序，提示用户输入一个考试分数（0-100），根据分数输出对应的等级：

90-100：A
80-89：B
70-79：C
60-69：D
0-59：F

要求：
1. 使用 input() 获取用户输入，并转换为整数。
2. 使用 if-elif-else 判断等级。
3. 如果输入不在 0-100 范围内，输出“无效分数”。

提示：
- 使用 int() 转换输入为整数。
- 检查输入是否在有效范围内（0 ≤ score ≤ 100）。
- 使用多条件判断实现等级划分。
'''
level = ""
input1 = 0
input1 = int(input("请输入分数："))
if(100 >= input1 >= 90):
    level = "等级：A"
elif(89 >= input1 >= 80):
    level = "等级：B"
elif(79 >= input1 >= 70):
    level = "等级：C"
elif(69 >= input1 >= 60):
    level = "等级：D"
elif(59 >= input1 >= 0):
    level = "等级：F"
else:
    level = "无效分数"
print(level)

'''
问题

变量名冲突：

使用 input1 作为变量名，虽然没问题，但 input 是 Python 内置函数名，容易让人误解。建议用更具描述性的名字，如 score。


冗余初始化：

input1 = 0 初始化后立即被覆盖（input1 = int(input(...))），这行代码多余。


缺少异常处理：

如果用户输入非整数（如 "abc"），int(input()) 会抛出 ValueError，程序会崩溃。题目未明确要求异常处理，但添加它可以提高健壮性。


括号冗余：

条件语句中的括号（如 if(100 >= input1 >= 90)）在 Python 中是多余的，可以去掉以提高可读性。


格式改进：

level = "等级：A" 每次重复“等级：”字符串，稍显冗余。可以在最后统一添加“等级：”前缀。
'''

# 改进代码
try:
    score = int(input("请输入分数："))
    if 0 <= score <= 100:
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        print(f"等级：{grade}")
    else:
        print("无效分数")
except ValueError:
    print("请输入有效的整数分数")