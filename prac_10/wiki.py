"""
Cp1404 Practical
"""
import wikipedia

search_query = input("What would you like search for?: ")
while search_query != "":
    try:
        print(wikipedia.page(search_query).title)
        print(wikipedia.summary(search_query))
        print(wikipedia.page(search_query).url)
    except wikipedia.exceptions.DisambiguationError as e:
        print("Not specific enough...")
        print(e.options)
    search_query = input("What would you like search for?: ")
print("thanks")
