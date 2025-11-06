class TodoItem:
    def __init__(self, task, priority):
        self.task = task
        self.priority = priority
        
    def __str__(self):
        print(self.priority,":",self.task)