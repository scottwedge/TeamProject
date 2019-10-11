from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

from kivy.config import Config
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')

class MyApp(App):
    def build(self):
        return Label(text='text')

if __name__ == '__main__':
    MyApp().run()