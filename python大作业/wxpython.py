import wx


class LoginFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='用户登录', size=(300, 200))

        # 创建用户名和密码的文本框
        username_label = wx.StaticText(self, label='用户名:', pos=(10, 20))
        password_label = wx.StaticText(self, label='密码:', pos=(10, 50))

        self.username_text = wx.TextCtrl(self, pos=(80, 20), size=(150, -1))
        self.password_text = wx.TextCtrl(self, pos=(80, 50), size=(150, -1), style=wx.TE_PASSWORD)

        # 创建登录按钮
        login_button = wx.Button(self, label='登录', pos=(150, 100))
        login_button.Bind(wx.EVT_BUTTON, self.on_login)

        # 显示窗口
        self.Show()

    def on_login(self, event):
        username = self.username_text.GetValue()
        password = self.password_text.GetValue()
        print(f"用户名: {username}, 密码: {password}")
        # 这里你可以添加更多的逻辑，比如验证用户名和密码，等等。


if __name__ == '__main__':
    app = wx.App()
    LoginFrame()
    app.MainLoop()