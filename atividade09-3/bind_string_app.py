from kivy.app import App  # Importa a classe base para o aplicativo
from kivy.uix.boxlayout import BoxLayout  # Layout que organiza os widgets em linha ou coluna
from kivy.uix.label import Label  # Componente de texto
from kivy.uix.button import Button  # Componente de botão
from kivy.properties import StringProperty  # Propriedade reativa de string usada no Kivy

class StatusWidget(BoxLayout):
    status_message = StringProperty("Offline")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.label = Label(text=self.status_message)  # Cria um Label com o texto da propriedade
        self.add_widget(self.label)  # Adiciona o Label ao layout

        btn = Button(text="Mudar Status")  # Cria um botão
        btn.bind(on_release=self.mudar_status)  # Liga o botão ao método que altera o status
        self.add_widget(btn)  # Adiciona o botão ao layout

        self.bind(status_message=self.update_label_text)

    def update_label_text(self, instance, value):
        self.label.text = value

    def mudar_status(self, instance):
        self.status_message = "Online" if self.status_message == "Offline" else "Offline"

class BindStringApp(App):
    def build(self):
        return StatusWidget()

if __name__ == "__main__":
    BindStringApp().run()
