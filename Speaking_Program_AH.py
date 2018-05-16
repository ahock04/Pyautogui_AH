import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("Can you let me use your bat today Ryan?")

answer = pg.prompt("Enter yes or no below.")

if answer == "yes":
    speak.Speak("Thank you Ryan, I appreciate you.")
elif answer == "no":
    speak.Speak("That is not very nice, you should let me use your bat Ryan")
else:
    speak.Speak("Say yes or no or I will take your bat")
    

speak.Speak("What video would you like to watch?")

video = pg.prompt("Enter your video below")

speak.Speak("Ok, let's look for " + video + " on YouTube.")

wb.open("https://www.youtube.com/results?search_query=" + video)
