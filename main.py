import speech_recognition as sr
import os
import webbrowser
import pywhatkit as kt
from pynput.keyboard import Key, Controller

keyboard = Controller()
"""Activate the keyboard function from pywhatkit"""

recording = sr.Recognizer()
"""Initiate recording function from speech_recognition"""

with sr.Microphone(device_index=1) as source:
    """
    On 'sr.Microphone(device_index=1)' the device index is personal, it is my microphone(i had pick one microphone because i had a few other that i dont use).
    You can also leave it empty and it will use your default microphone "(sr.Microphone())'
    You can get your microphone list by running this on a empty python file:

    import speech_recognition as sr
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

    This will print all your microphones with the index so that you can change your microphone selected by the program.
    Example:
    Microphone with name "Microsoft Sound Mapper - Input" found for `Microphone(device_index=0)`
    Microphone with name "Microphone (Razer Seiren Mini)" found for `Microphone(device_index=1)`

    In my case i use the Razer Seiren Mini which is (device_index=1)
    """ 
    recording.adjust_for_ambient_noise(source)
    print("Please Say something:")
    audio = recording.listen(source)

try:
    """
    This will try to undertand what you said, and turn it into a string
    The first two options will only open a file, with its directory
    The third and fourth options are to 'play' (as if you where using your play key on a keyboard)
    and to type whatever you want to type and pressing enter after finishing typing.
    The other five options after type are to open specific websites chosen by me.
    The last options is to open a new google window(or a tab if google is already open) and do the search you said after 'search'
    """
    if recording.recognize_google(audio) == "open valorant":
        os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games\VALORANT.lnk")

    elif recording.recognize_google(audio) == "open League of Legends":
        os.startfile(r"C:\Users\manuh\Desktop\LeagueClient.lnk")
    

    elif recording.recognize_google(audio) == "play":
        keyboard.press(Key.media_play_pause)
        keyboard.release(Key.media_play_pause)

    elif recording.recognize_google(audio)[:4] == "Type" or "type":
        keyboard.type(recording.recognize_google(audio)[4:])
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    elif recording.recognize_google(audio) == "open email":
        webbrowser.open_new("https://outlook.live.com/mail/0/")

    elif recording.recognize_google(audio) == "open LinkedIn":
        webbrowser.open_new("https://www.linkedin.com/feed/")

    elif recording.recognize_google(audio) == "open Spotify":
        webbrowser.open_new("https://open.spotify.com/#_=_")       

    elif recording.recognize_google(audio) == "open YouTube":
        webbrowser.open_new("https://www.youtube.com/")

    elif recording.recognize_google(audio) == "open WhatsApp":
        webbrowser.open_new("https://web.whatsapp.com/")

    elif recording.recognize_google(audio)[:6] == "search":
        kt.search(recording.recognize_google(audio)[7:])

    else:
        print("You said: \n" + recording.recognize_google(audio))
except Exception as e:
   print(e)