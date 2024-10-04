from kivy.app import App

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
# Appの継承 TestApp→Test→Test.kv 一致させる必要あり
class TestApp(App):
    pass 

# Pythonスクリプトファイルがメインで実行されたら以下のコードを実行
if __name__=='__main__':
    TestApp().run()