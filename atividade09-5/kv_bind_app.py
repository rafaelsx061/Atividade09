from kivy.app import App

# Importa o BoxLayout, um tipo de layout que organiza widgets em uma linha ou coluna
from kivy.uix.boxlayout import BoxLayout

# Define uma classe chamada MyContainer que herda de BoxLayout
# Essa classe pode ser usada para definir um layout personalizado no arquivo .kv
class MyContainer(BoxLayout):
    pass  # Nenhuma funcionalidade adicional por enquanto, apenas herda o comportamento padrão

# Define a classe principal do aplicativo, que herda de App
class KvBindApp(App):
    def build(self):
        # Retorna uma instância de MyContainer quando o aplicativo for iniciado
        return MyContainer()

# Verifica se este arquivo está sendo executado diretamente (e não importado)
if __name__ == "__main__":
    # Inicia o aplicativo
    KvBindApp().run()
