import time
import yagmail

class Mail:
    """
    邮件相关类
    """

    def log(self, content):
        now_time = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime()
        )
        print(f'{now_time}: {content}')

    def sendmail(self, msg, title, receivers):
        """
        发送邮件
        
        Arguments:
            msg {str} -- 邮件正文
            title {str} -- 邮件标题
            receivers {list} -- 邮件接收者，数组
        """

        yag = yagmail.SMTP(
            host='smtp.qq.com', user='你的邮箱',
            password='你的鉴权码', smtp_ssl=True
        )

        try:
            yag.send(receivers, title, msg)
            self.log("邮件发送成功")

        except BaseException as e:
            print (e)
            self.log("Error: 无法发送邮件")

