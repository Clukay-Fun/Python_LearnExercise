'''
练习 1：定义 Student 类管理成绩（中级）
题目描述：
定义一个 Student 类，用于管理学生信息（姓名和成绩）。实现以下功能：
初始化时传入姓名和成绩。
方法 get_grade() 返回成绩对应的等级（90-100: A, 80-89: B, 70-79: C, 60-69: D, 0-59: F）。
方法 display() 打印学生信息，格式为：姓名: 成绩 (等级)。

要求：
确保成绩在 0-100 范围内，否则抛出 ValueError。
测试代码：
student = Student("Alice", 85)
print(student.get_grade())  # B
student.display()  # Alice: 85 (B)

提示：
使用 __init__ 初始化 name 和 score。
在 __init__ 中验证成绩范围。
get_grade() 使用 if-elif-else 判断等级。
'''
