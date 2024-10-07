hoimport speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
import requests
import translate
import pywhatkit
import pywikihow
import google.generativeai as genai


model = genai.GenerativeModel('gemini-pro')
GOOGLE_API_KEY = "OpenAI API Key"

genai.configure(api_key=GOOGLE_API_KEY)

def prompt():
    text = query
    input=str(text)
    response = model.generate_content(input)
    print(response.text)
    speak(response.text)
    return response



engine = pyttsx3.init()
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('volume',10)

def voice_change(v):
    x = int(v)
    engine.setProperty('voice', voices[x].id)
    speak("done sir")


#speak function
def speak(audio):
    engine.say(audio)
    engine.ru


#time function
def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)


#date function
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)


def checktime(tt):
    hour = datetime.datetime.now().hour
    if ("morning" in tt):
        if (hour >= 6 and hour < 12):
            speak("Good morning sir")
        else:
            if (hour >= 12 and hour < 18):
                speak("it's Good afternoon sir")
            elif (hour >= 18 and hour < 24):
                speak("it's Good Evening sir")
            else:
                speak("it's Goodnight sir")
    elif ("afternoon" in tt):
        if (hour >= 12 and hour < 18):
            speak("it's Good afternoon sir")
        else:
            if (hour >= 6 and hour < 12):
                speak("Good morning sir")
            elif (hour >= 18 and hour < 24):
                speak("it's Good Evening sir")
            else:
                speak("it's Goodnight sir")
    else:
        speak("it's night sir!")


#welcome function
def wishme():
    speak("Welcome Back")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning sir!")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon sir")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening sir")
    else:
        speak("Goodnight sir")

    speak("Jarvis at your service, Please tell me how can i help you?")


def wishme_end():
    speak("signing off")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening")
    else:
        speak("Goodnight.. Sweet dreams")
    quit()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def main():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source)

        print("Recognizing Now .... ")


        # recognize speech using google

        try:
            print("You have said ")
            query = r.recognize_google(audio)
            print(query)


        except Exception as e:
            print("Error :  " + str(e))
            
            return "None"

        return query




def new():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        speak("Ok sir please tell me again")

        audio = r.listen(source)

        print("Recognizing Now .... ")


        # recognize speech using google

        try:
            query = r.recognize_google(audio)
            print(query)
            speak("ok sir")


        except Exception as e:
            print("Error :  " + str(e))
            
            return "None"

        return query



        # write audio
        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("hv1214293@gmail.com", "H@rsh2006")
    server.sendmail("user-name@xyz.com", to, content)
    server.close()


#screenshot function
def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\admin\\OneDrive\\Pictures\\Screenshots\\ss.png")


