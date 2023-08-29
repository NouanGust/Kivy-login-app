import kivy
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

class LoginApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.accent_palette = "Teal"
        self.root.current = 'login'
        return Builder.load_file('login.kv')
    
    def login(self):
        screen = self.root_window
        # usermane = self.root.ids.username.text
        # senha = self.root.ids.senha.text
        # if usermane and senha != '':
        #     self.root.current = 'logado'
        print(self.root.ids.username.text)


LoginApp().run()