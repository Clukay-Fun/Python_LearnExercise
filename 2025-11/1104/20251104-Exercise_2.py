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
    
'''改进点
修正 __str__：返回字符串，而不是 print。
添加优先级验证：确保是正整数。
使用 print(task) 替代 task.__str__()。
变量名更简洁：todos 更符合 Python 命名习惯。
'''

from todo import TodoItem

todos = []
todos.append(TodoItem("Write code", 1))
todos.append(TodoItem("Read book", 3))
todos.append(TodoItem("Exercise", 2))

sorted_todos = sorted(todos, key=lambda x: x.priority)
for task in sorted_todos:
    print(task)  # 自动调用 __str__