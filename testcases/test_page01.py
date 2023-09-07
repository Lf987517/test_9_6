from time import sleep
from objectpage.login_page import Loginpage
from data.data import ReadWrite
from log.log import loggers

class TestCases:
    def test_01(self,login):
        '''
        验证有效的登录用户名和密码登录成功
        '''
        print('登录的第一个测试用例')
        self.driver=login
        self.loginpage=Loginpage(self.driver)
        user_list=ReadWrite().excelread('users')
        username=user_list[0][0]
        password=user_list[0][1]
        print(username +password)
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        self.loginpage.click_login()
        sleep(0.5)
        # try:
        assert '我的地盘 - 禅道' in self.driver.title
        self.loginpage.click_logout()
        loggers.info('有效的用户名和密码登录系统')
        # except:
        #     print('登录不成功')

    # def atest_02(self):
    #     '''
    #     验证密码为空时登录失败
    #     '''
    #     print('登录的第二个测试用例')
    #     self.loginpage.input_username('admin')
    #     self.loginpage.click_login()
    #     sleep(0.5)
    #     alert_dialog=self.driver.switch_to.alert
    #     alert_dialog.accept()
