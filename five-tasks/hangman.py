# guess_word = 'armenia'

# answer = '_' * len(guess_word)
# wrong = 0

# while True:
#     if wrong == 3:
#         print('You lose!' + '\n' + 'The correct word is: ' + guess_word)
#         break

#     if '_' not in answer:
#         print('You win!')
#         break

#     letter = input('Enter a letter: ')

#     if len(letter) > 1 or not letter.isalpha():
#         print("You haven't wrote a letter!")
#         continue
#     elif letter.lower() in answer:
#         print("You've already choosen this letter")
#     elif letter.lower() not in guess_word:
#         wrong += 1
#         print(f'You have {3 - wrong} attempts left')
#     else:
#         for i in range(len(guess_word)):
#             if guess_word[i] == letter.lower():
#                 answer = answer[:i] + letter + answer[i + 1:]
#         print(answer)      