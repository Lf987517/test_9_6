import os

url ='http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html'
root_path=os.path.dirname(os.path.dirname(__file__))
driver_path=root_path+r'/driver/msedgedriver.exe'
case_path = root_path+r'/test_cases'
# report_path = root_path+r'/result/report'
file_path = root_path+r'/data/test.xlsx'
log_file= root_path+r'/log/log.txt'
system_version='1.2'