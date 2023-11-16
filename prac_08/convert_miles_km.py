"""
CP1404 Prac
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesKiloConvertApp(App):
    output_text = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (450, 300)
        self.title = "Miles Km Convert"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_miles(self, text):
        result = self.check_number(text) * MILES_TO_KM
        self.output_text = str(result)

    def handle_increment(self, text, diff):
        new_miles = self.check_number(text) + float(diff)
        self.root.ids.input_number.text = str(new_miles)

    def check_number(self, text):
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesKiloConvertApp().run()
