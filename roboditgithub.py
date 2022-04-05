from multiprocessing import set_forkserver_preload
import pyttsx3 #text data to speech
import datetime
import time
import random
import speech_recognition as src #pip install Speech_Recognition == mic to text
import smtplib

from email.message import EmailMessage
import pyautogui
import webbrowser as wb
import wikipedia
import requests
from newsapi import NewsApiClient
import clipboard
#import pywhatkit 
import os
import pyjokes
import string

engine = pyttsx3.init() #creating the engine
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def get_voices(voice):
    voices = engine.getProperty('voices')
    #print(voices[1].id)
    if voice ==1:
        engine.setProperty("voice",voices[0].id)
        speak("hello this is robodir")
    if voice ==2:
        engine.setProperty("voice",voices[1].id)
        speak("hello this is girl robodir ")#i didnt find any name lol 
    

def day_time():
    time = datetime.datetime.now().strftime('%I:%M:%S')#hour = I minutes = M seconds
    speak(time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    
    speak("the current date is:")

    speak(day)
    speak(month)
    speak(year)
def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("good morning sir")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir")
    elif hour >= 18 and hour < 21:
        speak("good evening sir")
    elif hour >= 21 and hour < 24:
        speak("good night sir")
    else:
        None
def nice_sentence():
    nice_senten = ["you are looking good today","happy to serve you","nice to do job with you "]
    sentence = random.choice(nice_senten)
    speak(sentence)
def roll():
    speak("okay rolling the die")
    die = ["1","2","3","4","5","6"]
    roll = []
    roll.extend(die)
    random.shuffle(roll)
    roll = (''.join(roll[0]))
    speak("i rolled a die and you get" +roll )
def wish_me():
    greeting()
    nice_sentence()
    speak("the time is:")
    time.sleep(0.5)
    day_time()
    time.sleep(0.5)
    date()
    time.sleep(0.5)
    speak("robodir as your service. how may i help you")


def search_google():
    speak("what do you want me to search for")
    search = takeCommandmic()
    wb.open('https://www.google.com/search?q='+ search )
def news():
    speak("what topic do you want to hear")
    topic = takeCommandmic()  
    newsapi = NewsApiClient(api_key = "e481838e31f84968bdf2173752afe6ce")
    data = newsapi.get_top_headlines(q = topic,language = "en",page_size=10)#topic we want to search
    newsdata = data["articles"]
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))
    speak("that is it for now. i will update you some time")
def text_to_speech():
    text = clipboard.paste()#allows you to read the copyied text
    print(text)
    speak(text)
def covid():
    r = requests.get("https://coronavirus-19-api.herokuapp.com/all")
    data = r.json()
    covid_data = f'confirmed cases: {data["cases"]} \n Deaths: {data["deaths"]} \n Recovered: {data["recovered"]}' 
    print(covid_data)
    speak(covid_data)
def screenshot():
    try:

        name_img = time.time() #current time
        name_img = 'C:\\Users\\cantu\\Desktop\\own codes\\robodit\\screenshots\\{name_img}.png'
        img = pyautogui.screenshot(name_img)
        img.show()
    except OSError as e:
        print(e)
def password():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    passlength = takeCommandmic()
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    newpass = ("".join(s[0:passlength]))
    speak(newpass)
#while True:

    #voice = int(input("press 1 for male voice and press 2 for female voice\n"))
    #get_voices()

def takeCommand_cmd():
    query=input("pls tell me how can i help you\n ")
    return query

def takeCommandmic():
    r= src.Recognizer()
    with src.Microphone() as source:#opening mic
        print("listening...") #saving the voice to audio variable
        r.pause_threshold  =1
        audio = r.listen(source)
    try:
        print("recognizing")
        query = r.recognize_google(audio, language="en-US")
        print(query)
    except Exception as e:
        print(e)
        speak("please say that again")
        
        return "None"
    return query
def flip():
    speak("flipping a coin")
    coin = ["heads","tales"]
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss = (''.join(toss[0]))
    speak("you got " + toss)
if __name__ =="__main__":
    get_voices(1)#ONE TO MAKE MAN VOICE , 2 TO GIRL VOICE
    wish_me()
    while True:
        query= takeCommandmic().lower()
        if "time" in query:
            day_time()
        elif "date" in query:
            date()
        elif "offline" in query:
            try:

                speak("closing...")
                time.sleep(0.5)
                break
            except TypeError:
                break
        



       
        elif "wikipedia" in query:
        
           speak("searching on wikipedia")
           query = query.replace("wikipedia",'')
           result = wikipedia.summary(query,sentences=2)
           print(result)
           speak(result)

        elif "f***" in query:
            speak("thats not a normal word")

        elif "google" in query:
            search_google()

        elif "hello" in query:
            speak("hello owner")

        elif "youtube" in query:
            speak("what should i search for you on youtube")
            topic = takeCommandmic()
            wb.open("https://www.youtube.com/" + topic)

        elif "weather" in query:
            city = "istanbul"#write what city you want
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=4c80c3cf38fbb5aa2482aafd65ba5891"
            res = requests.get(url)
            data = res.json()
            weather = data["weather"][0]["main"]
            temp = data["main"]["temp"] #fahrenheit
            desp = data["weather"] [0] ['description']
            temp = round((temp-32)*5/9) #to celcius
            print(f"temp is {temp} celcius")
            print(f"weather is {weather}")
            
            speak(f"wheather in {city} is")
            speak(f"temperature: {temp} celcius")
            speak(f"weather is {weather}")
        elif "news" in query:
            news()
        elif "covid" in query:
            covid()
        elif "open code" in query:
            codepath = "C:\\Users\\name\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"#enter the users folders name in the 'name' part
            os.startfile(codepath)
        elif "open document" in query:
            os.system("explorer C://{}".format(query.replace("Open",'')))
        elif "read" in query:
            text_to_speech()
        elif "joke" in query:
            speak(pyjokes.get_joke())
        elif "screenshot" in query:
            screenshot()
        elif "remember that " in query:
            speak("what do you want me to remember")
            data = takeCommandmic()
            remember = open("data.txt","w")
            remember.write(data)
            remember.close()
        elif "do you know anything" in query:
            remember = open("data.txt","r")
            speak(remember.read())
        elif "password" in query:
            password()
        elif "flip" in query:
            flip()
        elif "roll" in query:
            roll()
        elif "command" == query:
            speak("wikipedia") #allows you to search thing on wikipedia
            speak("time")#says the current time
            speak("date")#says the current date
            speak("offline")#closes robodir
            speak("google")#searches something on google
            speak("youtube")#searches something on youtube
            speak("news") #finds the news that you choosed the topic for
            speak("covid")# tells you how much deaths recoveries and cases in the whole country
            speak("weather")#tells you the weather of a certain location 
            speak("read")#robodir reads the copied text
            speak("open code")#opens vs code
            speak("open document")#opens documents folder
            speak("joke")#makes a random joke.mostly about proggraming
            speak("screenshot")# screenshots the screen
            speak("password")#creates a random password
            speak("roll a die")# rolls a die
            speak("flip a coin") #flips a coin
# http://api.openweathermap.org/data/2.5/weather?q=istanbul&units=imperial&appid=4c80c3cf38fbb5aa2482aafd65ba5891





        

        
