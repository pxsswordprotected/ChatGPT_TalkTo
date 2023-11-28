import speech_recognition as sr
import openai

recognizer = sr.Recognizer()

with sr.Microphone() as source: #creates a Microphone object and opens a connection to the system's default microphone
    print("Say something:") #prints a message to the console, prompting the user to say something.
    audio = recognizer.listen(source) # records audio from the microphone using the listen method of the Recognizer object. The recorded audio is stored in the audio variable

try:
    text_input = recognizer.recognize_google(audio)
    print("You said:", text_input)
except sr.UnknownValueError:
    print("Sorry, could not understand audio.")
except sr.RequestError as e:
    print(f"Error with the speech recognition service: {e}")
