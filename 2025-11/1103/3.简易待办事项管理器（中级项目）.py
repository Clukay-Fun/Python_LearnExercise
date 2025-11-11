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

'''改进点
使用列表 todos 存储 (task, priority) 元组，统一写入。
使用 'w' 模式在循环后一次性写入，避免覆盖。
读取文件并用 sort(key=lambda x: x[1]) 按优先级排序。
更严格的输入验证（检查逗号和数字）。
格式正确：任务:优先级。
默认相对路径 "todo.txt"。
'''

#改进后的代码
def manage_todo(filename="todo.txt"):
    todos = []
    print("请输入待办事项（任务,优先级），输入 quit 结束：")
    
    while True:
        user_input = input()
        if user_input == "quit":
            break
        try:
            task, priority = user_input.split(",", 1)
            task = task.strip()
            priority = int(priority.strip())  # 确保优先级是数字
            todos.append((task, priority))
        except ValueError:
            print("请输入正确格式（任务,优先级）或优先级必须为数字")
    
    # 保存到文件
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for task, priority in todos:
                file.write(f"{task}:{priority}\n")
    except FileNotFoundError:
        print("文件保存失败")
        return
    
    # 读取并排序显示
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            todos = []
            for line in file:
                task, priority = line.strip().split(":", 1)
                todos.append((task, int(priority)))
            todos.sort(key=lambda x: x[1])  # 按优先级升序
            print("---")
            print("排序后的待办事项：")
            for task, priority in todos:
                print(f"{priority}: {task}")
    except FileNotFoundError:
        print("文件不存在")
    except ValueError:
        print("文件内容格式错误")

manage_todo()