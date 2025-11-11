'''
练习 3：日志分析器类（中级项目）
题目描述：
创建一个 LogAnalyzer 类，分析日志文件（每行格式：[YYYY-MM-DD HH:MM:SS] LEVEL message），统计每个级别（INFO, WARNING, ERROR）的出现次数，并提取所有 ERROR 消息。

要求：
1.定义 LogAnalyzer 类：
    方法 load_log(filename)：读取日志文件。
    方法 get_stats()：返回 {level: count} 字典。
    方法 get_errors()：返回 ERROR 消息列表。

2.使用正则表达式解析日志行（r'^\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] (INFO|WARNING|ERROR) (.+)$'）。

3.使用 try-except 处理文件和格式错误。

4.测试文件 log.txt：
[2023-10-01 12:00:00] INFO System started
[2023-10-01 12:01:00] ERROR Failed to connect
[2023-10-01 12:02:00] WARNING Low memory
[2023-10-01 12:03:00] ERROR Invalid input

示例：
analyzer = LogAnalyzer()
analyzer.load_log("log.txt")
print(analyzer.get_stats())  # {'INFO': 1, 'WARNING': 1, 'ERROR': 2}
print(analyzer.get_errors())  # ['Failed to connect', 'Invalid input']

提示：
- 使用 re.match(pattern, line) 解析每行。
- 存储结果：self.stats = {'INFO': 0, 'WARNING': 0, 'ERROR': 0}。
'''