"""
CP1404 Prac
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934


class MilesKiloConvertApp(App):
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (450, 300)
        self.title = "Miles Km Convert"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_miles(self, value):
        result = float(value) * MILES_TO_KM
        self.root.ids.output_number.text = str(result)

    def handle_increment(self, number, diff):
        self.root.ids.input_number.text = number + diff


MilesKiloConvertApp().run()
