import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Marvel(BoxLayout):
	def hulk_esmaga(self):
		self.ids.hulk.text = "Hulk: \nDEUS FRACO!"
		self.ids["loki"].text = "Loki: \n!! >_< !!"
		self.ids["loki"].font_size = '60sp'

	def reset(self):
		self.ids.hulk.text = "Pressione para esmagar"
		self.ids["loki"].text = 'Loki: \nEU SOU UM DEUS!'
		self.ids["loki"].font_size = '30sp'

class MainApp(App):
	pass

if __name__ == '__main__':
    MainApp().run()