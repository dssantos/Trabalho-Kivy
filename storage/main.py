import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.storage.jsonstore import JsonStore

store = JsonStore('aluno.json')

store.put('fulano', cpf='111', nome='Fulano', turma='INF28')

for item in store.find(cpf='111'):
    x = '\nIndice: ' + item[0] + '\nChaves/Valores:\n' + str(item[1])
    print(x)

class MainApp(App):
	def build(self):
		return Label(text=x)

MainApp().run()