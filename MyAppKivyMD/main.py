from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MainApp(MDApp):
    def build(self):
        MDLabel.halign = "center"
        return MDLabel(text="Hello from KivyMD!")


app = MainApp(title="First app on KivyMD")
app.run()
