'''
练习 2：模块化的待办事项类（中级）
题目描述：
创建一个模块 todo.py，定义一个 TodoItem 类，管理待办事项（任务和优先级）。然后在主程序中：

创建多个 TodoItem 对象。
按优先级排序并打印。

要求：

在 todo.py 中定义 TodoItem 类：

属性：task（字符串），priority（整数）。
方法：__str__ 返回格式 优先级: 任务。

主程序 main.py：

导入 todo.py。
创建至少 3 个 TodoItem 对象，存入列表。
按优先级升序排序，打印所有任务。

使用 try-except 确保优先级是正整数。

示例（main.py 输出）：
1: Write code
2: Exercise
3: Read book

提示：
todo.py：
pythonclass TodoItem:
    def __init__(self, task, priority):
        self.task = task
        self.priority = priority

main.py：使用 sorted(todos, key=lambda x: x.priority)。
'''

import todo
todoList = []
todoItem = todo.TodoItem
todoList.append(todoItem("Write code",1))
todoList.append(todoItem("Read book",3))
todoList.append(todoItem("Exercise",2))
new_lst = sorted(todoList, key=lambda x: x.priority)
for task in new_lst:
    task.__str__()