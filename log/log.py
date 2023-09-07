
import logging
from config.config import log_file

#创建日志器
loggers=logging.getLogger()
#设置日志器的级别
loggers.setLevel(logging.INFO)

#定义处理器的格式
# f=logging.FileHandler(r'D:\software\prcharm-project\Test\pytest\web_pytest_framework\log',mode='a',encoding='utf-8')
format=logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
logFile=log_file
#创建处理器
fh=logging.FileHandler(logFile,mode='a',encoding='utf-8')
#设置处理器级别
fh.setLevel(logging.INFO)
#设置处理器格式
fh.setFormatter(format)
#添加到日志器
loggers.addHandler(fh)


#日志文件的formate
'''
%(created)f:日期
%(name):logger的名字
%(levelno):数字形式的日志级别 DEBUG 10,INFO 20,WARNING 30, ERROR 40,CRITICAL 50
%(filename):调用日志输出函数的模块的完整路径名
%(module)s:调用日志输出的模块名
%(asctime)s:字符串形式的当前时间，‘2022-04-20’
%(message)s:用户输入信息
'''