import kivy.app
import kivy.uix.label


class MainApp(kivy.app.App):
    def build(self):
        return kivy.uix.label.Label(text="Hello Kivy!")


app = MainApp(title="First app on Kivy")
app.run()
