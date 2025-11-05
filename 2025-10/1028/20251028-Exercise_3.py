# 练习 3：简单成绩管理系统
'''
题目描述：
编写一个程序，模拟一个简单的成绩管理系统：

提示用户输入学生姓名和成绩（格式：姓名:成绩，如 Alice:85），输入 "quit" 结束。
将每位学生的姓名和成绩存入字典。
程序结束后，输出：

所有学生成绩列表
平均分
最高分和最低分学生

提示：

使用 while True 循环 + break 退出。
使用 split(":") 分割输入。
使用 sum(scores.values()) / len(scores) 计算平均分。
使用 max(scores, key=scores.get) 找最高分学生。

示例
请输入学生成绩（姓名:成绩），输入 quit 结束：
Alice:85
Bob:92
Charlie:78
quit
---
学生成绩：{'Alice': 85, 'Bob': 92, 'Charlie': 78}
平均分：85.0
最高分：Bob (92分)
最低分：Charlie (78分)
'''
maxScore,minScore = 0,0
scores = {}
print("请输入学生成绩（姓名:成绩），输入 quit 结束：")
while True:
    student_mark = input("")
    if student_mark == "quit":
        print("---")
        break
    
    temp = student_mark.split(":")
    scores[temp[0]] = int(temp[1])

for i,j in scores.items():
    #sum1 += j
    if maxScore < j:
        maxScore = j
        maxName = i
    else:
        minScore = j
        minName = i
    print(i,j)

print("学生成绩：",scores)
print("平均分：",sum(scores.values()) / len(scores))
print(f"最高分：{maxName}（{maxScore}）")
print(f"最低分：{minName}（{minScore}）")


#优化代码
scores = {}
print("请输入学生成绩（姓名:成绩），输入 quit 结束：")
while True:
    user_input = input()
    if user_input == "quit":
        break

    # 简单输入验证
    if ":" not in user_input:
        print("输入格式错误，请使用 姓名:成绩")
        continue

    name, score_str = user_input.split(":", 1)  # 最多分割一次
    name = name.strip()
    score_str = score_str.strip()

    if not score_str.isdigit():
        print("成绩必须是数字！")
        continue

    scores[name] = int(score_str)

# === 程序结束，统一输出 ===
if not scores:
    print("没有录入任何学生成绩。")
else:
    print("---")
    print("学生成绩：", scores)

    avg = sum(scores.values()) / len(scores)
    print(f"平均分：{avg:.1f}")

    # 找最高分
    max_name = max(scores, key=scores.get)
    max_score = scores[max_name]
    print(f"最高分：{max_name} ({max_score}分)")

    # 找最低分
    min_name = min(scores, key=scores.get)
    min_score = scores[min_name]
    print(f"最低分：{min_name} ({min_score}分)")