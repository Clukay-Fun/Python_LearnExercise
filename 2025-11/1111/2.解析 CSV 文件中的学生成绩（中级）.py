'''
练习 2：解析 CSV 文件中的学生成绩（中级）
题目描述：
编写一个函数 parse_csv_scores(filename)，读取 CSV 文件（格式：name,score），返回一个字典 {name: score}。使用正则表达式验证每行格式，确保姓名只含字母和空格，成绩是 0-100 的整数。
'''

'''
要求：
1.CSV 文件示例（scores.csv）：
Alice,85
Bob,92
Charlie,abc
'''

#2.使用 re 验证姓名（r'^[A-Za-z\s]+$'）和成绩（r'^\d{1,3}$'）。

'''
3.跳过无效行，打印错误信息。
4.使用 try-except 处理文件错误。
'''

'''
示例：
pythonresult = parse_csv_scores("scores.csv")
print(result)  # {'Alice': 85, 'Bob': 92}
# 打印: 无效行: Charlie,abc
'''

#提示：
#- 读取 CSV：with open(filename, 'r') as file: file.readlines()
#- 验证姓名：re.match(r'^[A-Za-z\s]+$', name)
#- 验证成绩：re.match(r'^\d{1,3}$', score) and 0 <= int(score) <= 100

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