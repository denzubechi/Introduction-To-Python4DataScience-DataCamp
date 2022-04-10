# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""  

from kivy.app import App
from kivy.uix.label import Label
class FirstApp(App):
    def build(self):
        return Label(text="Hello Samuel")
FirstApp().run()        