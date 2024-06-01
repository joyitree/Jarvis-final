# take command in this python file.

import eel
import time
import pyttsx3
import wikipedia
import pyautogui
import requests
from PIL import Image
from datetime import datetime
import speech_recognition as sr
from engine.config import ASSISTANT_NAME

                             # speak function
def speak(text, use_eel = True):
    ''' it converts text to speech '''
    
    text = str(text).capitalize()
    engine=pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    
    if use_eel:
        eel.DisplayMessage(text)
        eel.receiverText(text)
    
    
    engine.say(text)
    engine.runAndWait()
 
                                # greet user function
    
def greetUser(username):
    '''Greets the user according to the time'''
    
    hour = datetime.now().hour
    
    greeting = "morning" if 6 <= hour < 12 else "afternoon" if 12 <= hour < 18 else "evening" if 18 <= hour < 21 else "night"    
    
    speak(f"Good {greeting}, {username}", use_eel=False)
    speak(f"I am {ASSISTANT_NAME}. Present at your service", use_eel=False)

def takecommand():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        eel.DisplayMessage("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 200
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 6)
        
    try: 
        print('Recognizing!!')
        eel.DisplayMessage("Recognizing!!")
        query = r.recognize_google(audio, language='en-in')
        print(f"user : {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
        
        
    except Exception as e:
        return ''
    
    return query.lower()
    
    
@eel.expose
def allCommands(message=1):
    
    '''This func handles all the commnads from the user
    and address them accordingly. It imports necessary functions 
    from the engine.featues package to accomplish the task.'''
    
    if message == 1:
        query = takecommand() # it will fetch speech to text
        print(query)
        eel.senderText(query) # Chat History : sender
        
    else:
        query = message
        print(f"user : {query}")
        eel.senderText(query) # Chat History : sender
        
    try:
    
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
            
        # youtube automation
        elif "on youtube" in query or "youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
        
        elif 'close' in query:
            from engine.features import close_application
            close_application(query)
        
        # whatsapp automation
        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp
            message = ""
            contact_no, name = findContact(query)
            if(contact_no != 0):

                if "send message" in query:
                    message = 'message'
                    speak("what message to send")
                    query = takecommand()
                    
                elif "phone call" in query:
                    message = 'call'
                else:
                    message = 'video call'
                    
                whatsApp(contact_no, query, message, name)
        
        # Email Sending
        elif "email" in query or "gmail" in query or "mail" in query:
            from engine.features import findEmail, send_email
            email, name = findEmail(query)
            if(email != 0):
                receiver_address = email
                speak("What should be the subject ma'am?")
                subject = takecommand().capitalize()
                speak("What is the message ma'am")
                message = takecommand().capitalize()
                speak("Sending the email..")
                if send_email(receiver_address, subject, message):
                    speak("I've sent the email, sir")
                else:
                    speak("Something went wrong while I was sending the mail,ma'am")
                    
        # Current Time
        elif "time" in query:
            from engine.features import time_am_pm
            time_now = time_am_pm()
            speak(f'The time is {time_now}')
            print(f'The time is {time_now}')
        
        # Current Date 
        elif "date" in query:
            from engine.features import format_date
            today_date = format_date()
            speak(f'Today is {today_date}')
            print(f'Today is {today_date}')
            
        # Jarvis taking Notes 
        elif "remember that" in query or "remember this" in query or "take a note" in query or "write this down" in query:
            speak("What should I remember sir")
            rememberMessage = takecommand()
            speak(f"You said me to remember {rememberMessage}")
            remember = open('note.txt', 'w')
            remember.write(rememberMessage)
            remember.close()
        
        # Jarvis access Notes 
        elif "do you remember anything" in query or "read my notes" in query:
            remember = open('note.txt', 'r')
            speak(f"You said me to remember that {remember.read()}")
        
        # News 
        elif "news" in query or "headline" in query:
            from engine.features import get_latest_news
            news = get_latest_news()
            speak("I'm reading out the latest news headlines, sir")
            for headline in news:
                speak(headline)
        
        #Ip Address
        elif "ip adress" in query or "my ip" in query:
            from engine.features import find_my_ip
            ip_add = find_my_ip()
            speak(f"ma'am, your ip adress is: {ip_add}")
            print(f"Ip Address: {ip_add}")
        
        # Weather Forecast
        elif "weather" in query or "forecast" in query or "temperature" in query or "climate" in query:
            from engine.features import get_weather_report, findCityName
            city = findCityName(query)
            # User has provided any city name 
            if city!= None:
                speak(f"Getting weather report for the city {city}....")
                weather, temperature, feels_like = get_weather_report(city)
            else:
                city = "Kolkata" # HARD CODE as of now
                speak(f"Getting weather report for your city Kolkata")  
                weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
        
        # Wikipedia Search 
        elif 'wikipedia' in query:
            try :
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=4)
                speak("According to Wikipedia ")
                print(results)
                speak(results)

            except Exception:
                speak("Sorry Sir, i can't find anything such like that on the wikipedia. ")
        
        # JARVIS abbrevation
        elif "stands for" in query or "your full form" in query:
            speak('JARVIS stands for JUST A RATHER VERY INTELLIGENT SYSTEM')
            
        # Joke 
        elif "joke" in query:
            from engine.features import get_random_joke
            speak("Hope you like this one, ma'am")
            joke = get_random_joke()
            speak(joke)
        
        # Advice
        elif "advice" in query:
            from engine.features import get_random_advice
            speak("Here's and advice for you, ma'am")
            advice = get_random_advice()
            speak(advice)
        
        # Trending Movies
        elif "trending movies" in query:
            from engine.features import get_trending_movies
            movies = get_trending_movies()
            speak("Some of the trending movies are:")
            for movie in movies:
                speak(movie)
        
        # Screenshot
        elif "take screenshot" in query or "take a screenshot" in query or "capture the screen" in query:
            speak("By what name do you want to save the screenshot?")
            name = takecommand()
            name = f'{name}.png'
            speak("Alright ma'am, taking screenshot...")
            pyautogui.screenshot(name)
            speak("The screenshot has been succesfully captured")
            speak("For your convinence I am displaying it on the screen")
            sc = Image.open(name)
            sc.show(sc)
        
        # Drawing using Turtle 
        elif "draw rdj" in query or "draw robert downey junior" in query or "draw tony stark" in query:
            from engine.features import draw
            speak("Drawing using turtle..")
            draw("rdj")
            
        elif "draw iron man" in query:
            from engine.features import draw
            speak("Drawing iron man ASCII animation using turtle...")
            draw("ironman")
            
        elif "draw tom holland" in query or "draw spiderman" in query:
            from engine.features import draw
            speak("Drawing using turtle..")
            draw("tom holland")
            
        elif "draw vijay" in query or "draw spuerstar vijay" in query:
            from engine.features import draw
            speak("Drawing using turtle..")
            draw("vijay")
            
        elif "bts" in query:
            from engine.features import draw
            speak("Drawing using turtle..")
            draw("bts")
            
        # System Performance
        elif "pc stats" in query or "system stats" in query or "system performance" in query or "pc performance" in query:
            from engine.features import get_pc_stats
            cpu_usage, cpu_Ghz, used_mem, total_mem, mem_usage_percentage, gpu_usage, gpu_temp = get_pc_stats()
            
            speak(f'Current CPU utilization is {cpu_usage}% with a clock speed of {cpu_Ghz: .2f} giga hertz')
            print(f'CPU: {cpu_usage}% {cpu_Ghz: .2f}GHz')
            
            speak(f'{used_mem: .2f}GB of RAM out of total {total_mem: .2f}GB is in use, that comes out to be {mem_usage_percentage}%')
            print(f'RAM: {used_mem: .2f}/{total_mem: .2f}GB ({mem_usage_percentage})%')
            
            if gpu_usage != None and gpu_temp != None:
                speak(f'and GPU utilization is {gpu_usage}% working at a temperature of {gpu_temp}℃')
                print(f'GPU: {gpu_usage}% ({gpu_temp}℃)')
        
        # Google Translate
        elif "translate" in query:
            from engine.features import translate_text
            translated_text = translate_text(query)
            speak(translated_text)
            print(translated_text)
        
        # System going offline
        elif 'offline' in query or 'goodbye' in query or 'bye' in query:
            speak('Alright mam, going offline. It was nice working with you')
            pyautogui.hotkey('alt', 'f4')
        
        # Introduction
        elif "introduce yourself" in query or "tell me about yourself" in query:
            speak("Jarvis system was designed as JUST A RATHER VERY INTELLIGENT SYSTEM. I can assist you with a varity of system tasks, like opening documents, searching websites, creating emails, automating whatsapp, getting the current weather and trending headlines and many more")
            speak("I'm a modular program, that can adapt to my environment as needed by my user")
        
        # Working of Jarvis
        elif "explain how you work" in query:
            speak("This can get complicated, may be let me explain how I work, and you can just sit back, or whatever you humans are doing lately.")
            speak("I only listen for the one set activation phrase 'jarvis'. Once I'm paying attention you can say your request, usually it is some mundane task like 'what is the weather today?', then I have to translate that dribble into something that i can understand, so i connect to google, and use their speech-to-text engine to change the sounds to words and a make a data stream. Then I have to pipeline that query into my architecture to showcase your result. Like in this example after processing your query, it comes back as check weather so I access weather API then speak back the weather report i get. I then go back to waiting to be called for the next boring task and repeat that over and over.")
        
        # Internet Speed 
        elif "speed test" in query or "internet speed" in query or "download speed" in query or "upload speed" in query:
            # from engine.features import get_internet_speed
            # speak("Wait a few seconds ma'am, calculating your internet speed..")
            # download_speed, upload_speed = get_internet_speed()
            # speak(f"ma'am, we hve {download_speed} Megabits per second downloading speed and {upload_speed} Megabits per second uploding speed")
            # print(f"Download Speed: {download_speed} Mbps")
            # print(f"Upload Speed: {upload_speed} Mbps")      
            
            speak("Wait a few seconds ma'am, calculating your internet speed..")
            import speedtest
            st=speedtest.Speedtest()
            # Get best server based on ping
            st.get_best_server()
            dl=st.download()
            dl=dl/1e6
            ul=st.upload()
            ul=ul/1e6
            speak(f"ma'am, we hve {dl:.2f} Megabits per second downloading speed and {ul:.2f} Megabits per second uploding speed")
            print(f"Download Speed: {dl:.2f} Mbps")
            print(f"Upload Speed: {ul:.2f} Mbps") 
        
        # Music Playback
        elif "play" in query:
            speak("Ok ma'am")
            from engine.features import play_song
            driver =play_song(query)
            while True:
                from engine.features import control_music
                query = takecommand().lower()
                # from engine_py.helper import remove_words
                # wd_rmv=['jarvis','hay jarvis']
                # query = remove_words(query,wd_rmv)
                control_music(driver, query)
                if "play" in query:
                    driver.quit()
                    time.sleep(2)
                    # play_song(query)
                    
                elif 'quit' in query or 'close' in query:
                    driver.quit()
                    break
                
        # battery power of system 
        elif "battery" in query or "power" in query:
            import psutil
            battery = psutil.sensors_battery()
            percentage=battery.percent
            speak(f"your system have {percentage} percent battery")
        
        # internet speed 
        elif "my location" in query or "whre i am" in query or "where we are" in query:
            speak("wait let me check")
            try:
               response = requests.get('https://ipinfo.io')
               data = response.json()
               city=data['city']
               region = data['region']
               country = data['country']
               speak(f"i am not sure, but i think the city is {city}, the region is {region} and the country name start with {country}")
            except Exception as e:
                speak("sorry, due to network issue i can't get the information")
              
        #volume control
        elif "volume up" in query:
            pyautogui.press("volumeup")
        elif "volume down" in query:
            pyautogui.press("volumedown")
        elif "volume mute" in query or "mute" in query:
            pyautogui.press("volumemute") 
        

        else:
            # HugChat AI 
            from engine.features import chatBot
            speak("Getting information, ma'am...")
            chatBot(query)   
        
        # elif 'chrome' in query:
        #     from engine.features import close_web
        #     close_web(query)
    except:
        print("error")
    
    eel.ShowHood()
    
    
    
    
    
