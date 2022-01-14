
import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

def Hangman():
  chosen_word = random.choice(word_list)

  display = []
  bank = []  #User entered letters go here

  print(f'Word: {chosen_word}.')
  for letters in chosen_word:
      display += '_'

  print(logo)
  print(stages[6])
  print(display)
  lives = 6

  while '_' in display:
      guess = input("Guess a letter: ").lower()
      for position in range(len(chosen_word)):
          letter = chosen_word[position]
          if guess == letter:
              display[position] = letter
              if letter in bank:
                print('you already tried ' + guess + ', try again')
                guess = input("Guess a letter: ").lower()
                for position in range(len(chosen_word)):
                    letter = chosen_word[position]
                    if guess == letter:
                        display[position] = letter
      if guess not in chosen_word:
        if guess in bank:
            print('you already tried ' + guess + ', try again')
            guess = input("Guess a letter: ").lower()
            for position in range(len(chosen_word)):
                    letter = chosen_word[position]
                    if guess == letter:
                        display[position] = letter
        else:
          print('Sorry ' + guess + ' is not in the word, try again')
          lives -= 1
          if lives == 0:
              print(stages[0])
              print('You Loose')
              question = input('Do you want to play again ?\n').lower()
              if question == 'yes':
                Hangman()
              elif question == 'no':
                print('Thank you for playing!')
                exit()
      print(stages[lives])
      print(display)
      bank.append(guess)
  print('You win!')

  question = input('Do you want to play again ?\n').lower()

  if question == 'yes':
    Hangman()
  elif question == 'no':
    print('Thank you for playing!')
    exit

Hangman()
