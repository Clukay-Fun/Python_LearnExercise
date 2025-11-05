'''
练习 3：成绩管理函数化（中级项目）
题目：
将昨天的 成绩管理系统 封装成函数 manage_scores()，无需输入，直接在函数内写死 3 名学生成绩，然后：

输出字典
输出平均分（保留 1 位小数）
输出最高分和最低分学生

要求：

函数名：manage_scores()
内部写死数据：
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
使用 max(..., key=scores.get) 和 min(...)
输出格式与昨天一致

示例输出：
学生成绩：{'Alice': 85, 'Bob': 92, 'Charlie': 78}
平均分：85.0
最高分：Bob (92分)
最低分：Charlie (78分)
'''

def manage_scores():
    scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
    print("学生成绩：",scores)
    
    avg = sum(scores.values()) / len(scores)
    print(f"平均分：{avg:.1f}")
    
    max_name = max(scores, key = scores.get)
    max_score = scores[max_name]
    print(f"最高分：{max_name}({max_score}分)")
    
    min_name = min(scores, key = scores.get)
    min_score = scores[min_name]
    print(f"最低分：{min_name}({min_score}分)")
    
manage_scores()