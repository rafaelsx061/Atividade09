from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class InputPropWidget(BoxLayout):
    pass

class InputPropApp(App):
    def build(self):
        return InputPropWidget()

if __name__ == "__main__":
    InputPropApp().run()