#battery and cpu usage
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is at ' + usage)
    print('CPU usage is at ' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    print("battery is at:" + str(battery.percent))


#joke function
def jokes():
    j = pyjokes.get_joke()
    print(j)
    speak(j)


#weather condition
def weather():
    api_key = "YOUR-API_KEY" #generate your own api key from open weather
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    speak("tell me which city")
    city_name = main()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        r = ("in " + city_name + " Temperature is " +
             str(int(current_temperature - 273.15)) + " degree celsius " +
             ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
             ", humidity is " + str(current_humidiy) + " percent"
             " and " + str(weather_description))
        print(r)
        speak(r)
    else:
        speak(" City Not Found ")


def personal():
    speak(
        "I am Jarvis, version 1.0, I am an AI assistent, I am developed by Harsvardhan on 13 november 2022 in INDIA"
    )
    speak("Now i hope you know me")


if __name__ == "__main__":
    wishme()
    while (True):
        query = main().lower()

        #time

        if ('time' in query):
            time()

#date

        elif ('date' in query):
            date()

    
        elif ('jarvis play' in query or 'please play' in query or 'play' in query):
            question = new()
            pywhatkit.playonyt(question)
            speak("Ok Sir i Am Playing")
        elif ('jarvis find' in query):
            harsh = new()
            pywhatkit.search(harsh)
            speak("This is I Found from Google")


        elif ('open google' in query):
            wb.open_new_tab('https://www.google.com/')

        elif ('open youtube' in query):
            wb.open_new_tab('https://www.youtube.com/')

        elif ('open replit' in query or 'open code' in query):
            wb.open_new_tab('https://replit.com/')
        elif ('play youtube music' in query):
            wb.open_new_tab('https://www.youtube.com/watch?v=V5En3Ks3OjE')
        elif('track speed post' in query or 'track post' in query):
            wb.open_new_tab('https://www.indiapost.gov.in/_layouts/15/dop.portal.tracking/trackconsignment.aspx')
        elif('download aadhar card' in query):
            wb.open_new_tab('https://myaadhaar.uidai.gov.in/genricDownloadAadhaar')
        elif('open sarkari result' in query):
            wb.open_new_tab('https://www.sarkariresult.com/')
        elif ('dictionary' in query or 'translate' in query):
            speak('What you want to search in your intelligent dictionary?')
            translate = new()
            wb.open('https://www.google.com/search?q=google+translate&oq=google+trans&aqs=chrome.0.35i39i67j69i57j0i67j0i131i433i512l2j0i433i512l2j0i131i433j0i433i512j0i131i433.6589j0j7&sourceid=chrome&ie=UTF-8'+ translate)
        elif('youtube search' in query):
            speak("what you want to search")
            command = new()
            wb.open('https://www.youtube.com/results?search_query=' + command)
        
        elif('Jarvis' in query or 'friend' in query or 'problem' in query):
            speak("please tell me sir")
            ask = new()
            pywhatkit.search(ask)
            speak("Are you satisfied sir")

                
        elif ('google search' in query):
            import wikipedia as googleScrape
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            query = query.replace("google","")
            speak("This is what i found on the web")

            try:
                pywhatkit.search(query)
                result = googleScrape.summary(query,3)
                speak(result)

            except:
                speak("No Speakable Data Available")
#personal info
        elif ("tell me about yourself" in query):
            personal()
        elif ("about you" in query):
            personal()
        elif ("who are you" in query):
            personal()
        elif ("yourself" in query):
            personal()

        

        elif ("developer" in query or "tell me about your developer" in query
              or "father" in query or "who developed you" in query
              or "developer" in query):
            speak("My self jarvis version 3.8 master harsvardhan developed me and i was only obey there command")

#searching on wikipedia

        elif("wikipedia search" in query):
            search = main()
            wb.open_new_tab('https://en.wikipedia.org/wiki/' + search)

#sending email

        elif ("send email" in query):
            try:
                speak("What is the message for the email")
                content = main()
                to = 'reciever@xyz.com'
                sendEmail(to, content)
                speak("Email has sent")
            except Exception as e:
                print(e)
                speak("Unable to send email check the address of the recipient")

        
#sysytem logout/ shut down etc

        elif ("logout" in query):
            os.system("shutdown -1")
        elif ("restart" in query):
            os.system("shutdown /r /t 1")
        elif ("shut down" in query):
            os.system("shutdown /r /t 1")

        elif("tell me about weather" in query or "whats the weather" in query or "weather" in query):
            wb.open_new_tab('https://weather.com/en-IN/?Goto=Redirected')
            
        elif('play music' in query):
            wb.open_new_tab('https://www.youtube.com/watch?v=sqmNziU3OxQ&list=RDCLAK5uy_nGukXBMKlUZeW_yN6CTk6VeO-7GBqnZuo&start_radio=1')

#reminder function

        elif ("create a reminder list" in query or "reminder" in query):
            speak("What is the reminder?")
            data = main()
            speak("You said to remember that" + data)
            reminder_file = open("data.txt", 'a')
            reminder_file.write('\n')
            reminder_file.write(data)
            reminder_file.close()


#screenshot
        elif ("screenshot" in query or "take screenshot" in query):
            screenshot()

#cpu and battery usage
        elif("cpu and battery" in query or "battery" in query or "cpu" in query):
            cpu()

#jokes
        elif ("tell me a joke" in query or "joke" in query):
            jokes()

#weather
        elif ("weather" in query or "temperature" in query):
            weather()

#jarvis features
        elif ("tell me your powers" in query or "help" in query or "features" in query):
            features = ''' i can help to do lot many things like..
            i can tell you the current time and date,
            i can tell you the current weather,
            i can tell you battery and cpu usage,
            i can create the reminder list,
            i can take screenshots,
            i can send email to your boss or family or your friend,
            i can shut down or logout or hibernate your system,
            i can tell you non funny jokes,
            i can open any website,
            i can search the thing on wikipedia,
            i can change my voice from male to female and vice-versa
            And yes one more thing, My boss is working on this system to add more features...,
            tell me what can i do for you??
            '''
            print(features)
            speak(features)

        elif ("hii" in query or "hello" in query or "goodmorning" in query or "goodafternoon" in query or "goodnight" in query or "morning" in query or "noon" in query or "night" in query):
            query = query.replace("jarvis", "")
            query = query.replace("hi", "")
            query = query.replace("hello", "")
            if ("morning" in query or "night" in query or "goodnight" in query or "afternoon" in query or "noon" in query):
                checktime(query)
            else:
                speak("what can i do for you")

#changing voice
        elif ("voice" in query):
            speak("for female say female and, for male say male")
            q = main()
            if ("female" in q):
                voice_change(1)
            elif ("male" in q):
                voice_change(0)
        elif ("male" in query or "female" in query):
            if ("female" in query):
                voice_change(1)
            elif ("male" in query):
                voice_change(0)


        elif("" in query):
            prompt()
#exit function

        elif ('i am done' in query or 'bye bye jarvis' in query or 'go offline jarvis' in query or 'bye' in query or 'nothing' in query or 'good bye' in query):
            wishme_end()
