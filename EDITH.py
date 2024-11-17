import webbrowser
import datetime
from modules.talk import greet, talk
from modules.input import take_input
from modules.search import search_web
from modules.sendmail import send_email
from modules.weather_info import get_weather, get_current_city

def main():
    greet()
    while True:
        try:
            query = take_input().lower()

            if 'wikipedia' in query:
                search_web(query)

            elif 'open youtube' in query:
                webbrowser.open("https://www.youtube.com")

            elif 'open google' in query:
                webbrowser.open("https://www.google.com")

            elif 'what time is it' in query:
                time = datetime.datetime.now().strftime("%I:%M %p")
                talk("The current time is " + time)
                print("The current time is " + time)

            elif 'send email' in query or 'email' in query or 'mail' in query:
                talk("Please provide the recipient's email address.")
                recipient_email = input("Recipient's Email: ")
                talk("What is the subject of the email?")
                subject = input("Subject: ")
                talk("What message would you like to send?")
                message = input("Message: ")
                try:
                    send_email(recipient_email, subject, message)
                    talk("Email sent successfully.")
                except Exception as e:
                    print("Failed to send email:", e)
                    talk("Failed to send the email. Please try again.")

            elif 'weather' in query:
                city = get_current_city()
                if city:
                    print("Detected city:", city)
                    talk(f"Detected city {city}")
                    weather_info = get_weather(city)
                    if weather_info:
                        print("Weather forecast:", weather_info)
                        talk(f"The current weather in {city} is {weather_info}.")
                    else:
                        print("Could not retrieve weather information.")
                        talk("Could not retrieve weather information.")
                else:
                    print("Could not determine current location.")
                    talk("Could not determine current location.")

            elif 'abort' in query:
                talk("Goodbye!")
                break

        except Exception as e:
            print("An error occurred:", e)
            talk("An unexpected error occurred. Please try again.")

if __name__ == "__main__":
    main()
