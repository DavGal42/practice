#!/usr/bin/python3

import random

#questions = [
#	"What is the capital of France?Paris,Moscow,Yerevan,Berlin",
#	"What is the capital of Russia?Moscow,Paris,Yerevan,Berlin",
#	"What is the capital of Georgia?Tbilisi,Moscow,Yerevan,Berlin",
#	"What is the capital of Norway?Oslo,Moscow,Yerevan,Berlin",
#	"What is the capital of Canada?Ottawa,Moscow,Yerevan,Berlin",
#	"What is the capital of Belarus?Minsk,Moscow,Yerevan,Berlin",
#	"What is the capital of Ukrain?Kiev,Moscow,Yerevan,Berlin",
#	"What is the capital of Portugal?Lisbon,Moscow,Yerevan,Berlin",
#	"What is the capital of Austria?Veinne,Moscow,Yerevan,Berlin",
#	"What is the capital of Armenia?Lennakan,Moscow,Yerevan,Berlin",
#]
#
#ind = []
#while len(ind) < 5:
#	i = random.randint(0, len(questions) -1)
#	if i not in ind:
#		ind.append(i)
#
#quests = []
#for i in ind:
#	quests.append(questions[i])
#
#
#questions_dict = {}
#for question in quests:
#	q,a = question.split("?")
#	questions_dict[q] = a.split(",")
#
#count = 0
#
#for q,a in questions_dict.items():
#	print(q + "?")
#	correct = a[0]
#	random.shuffle(a)
#	for el in a:
#		print(el)
#	answer = input("Enter your answer: ")
#	if answer.lower() == correct.lower():
#		print("Coorect")
#		count += 1
#	else:
#		print("Wrong. The correct answer was:", correct)
#	
#print("You got %d/%d" %(count, len(questions_dict)))

#mstr = input("Enter a sentence: ")
#ml = mstr.split()
#
#for i in range(len(ml)):
#	ml[i] = ml[i][::-1]
#
#mstr = " ".join(ml)
#print(mstr)

#mstr = " ".join([el[::-1] for el in input("Enter a sentence: ").split()])
#print(mstr)

#ml = []
#for i in range(1, 11):
#	if i % 2 == 0:
#		ml.append(i**2)
#
#print(ml)

#tmp = [i ** 2 for i in range(1,11) if i % 2 == 0]
#print(tmp)


#mstr = input("Enter a sentence: ")
#ml = mstr.split()
#
#for i in range(len(ml)):
#	if ml[i][0] == ml[i][-1]:
#		ml[i] = ml[i].upper()
#	else:
#		ml[i] = ml[i].lower()
#mstr = " ".join(ml)
#print(mstr)

ml = [el.upper() if el[0] == el[-1] else el.lower() for el in input().split()]
mstr = " ".join(ml)
print(mstr)
