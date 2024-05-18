import tkinter as tk
import random


"""
Author: David Galstyan
Description: This is a game “Who wants to be a millionaire”. The user enters the nickname,
            then plays the game against 10 random questions.There are 3 helpsprovided during the game.
            Each help can be used just once. At the end of the game, the user is displayed in the top players board.
"""


questions = [
	"What is the capital of France?Paris,Moscow,Yerevan,Berlin",
	"What is 2 + 2?4,3,5,6",
	"What is the capital of Georgia?Tbilisi,Moscow,Yerevan,Berlin",
	"What is the largest planet in our solar system?Jupiter,Earth,Mars,Venus",
	"What is the main ingredient in guacamole?Avocado,Tomato,Cucumber,Carrot",
	"What is the freezing point of water in Celsius?0,32,-1,100",
	"What is the chemical symbol for gold?Au,Ag,Fe,Pb",
	"Which country is known as the Land of the Rising Sun?Japan,China,India,Armenia",
	"What is the capital of Austria?Veinne,Moscow,Yerevan,Berlin",
	"Who wrote 'Romeo and Juliet'?William Shakespeare,Mark Twain,Charles Dickens,Jane Austen",
    "What is the square root of 16?4,3,5,6",
    "What gas do plants absorb from the atmosphere?Carbon dioxide,Oxygen,Nitrogen,Hydrogen",
    "What is the longest river in the world?Nile,Amazon,Yangtze,Mississippi",
    "Which planet is known as the Red Planet?Mars,Venus,Mercury,Saturn",
	"How many continents are there on Earth?7,5,6,8",
    "What is the main language spoken in Brazil?Portuguese,Spanish,English,French",
    "What is the capital of Italy?Rome,Venice,Milan,Florence",
	"Which element has the atomic number 1?Hydrogen,Helium,Lithium,Oxygen",
    "What is the largest mammal in the world?Blue whale,Elephant,Great white shark,Giraffe",
	"What is the smallest prime number?2,1,3,5",
]

def get_index():
	index = []
	while len(index) < 10:
		i = random.randint(0, len(questions) -1)
		if i not in index:
			index.append(i)

	return index

def get_questions(ind):
	quests = []
	for i in ind:
		quests.append(questions[i])

	return quests

def get_questions_dict(quests):
	questions_dict = {}
	for question in quests:
		q, a = question.split("?")
		questions_dict[q] = a.split(",")

	return questions_dict



def on_button_click():
    name = entry.get()
    if name:
        root.destroy()
        open_second_window(name)

def open_second_window(name):
    second_window = tk.Tk()
    second_window.title("Welcome")
    second_window.configure(bg='#142666')

    label = tk.Label(second_window, text=f"Hello, {name}!")
    label.pack(pady=20)
    label.configure(bg='#142666',fg='#8392c9', font=('Roboto', 10, 'bold'))

    button = tk.Button(second_window, text="Start", command=lambda: [second_window.destroy(), open_third_window()])
    button.pack(pady=10)
    button.configure(bg='#8392c9')

    second_window.mainloop()

def open_third_window():
    third_window = tk.Tk()
    third_window.title("Who Wants To Be A Millionaire?")

    label = tk.Label(third_window, text="This is the main script window.")
    label.pack(pady=20)

    main_script_label = tk.Label(third_window, text="Here you can write your main script.")
    main_script_label.pack(pady=10)

    close_button = tk.Button(third_window, text="Close", command=third_window.destroy)
    close_button.pack(pady=10)

    third_window.mainloop()


root = tk.Tk()
root.title("Name Input")
root.configure(bg='#142666')

frame = tk.Frame(root)
frame.pack(pady=20, padx=20)
frame.configure(bg='#142666')

label = tk.Label(frame, text="Enter your name", fg='#8392c9', font=('Roboto', 10, 'bold'))
label.pack(pady=1)
label.configure(bg='#142666')

entry = tk.Entry(frame)
entry.pack(pady=10)

button = tk.Button(frame, text="Submit", command=on_button_click)
button.pack(pady=1)
button.configure(bg='#8392c9')

root.mainloop()