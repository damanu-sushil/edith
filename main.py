from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from googlesearch import search

app = FastAPI()

# templates = Jinja2Templates(directory="templates")
templates = Jinja2Templates(directory='templates')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

class Query(BaseModel):
    query: str

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

@app.get("/assistant", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Welcome!!"})

@app.post("/assistant2/", response_class=HTMLResponse)
async def assistant(query: Query, request: Request):
    query = query.query.lower()
    response = {"response": ""}

    if 'search' in query:
        response["response"] = search_web(query)
    elif 'open youtube' in query:
        webbrowser.open(f"https://www.youtube.com")
        response["response"] = "Opening YouTube"
    elif 'open google' in query:
        webbrowser.open(f"https://www.google.com")
        response["response"] = "Opening Google"
    elif 'what time is it' in query:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("The current time is " + time)
        response["response"] = f"The current time is {time}"
        
    elif 'send email' in query:
        response["response"] = templates.TemplateResponse("email_form.html", {"request": request})
        
    elif "stop" in query:
        response["response"] = "Goodbye!"
    else:
        response["response"] = "I'm sorry, I didn't understand that."

    return response

def search_web(query):
    try:
        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            talk("According to Wikipedia")
            print(results)
            talk(results)
        else:
            print("no result found in wikipedia, Searching in google")
            talk("no result found in wikipedia, Searching in google")
            results = list(search(query, num=2, stop=2, pause=2))
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

def send_email(recipient_email, subject, message):
    try:
        sender_email = "sushilkumardora1290@gmail.com"
        smtp_server = 'smtp.gmail.com'
        smtp_port = 465
        app_password = 'bqjdqsxnkicbhdrc'
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)

        server.login(sender_email, app_password)

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        server.sendmail(sender_email, recipient_email, msg.as_string())

        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
