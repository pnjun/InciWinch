# -*- coding: utf-8 -*-
#General Imports
from radioHandler import RadioHandler

#Kivy Imports
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty


class InciWinchApp(App):
    theme_cls = ThemeManager()
    previous_date = ObjectProperty()
    title = "InciWinch"

    def build(self):
        main_widget = Builder.load_file('gui.kv')
        return main_widget



if __name__ == '__main__':
    InciWinchApp().run()


    radio = RadioHandler("/dev/tty.usbserial-DN03FTBY")
