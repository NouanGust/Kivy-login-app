import kivy
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

class LoginApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.accent_palette = "Teal"
        self.root.current = 'login'
        
        self.dialog = MDDialog(text='Insira um nome e senha.', buttons =[
    MDFlatButton(text='Ok!', on_release=self.dialog.dismiss)        
])
        
        return Builder.load_file('login.kv')
    
    def mostrar_erro(self):

        self.root.get_screen('login').add_widget(self.dialog)

    # Método login

    def login(self):
        username = self.root.get_screen('login').ids.username.text
        senha = self.root.get_screen('login').ids.senha.text
        if username and senha:
            self.root.current = 'logado'
        else:
            self.mostrar_erro()
            
            print("Por favor, insira nome de usuário e senha.")



LoginApp().run()
