from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.properties import ListProperty


class MyPaintWidget(Widget):
    current_draw_color = ListProperty([1, 0, 0, 1])  # Vermelho por padrão

    def on_touch_down(self, touch):
        with self.canvas:
            Color(*self.current_draw_color)  # Usa a cor atual
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=2)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

    def set_draw_color(self, color_list):
        self.current_draw_color = color_list  # Atualiza a cor


class PaintColorApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical')

        # Área de desenho
        self.painter = MyPaintWidget()
        main_layout.add_widget(self.painter)

        # Área dos botões
        buttons_layout = BoxLayout(size_hint_y=0.15)

        # Botão Vermelho
        btn_vermelho = Button(text='Vermelho', background_color=[1, 0, 0, 1])
        btn_vermelho.bind(on_release=lambda x: self.painter.set_draw_color([1, 0, 0, 1]))
        buttons_layout.add_widget(btn_vermelho)

        # Botão Verde
        btn_verde = Button(text='Verde', background_color=[0, 1, 0, 1])
        btn_verde.bind(on_release=lambda x: self.painter.set_draw_color([0, 1, 0, 1]))
        buttons_layout.add_widget(btn_verde)

        # Botão Azul
        btn_azul = Button(text='Azul', background_color=[0, 0, 1, 1])
        btn_azul.bind(on_release=lambda x: self.painter.set_draw_color([0, 0, 1, 1]))
        buttons_layout.add_widget(btn_azul)

        main_layout.add_widget(buttons_layout)

        return main_layout


if __name__ == '__main__':
    PaintColorApp().run()
