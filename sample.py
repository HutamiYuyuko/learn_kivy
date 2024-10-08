from kivy.app import App
# 文字を表示する
from kivy.uix.label import Label

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

# 日本語が使用できるように
# 日本語のフォントが入っているパスを指定
# windows C:\Windows\Fonts
# Mac \System/Library/Fonts
resource_add_path('C:\Windows\Fonts')
# フォント指定
LabelBase.register(DEFAULT_FONT,'YuGothL.ttc')

# App().run()

# テキストの表示クラス
# Appの継承
class TextApp(App):
    def build(self):
        return Label(text='みなさん、こんにちはゆゆです。')

TextApp().run()