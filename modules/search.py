from modules.talk import talk
import wikipedia
from googlesearch import search

def search_web(query):
    try:
        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            talk("According to Wikipedia")
            print(results)
            talk(results)
        else:
            print("No result found in Wikipedia, searching in Google")
            talk("No result found in Wikipedia, searching in Google")
            results = list(search(query, num_results=2))
            if results:
                for link in results:
                    print(link)
            else:
                print("No result found in Google.")
                talk("No result found in Google.")
    except Exception as e:
        print(e)
        print("An error occurred while searching.")
        talk("Sorry, I couldn't complete the search.")