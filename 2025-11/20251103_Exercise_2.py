'''
练习 2：保存和读取成绩（中级）
题目描述：
编写两个函数：

save_scores(scores, filename)：将字典 scores（键为学生姓名，值为成绩）保存到文件中，每行格式为 姓名:成绩。
load_scores(filename)：读取文件，返回成绩字典。

要求：
使用 with open() 进行文件操作。
使用 try-except 处理文件不存在或格式错误。

测试代码：
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
save_scores(scores, "scores.txt")
loaded = load_scores("scores.txt")
print(loaded)  # {'Alice': 85, 'Bob': 92, 'Charlie': 78}

提示：
写入：file.write(f"{name}:{score}\n")
读取：line.strip().split(":")
捕获 FileNotFoundError 和 ValueError。
'''
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
def save_scores(scores, filename):
    with open(filename,'w',encoding='utf-8') as file:
        try:
            for name,score in scores.items():
                file.write(f"{name}:{score}\n")
        except FileNotFoundError:
            print("文件不存在")

def load_scores(filename):
    score_dict = {}
    with open(filename,'r',encoding='utf-8') as file:
        try:
            for lines in file:
                line = lines.strip().split(":")
                score_dict[line[0]]=int(line[1])
        except FileNotFoundError:
            print("文件不存在")
    return print(score_dict)

save_scores(scores, "G:/.Program/Python/Python_LearnExercise-1/2025-11/scores.txt")
load_scores("G:/.Program/Python/Python_LearnExercise-1/2025-11/scores.txt")