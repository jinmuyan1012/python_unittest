import unittest
from login import get_username, get_password
# 使用TestCase


class TestLogin(unittest.TestCase):

    # 初始化用例
    def setUp(self) -> None:
        print('每次执行测试用例前执行')
    # 清空方法

    def tearDown(self) -> None:
        print("每次执行测试用例后执行")

    def test_login_username(self):
        # 预期结果：自己登录的账号
        expect_username = 'test01'
        # 实际结果：显示在页面上的账号
        acutl_username = get_username()
        self.assertEqual(expect_username, acutl_username)
        # assert expect_username == acutl_username

    def test_login_password(self):
        # 预期结果：自己登录的密码
        expect_password = 'test01'
        # 实际结果：显示在页面的密码
        acutl_password = get_password()
        self.assertEqual(expect_password, acutl_password)
        # assert expect_password == acutl_password


# unittest.main()

# 创建测试套件，套件可以理解为一组用例的组合

# suite = unittest.TestSuite()

# # 添加一条测试用例:addTest
# suite.addTest(TestLogin('test_login_username'))
# suite.addTest(TestLogin('test_login_password'))

# 添加多条测试用例：addTests
# lst = [TestLogin('test_login_username'), TestLogin('test_login_password')]
# suite.addTests(lst)


# 使用TestLoader中的discover()来执行测试用例

suite = unittest.TestLoader().discover('.', pattern='test*.py')

runner = unittest.TextTestRunner()
runner.run(suite)
