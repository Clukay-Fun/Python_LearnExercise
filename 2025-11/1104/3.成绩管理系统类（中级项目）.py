'''
练习 3：成绩管理系统类（中级项目）
题目描述：
创建一个 ScoreManager 类，管理学生成绩，支持：
添加学生（add_student(name, score)）。
保存成绩到文件（save_to_file(filename)）。
从文件读取成绩（load_from_file(filename)）。
打印统计信息（print_stats()）：学生成绩、平均分、最高/最低分学生。

要求：
使用 try-except 处理文件错误和无效成绩。

测试代码：
manager = ScoreManager()
manager.add_student("Alice", 85)
manager.add_student("Bob", 92)
manager.save_to_file("scores.txt")
manager.load_from_file("scores.txt")
manager.print_stats()

输出格式：
学生成绩：{'Alice': 85, 'Bob': 92}
平均分：88.5
最高分：Bob (92分)
最低分：Alice (85分)

提示：
内部用字典存储 {name: score}。
复用昨天的 save_scores 和 load_scores 逻辑。
使用 max(scores, key=scores.get) 找最高分。
'''

class ScoreManager:
    stdDict = {}
    sum = 0
    
    def add_student(self,name,score):
        try:
            self.stdDict[name] = int(score)
        except ValueError:
            print("请输入正确的数字")
            
    def save_to_file(self,filename):
        try:
            with open(filename,'w',encoding='utf-8') as file:
                for name,score in self.stdDict.items():
                    self.sum += int(score)
                    file.write(f"{name}:{score}\n")
        except FileNotFoundError:
            print("文件不存在")
            
    
    def load_from_file(self,filename):
        score_dict = {}
        with open(filename,'r',encoding='utf-8') as file:
            for line in file:
                name,score = line.strip().split(":",1)
                score_dict[name] = int(score)
        return score_dict
    
    def print_stats(self):
        maxScore = max(self.stdDict, key=self.stdDict.get)
        minScore = min(self.stdDict, key=self.stdDict.get)
        print(f"学生成绩：{self.stdDict}")
        print(f"平均分：{self.sum / len(self.stdDict)}")
        print(f"最高分：{maxScore}({self.stdDict[maxScore]}分)")
        print(f"最低分：{minScore}({self.stdDict[minScore]}分)")
        return
    
manager = ScoreManager()
manager.add_student("Alice",85)
manager.add_student("Bob", 92)
manager.save_to_file("scores.txt")
manager.load_from_file("scores.txt")
manager.print_stats()


'''改进点
将 stdDict 和 sum 改为实例属性。
修正平均分：在 print_stats 中计算，避免重复累加。
添加空字典检查，防止除零错误。
增强 load_from_file：更新 self.stdDict，并处理行格式错误。
移除 print_stats 的多余 return。
验证成绩范围（0-100）。
'''
class ScoreManager:
    def __init__(self):
        self.stdDict = {}  # 实例属性
        self.sum = 0       # 实例属性
    
    def add_student(self, name, score):
        try:
            score = int(score)
            if not (0 <= score <= 100):
                raise ValueError("分数必须在 0-100 之间")
            self.stdDict[name] = score
        except ValueError:
            print("请输入有效的数字分数")
            
    def save_to_file(self, filename):
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                for name, score in self.stdDict.items():
                    file.write(f"{name}:{score}\n")
        except FileNotFoundError:
            print("文件不存在")
            
    def load_from_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    try:
                        name, score = line.strip().split(":", 1)
                        self.stdDict[name] = int(score)
                    except ValueError:
                        print(f"无效格式行：{line.strip()}")
        except FileNotFoundError:
            print("文件不存在")
    
    def print_stats(self):
        if not self.stdDict:
            print("没有学生成绩")
            return
        print(f"学生成绩：{self.stdDict}")
        avg = sum(self.stdDict.values()) / len(self.stdDict)
        print(f"平均分：{avg:.1f}")
        max_name = max(self.stdDict, key=self.stdDict.get)
        print(f"最高分：{max_name} ({self.stdDict[max_name]}分)")
        min_name = min(self.stdDict, key=self.stdDict.get)
        print(f"最低分：{min_name} ({self.stdDict[min_name]}分)")

# 测试
manager = ScoreManager()
manager.add_student("Alice", 85)
manager.add_student("Bob", 92)
manager.save_to_file("scores.txt")
manager.load_from_file("scores.txt")
manager.print_stats()