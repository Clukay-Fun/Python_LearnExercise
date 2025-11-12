'''
练习 2：解析 CSV 文件中的学生成绩（中级）
题目描述：
编写一个函数 parse_csv_scores(filename)，读取 CSV 文件（格式：name,score），返回一个字典 {name: score}。使用正则表达式验证每行格式，确保姓名只含字母和空格，成绩是 0-100 的整数。
'''
import csv,re
def parse_csv_scores(filename):
    scores_dict = {}
    try:
        with open(filename,'r',encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                name = re.match(r'^[A-Za-z\s]+$',row[0])
                score = re.match(r'^\d{1,3}$',row[1])
                if name and score:
                    d_name = name.group()
                    d_score = score.group()
               
                scores_dict[d_name] = d_score
    except FileNotFoundError:
        print("找不到文件")
    except ValueError:
        print("值错误")
    return scores_dict
        
result = parse_csv_scores("2025-11/1111/scores.csv")
print(result)  # {'Alice': 85, 'Bob': 92}
# 打印: 无效行: Charlie,abc

'''
改进点
1.修正缩进：将 scores_dict 赋值放入 if 块。
2.转换成绩为整数：int(score)。
3.添加成绩范围验证：0 <= int(score) <= 100。
4.打印无效行：检测格式错误或无效成绩。
5.处理 IndexError：检查行长度。
'''
#修改后的代码
# ...existing code...
import csv
import re

def parse_csv_scores(filename):
    scores_dict = {}  # 存放解析后的 {name: score}
    try:
        # 以 utf-8 打开 CSV 文件，使用 csv.reader 逐行读取
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                try:
                    # 每行应恰好包含两个字段：name 和 score
                    if len(row) != 2:
                        print(f"无效行: {','.join(row)}")  # 字段数不对，打印提示并跳过
                        continue

                    name, score = row

                    # 验证姓名只包含字母和空格（例如 "Alice" 或 "Bob Smith"）
                    if not re.match(r'^[A-Za-z\s]+$', name):
                        print(f"无效行: {name},{score}")  # 姓名格式不合法，跳过
                        continue

                    # 验证成绩为 1 到 3 位数字，并在 0 到 100 范围内
                    if not (re.match(r'^\d{1,3}$', score) and 0 <= int(score) <= 100):
                        print(f"无效行: {name},{score}")  # 分数格式或范围不合法，跳过
                        continue

                    # 合法时将成绩转换为 int 并保存
                    scores_dict[name] = int(score)
                except ValueError:
                    # 防御性捕获：处理 int 转换或其他可能的值错误
                    print(f"无效行: {','.join(row)}")
    except FileNotFoundError:
        # 文件不存在时给出友好提示
        print("找不到文件")
    return scores_dict

# 测试：调用函数并打印解析结果
result = parse_csv_scores("scores.csv")
print(result)  # 期望输出示例: {'Alice': 85, 'Bob': 92}
# ...existing code...