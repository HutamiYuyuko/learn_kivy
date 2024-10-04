from kivy.app import App
# 文字を表示する
from kivy.uix.label import Label

# App().run()

# テキストの表示クラス
# Appの継承
class TextApp(App):
    def build(self):
        return Label(text='Hello kivy')

TextApp().run()