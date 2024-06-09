"""
    Author: David Galstyan

    Description: This is a script which executes voice commands.
"""

import speech_recognition as sr
import os

# Initialize the recognizer
r = sr.Recognizer()


def recognize_speech_from_microphone():
    with sr.Microphone() as source:
        print("Listening for the command to open Google Chrome...")
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print("You said: " + command)
            return command
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return None


def main():
    while True:
        command = recognize_speech_from_microphone()
        if command and "open Google Chrome" in command.lower():
            print("Opening Google Chrome...")
            os.system("start chrome")  # For Windows
            # os.system("open -a 'Google Chrome'")  # For macOS
            break


if __name__ == "__main__":
    main()
