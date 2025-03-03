<<<<<<< HEAD
import speech_recognition as sr
import webbrowser 
import pyttsx3
from data import most_visited_websites, installed_apps_and_programs_dict
import subprocess
import requests
from datetime import datetime, timedelta
import google.generativeai as genai
from dotenv import load_dotenv
import os
import yt_dlp

# Load environment variables from API_keys.env
load_dotenv("API_keys.env")
# Retrieve API keys
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
GEMINI_API = os.getenv("Gemini_api")

engine = pyttsx3.init() #intialising pyttsx3 module

def listen():
    #to listen and recognize audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio =  r.listen(source,phrase_time_limit = 3)
    command = r.recognize_google(audio)
    print("Recognizing ...")
    print(command)
    return command

def speak(text):
    engine.say(text)
    engine.runAndWait()

def open_command(command):
    # To open an app or website
    trigger = command.replace("open ", "").strip().lower()
    if (trigger in (most_visited_websites and installed_apps_and_programs_dict)):
        try:
            result = subprocess.run(f"{installed_apps_and_programs_dict[trigger]}", shell=True)
            if result.returncode == 0:
                speak(f"Opening {trigger}")
        except Exception as e:
            speak("Unable to open the application.")
            print(f"Error opening {trigger}: {e}")
    else :
        if trigger in most_visited_websites:
            webbrowser.open(most_visited_websites[trigger])
            speak(f"Opening {trigger}")
        elif trigger in installed_apps_and_programs_dict:
            try:
                result = subprocess.run(f"{installed_apps_and_programs_dict[trigger]}", shell=True)
                if result.returncode == 0:
                    speak(f"Opening {trigger}")
            except Exception as e:
                speak("Unable to open the application.")
                print(f"Error opening {trigger}: {e}")
        else :
            speak("Could not recognize what you want to open, searching it on google")
            webbrowser.open(f"https://www.google.com/search?q={trigger}")

def search(command):
    trigger = command.replace("open ", "").strip().lower()
    speak(f"Searching {command}")
    webbrowser.open(f"https://www.google.com/search?q={trigger}")

def news():
    today = datetime.today().strftime('%Y-%m-%d')
    NEWS_URL = f"https://newsapi.org/v2/everything?q=India&sortBy=publishedAt&apiKey={NEWS_API_KEY}" #used news api
    try:
        response = requests.get(NEWS_URL)
        news_data = response.json()
        if news_data.get("status") == "ok":
            articles = news_data.get("articles", [])[:5]  # Get top 5 news headlines          
            if not articles:
                print("No news articles found.")
                return
            news_headlines = "Here are the top news headlines:\n"
            for i, article in enumerate(articles, start=1):
                news_headlines += f"{i}. {article['title']}\n"
            print(news_headlines)
            speak(news_headlines)
        else:
            print(f"Error fetching news: {news_data.get('message', 'Unknown error')}")    
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")

def play_videos(command):
    trigger = command.replace("play", "").lower()
    search_url = f"ytsearch1:{command}"  # Search for top result
    ydl_opts = {"quiet": True}          # to keep scipt output clean

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(search_url, download=False)
        if "entries" in info and info["entries"]:
            video_url = info["entries"][0]["webpage_url"]
            print(f"Playing: {video_url}")
            webbrowser.open(video_url)
        else:
            print("No video found.")

def AI(command):    
    genai.configure(api_key=GEMINI_API)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(command)
    print(response.text)
    speak(response.text)

def processCommand(command):
    if command.startswith("open "):
        open_command(command)
    elif "news" in command :
        news()
    elif command.startswith("play"):
        play_videos(command)
    elif command.startswith("search"):
        search()
    else :
        AI(command)

#main code
speak("Intializing Jarvis ...")
while True :
    try :
    #Listen to what user says
        command = listen()
        #try to fire trigger word
        if (command.lower() == "jarvis"):
            print("Yes sir!")
            speak("Yes sir!")
            #Listen for command

            try : 
                command = listen()
                processCommand(command)
            except Exception as e:
                print("Error {0}".format(e))

    except Exception as e:
        print("Error {0}".format(e))
