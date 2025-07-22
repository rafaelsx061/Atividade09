from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

# Widget principal com uma propriedade de texto
class MyWidget(BoxLayout):
    saudacao = StringProperty("Olá, Kivy!")  # Propriedade do tipo string

class StringPropApp(App):
    def build(self):
        return MyWidget()

if __name__ == "__main__":
    StringPropApp().run()