class TodoItem:
    def __init__(self, task, priority):
        self.task = task
        self.priority = priority
        
    def __str__(self):
        print(self.priority,":",self.task)
        
# 改进后的代码
class TodoItem:
    def __init__(self, task, priority):
        if not isinstance(priority, int) or priority <= 0:
            raise ValueError("优先级必须是正整数")
        self.task = task
        self.priority = priority
    
    def __str__(self):
        return f"{self.priority}: {self.task}"