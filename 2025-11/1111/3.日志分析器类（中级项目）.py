'''
练习 3：日志分析器类（中级项目）
题目描述：
创建一个 LogAnalyzer 类，分析日志文件（每行格式：[YYYY-MM-DD HH:MM:SS] LEVEL message），统计每个级别（INFO, WARNING, ERROR）的出现次数，并提取所有 ERROR 消息。
'''
import re
class LogAnalyzer:
    line_lst = list()
    line_dict = dict()
    error_lst = list()
    def load_log(self,filename):
        with open(filename,'r',encoding='utf-8') as file:
            for line in file:
                self.line_lst.append(line.strip())
        return self.line_lst
    
    def get_stats(self):
        pattern = re.compile(r'^\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] (INFO|WARNING|ERROR) (.+)$')
        for line in self.line_lst:
            info = re.match(pattern,line)
            level = info.group(1)
            if level == 'ERROR':
                self.error_lst.append(info.group(2))
                
            self.line_dict[level] = self.line_dict.get(level,0)+1
        return dict(sorted(self.line_dict.items(),key=lambda x:x[1], reverse=True))
    
    def get_errors(self):
        return self.error_lst
    
analyzer = LogAnalyzer()
analyzer.load_log("2025-11/1111/log.txt")
print(analyzer.get_stats())
print(analyzer.get_errors())

'''改进点
1.将 line_lst, line_dict, error_lst 改为实例属性，在 __init__ 初始化。
2.添加 FileNotFoundError 处理。
3.检查 re.match 结果，跳过无效行。
4.初始化 stats 字典，确保所有级别都有默认值。
5.移除 load_log 的返回值。
'''
#改进后代码
import re
class LogAnalyzer:
    def __init__(self):
        self.lines = []
        self.stats = {'INFO': 0, 'WARNING': 0, 'ERROR': 0}
        self.errors = []
    
    def load_log(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                self.lines = [line.strip() for line in file]
        except FileNotFoundError:
            print("文件不存在")
    
    def get_stats(self):
        pattern = re.compile(r'^\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] (INFO|WARNING|ERROR) (.+)$')
        for line in self.lines:
            match = re.match(pattern, line)
            if match:
                level = match.group(1)
                self.stats[level] += 1
                if level == 'ERROR':
                    self.errors.append(match.group(2))
        return self.stats
    
    def get_errors(self):
        return self.errors

# 测试
analyzer = LogAnalyzer()
analyzer.load_log("log.txt")
print(analyzer.get_stats())  # {'INFO': 1, 'WARNING': 1, 'ERROR': 2}
print(analyzer.get_errors())  # ['Failed to connect', 'Invalid input']