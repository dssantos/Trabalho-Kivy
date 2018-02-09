#!/usr/bin/python
# -*- coding: utf-8 -*-

############################################ kv imbutido no codigo atraves de string
# import kivy
# from kivy.app import App
# from kivy.lang import Builder

# class MainApp(App):
# 	def build(self):
# 		return Builder.load_string('''
# Label:
# 	text: 'Hello'
# ''')

# MainApp().run()

############################################ kv imbutido no codigo atraves de variavel string
# import kivy
# from kivy.app import App
# from kivy.lang import Builder

# kv = '''
# Label:
# 	text: 'Hello'
# '''

# class MainApp(App):
# 	def build(self):
# 		return Builder.load_string(kv)

# MainApp().run()

############################################ retorna um widget diretamente

# import kivy
# from kivy.app import App
# from kivy.uix.label import Label

# class MainApp(App):
#         def build(self):
#                 return Label(text='Hello!')

# MainApp().run()

############################################ busca o arquivo .kv por convencao
# import kivy
# from kivy.app import App

# class MainApp(App):
# 	pass

# MainApp().run()

############################################ busca o arquivo .kv por convencao. Label recebe msg como parametro (app.msg)
import kivy
from kivy.app import App

class MainApp(App):
	msg = 'Hello!'

MainApp().run()
