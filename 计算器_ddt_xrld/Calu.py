import smtplib
import unittest
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

from HTMLTestRunner import HTMLTestRunner
from ddt import ddt, data, unpack
from data import int_data


# 测试用的class
class Calc:

    def add(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


# 测试代码脚本
@ddt
class MyTestCase(unittest.TestCase):
    @data(*int_data('calc测试数据.xls'))
    @unpack
    def test_calc(self, a, b, c):
        calc = Calc()
        s = calc.minus(a, b)
        self.assertEqual(c, s)  # add assertion here


if __name__ == '__main__':
    unittest.main()


def runner_test():
    test = unittest.defaultTestLoader.discover(r"D:\python_program\计算器测试", pattern="calculate_test1.py")
    # 创建运行器
    runner = HTMLTestRunner.HTMLTestRunner(
        title="计算器测试报告",
        description="测试计算器的加减法（课堂作业）",
        verbosity=2,
        stream=open(file="calculator_test.html", mode="w+", encoding="utf-8")
    )
    # 执行
    runner.run(test)


runner_test()


def email():
    smtp_server = 'smtp.qq.com'
    smtp_pass = 'lpuygenbzpusbbfj'
    smtp_send = '759960185@qq.com'
    stmp_receive = ['759489321@qq.com']

    file_name = 'calculator_test.html'

    msg = MIMEMultipart()
    msg['from'] = smtp_send
    msg['to'] = '759489321@qq.com'
    msg['subject'] = '最后的边界值测试有问题，原因是excel不支持这么长的整数' \
                     '，只能用字符串，除非在输入算法中专门做一个数据转换'

    with open(file_name, 'rb') as f:
        content = f.read()
        part = MIMEBase('application', 'octet-stream')
        # 这句代码是用来创建一个MIMEBase对象，它表示一个MIME消息的基本部分。
        # MIMEBase('application', 'octet-stream') 创建了一个表示应用程序类型数据（'application'）的MIMEBase对象
        # 该数据以八位组流（'octet-stream'）的形式呈现
        part.set_payload(content)
        encoders.encode_base64(part)
        part.add_header('Content-Dispositon', 'attachment; filename="{}"'.format(file_name))
        # 这句代码是用来设置邮件附件的Content-Disposition头的。
        # Content-Disposition 是一个 MIME 头部字段，用于描述消息体的呈现方式。
        # 它可以告诉邮件客户端如何处理邮件附件，例如是否应该将其作为文件保存、是否应该将其作为可执行文件运行等。
        msg.attach(part)

    server = smtplib.SMTP(smtp_server)
    server.login(smtp_send, smtp_pass)
    server.sendmail(smtp_send, msg['to'], msg.as_string())
    server.quit()


email()
