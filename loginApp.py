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
        # username = self.root.ids.username.text
        # senha = self.root.ids.senha.text
        # if usermane and senha != '':
        #     self.root.current = 'logado'
        print(self.root.ids.username.text)

    # Método login

    def login(self):
    username = self.root.get_screen('login').ids.username.text
    senha = self.root.get_screen('login').ids.senha.text
    if username and senha:
        self.root.current = 'logado'
    else:
        print("Por favor, insira nome de usuário e senha.")


LoginApp().run()
