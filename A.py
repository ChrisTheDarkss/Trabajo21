import json
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivy.uix.button import Button
from plyer import notification

class MainApp(MDApp):
    def build(self):
        box = MDBoxLayout(orientation='vertical')
        self.texto = MDTextField()
        boton = Button(text="Guardar", on_release=self.guardar)
        box.add_widget(self.texto)
        box.add_widget(boton)
        return box

    def guardar(self, instance):
        texto = self.texto.text
        json.dump({"texto": texto}, open("datos.json", "w"))
        notification.notify(title="Guardado", message='El texto  ha sido guardado exitosamente',timeout= 5)

MainApp().run()