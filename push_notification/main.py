from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from plyer import notification

class NotificationDemo(BoxLayout):

    def do_notify(self):
        title = self.ids.notification_title.text
        message = self.ids.notification_text.text
        notification.notify(title, message)

class MainApp(App):

    def build(self):
        return NotificationDemo()

MainApp().run()