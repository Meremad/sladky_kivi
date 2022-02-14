from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class MyApp(App):
    def press_b(self, instance):
        self.lbl.text = 'олжик лох'

    def build(self):
        box = BoxLayout(orientation='vertical', padding=[25])
        self.lbl = Label(text=' ', font_size=50)

        box.add_widget(Button(text='Нажми меня !', font_size=30, on_press=self.press_b))
        box.add_widget(self.lbl)

        return box


if __name__ == '__main__':
    MyApp().run()