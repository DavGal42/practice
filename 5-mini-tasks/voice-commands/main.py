"""
    Author: David Galstyan

    Description: This is a script which executes voice commands.
"""

import speech_recognition as sr
import subprocess

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to recognize speech from the microphone
def recognize_speech_from_microphone():
    with sr.Microphone() as source:
        print("Please say something...")
        audio = recognizer.listen(source)

    try:
        # Use Google Web Speech API to recognize speech
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand the audio")
        return None
    except sr.RequestError:
        print("Could not request results from the speech recognition service")
        return None

# Main function
def main():
    command = recognize_speech_from_microphone()
    if command:
        if "open chrome" in command:
            # Open Google Chrome browser
            subprocess.run(["open", "-a", "Google Chrome"])  # For macOS
            # subprocess.run(["google-chrome"])  # For Linux
            # subprocess.run(["start", "chrome"])  # For Windows
        else:
            print("Command not recognized or not supported.")

if __name__ == "__main__":
    main()
