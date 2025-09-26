import speech_recognition as sr  # For recognizing speech
import pyttsx3  # For speaking text
import datetime  # For current time/date
import webbrowser  # For web searches

recognizer = sr.Recognizer()  # Create a recognizer
engine = pyttsx3.init()       # Create speech engine

def speak(text):
    print("Assistant:", text)         # Print response in terminal for reference
    engine.say(text)                  # Speak the text out loud
    engine.runAndWait()               # Wait for the speaking to finish

def listen():
    with sr.Microphone() as source:   # Access microphone
        print("Listening...")         # Show that assistant is listening
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        audio = recognizer.listen(source)            # Capture the audio
        try:
            command = recognizer.recognize_google(audio)  # Convert speech to text
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")     # If audio was unclear
            return ""
        except sr.RequestError as e:
            speak("Sorry, I'm having trouble connecting.") # If connection problem
            return ""

def main():
    speak("Hello! I am your voice assistant. How can I help you?")
    while True:
        command = listen()
        if "hello" in command:
            speak("Hello! How are you?")
        elif "time" in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {now}")
        elif "date" in command:
            today = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is {today}")
        elif "search" in command:
            speak("What do you want to search for?")
            query = listen()
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Searching Google for {query}")
        elif "stop" in command or "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I don't understand that command.")

if __name__ == "__main__":
    main()
