import random

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


def start_game(quests):
	count = 0

	for q, a in quests.items():
		print(q + "?")
		correct = a[0]
		random.shuffle(a)
		for el in a:
			print(el)
		answer = input("Enter your answer: ")
		if answer.lower() == correct.lower():
			print("Coorect!")
			count += 1
		else:
			print("Wrong. The correct answer was:", correct)
	

index = get_index()
questions = get_questions(index)
questions_dict = get_questions_dict(questions)
start_game(questions_dict)