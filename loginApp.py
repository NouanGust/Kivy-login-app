import kivy
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel

class LoginApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.accent_palette = "Teal"
        self.root.current = 'logado'
    
        return Builder.load_file('login.kv')
    
    def mostrar_erro(self):
        self.root.get_screen('login').ids.errorLabel.text = "Informe os dados corretamente."


    # Método login

    def login(self):
        username = self.root.get_screen('login').ids.username.text
        senha = self.root.get_screen('login').ids.senha.text
        if username and senha:
            self.root.current = 'logado'
        else:
            self.mostrar_erro()
            
            print("Por favor, insira nome de usuário e senha.")

    def concluir(self):
        tarefaLabel = self.root.get_screen('logado').ids.tarefaLabel
        tarefaLabel.font_style = "Overline"
    
    def addTarefa(self):
        tarefa = MDLabel(text="nova tarefa")
        self.root.get_screen('logado').ids.telaPrincipal.add_widget(tarefa)
    


LoginApp().run()
