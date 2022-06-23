import imp
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import Property
from kivy.lang import Builder

# Designate the inherit.kv design file
Builder.load_file('inherit.kv')

class MyLayout(Widget):
    pass

class AwesomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    AwesomeApp().run()
    
