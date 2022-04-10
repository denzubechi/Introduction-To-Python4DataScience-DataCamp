# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 20:42:39 2020

@author: Sah Meey
"""


from kivy.app import App
from kivy.uix.image import Image
class FirstApp(App):
    def build(self):
        return  Image(source="game.JPG")
FirstApp().run()        