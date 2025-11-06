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
