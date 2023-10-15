"""
CP1404 Practical
"""

COLOUR_TO_CODE = {"apricot": "#fbceb1",
                  "aqua": "#00ff",
                  "aquamarine2": "#76eec6",
                  "baby blue": "#89cff0",
                  "baby pink": "f4c2c2",
                  "banana yellow": "#ffe135",
                  "beige": "#f5f5dc",
                  "blanched almond": "#ffebcd",
                  "bone": "#e3dac9",
                  "brick red": "#cb4154"}
colour = input("What colour would you like the code of?: ").lower()
while colour != "":
    try:
        print(f"{colour} is {COLOUR_TO_CODE[colour]}")
    except KeyError:
        print("Colour not included")
    colour = input("What colour would you like the code of?: ").lower()