'''
练习 3：简易待办事项管理器（中级项目）
题目描述：
编写一个程序，管理待办事项（To-Do List），支持以下功能：

输入待办事项（格式：任务,优先级），输入 "quit" 退出。
将待办事项保存到文件 todo.txt（每行：任务:优先级）。
读取文件并按优先级（数字，1 最高）排序显示。
使用 try-except 处理输入和文件错误。

示例：
请输入待办事项（任务,优先级），输入 quit 结束：
Write code,1
Read book,3
Exercise,2
quit
---
已保存到 todo.txt
排序后的待办事项：
1: Write code
2: Exercise
3: Read book

提示：
使用字典或列表存储 {任务: 优先级} 或 [(任务, 优先级)]。
保存：file.write(f"{task}:{priority}\n")
排序：sorted(todos, key=lambda x: x[1])
捕获 ValueError（优先级非数字）。
'''

filename = "G:/.Program/Python/Python_LearnExercise-1/2025-11/todo.txt"
print("请输入待办事项（任务,优先级），输入 quit 结束：")
todo_dict = {}
while True:
    todo_str = input("")
    if todo_str == "quit":
        break
    with open(filename,'w',encoding='utf-8') as file:
        try:
            todo_list = todo_str.split(",")
            file.write(f"{todo_list[1]}：{todo_list[0]}\n")
        except FileNotFoundError:
            print("文件未找到")
        except ValueError:
            print("输入的不是数字")
    