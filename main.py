#-*- coding: utf-8 -*-
from kivy.config import Config
#縦横の高さ
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')

from kivy.app import App
from kivy.uix.widget import Widget #ウィジェット

from kivy.properties import StringProperty

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

from random import randint #数字をランダムに表示

# デフォルトに使用するフォントを変更する
# resource_add_path('/System/Library/Fonts')
# LabelBase.register(DEFAULT_FONT, 'PingFang.ttc') #日本語が使用できるように日本語フォントを指定する
resource_add_path('C:\Windows\Fonts')
# フォント指定
LabelBase.register(DEFAULT_FONT,'YuGothL.ttc')

resource_add_path('image/')

class ImageWidget(Widget):
    source = StringProperty('image/ootsubo01.jpg')

    def __init__(self, **kwargs): # おまじない
        super(ImageWidget, self).__init__(**kwargs)
        pass

    def buttonStarted(self): # ボタンを押すとデフォルトの画像に戻る
        self.source= 'image/ootsubo01.jpg'

    def buttonRandom(self):
        self.source = f'ootsubo0{randint(1,7)}.jpg'

class OotsuboApp(App):
    def __init__(self, **kwargs):
        super(OotsuboApp, self).__init__(**kwargs)
        self.title = '大坪画像表示'

if __name__ == '__main__':
    OotsuboApp().run()
