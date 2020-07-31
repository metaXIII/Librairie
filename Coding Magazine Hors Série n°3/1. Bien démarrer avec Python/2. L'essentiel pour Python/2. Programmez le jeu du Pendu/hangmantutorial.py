#!/usr/bin/env python2
# coding=utf-8

from random import *

player_score = 0
computer_score = 0


def hangedman(hangman):
    graphic = [
        """
        +-----------+
        |
        |
        |
        |
        =================
        """,
        """
        +-----------+
        |           |
        |           O
        |
        |
        =================
        """,
        """
        +-----------+
        |           |
        |           O
        |          -|
        |
        =================
        """,
        """
        +-----------+
        |           |
        |           O
        |          -|-
        |
        =================
        """,
        """
        +-----------+
        |           |
        |           O
        |          -|-
        |          /
        =================
        """,
        """
        +-----------+
        |           |
        |           O
        |          -|-
        |          / \\
        =================
        """
    ]
    print graphic[hangman]


def game():
    dictionnary = ["gnu", "kernel", "linux", "pingouin", "ubuntu"]
    word = choice(dictionnary)
    word_length = len(word)
    clue = word_length * ["_"]
    tries = 6
    letters_tried = ""
    guesses = 0
    letters_right = 0
    letters_wrong = 0
    global player_score, computer_score
    while (letters_wrong != tries) and ("".join(clue) != word):
        letter = guess_letter()
        if len(letter) == 1 and letter.isalpha():
            if letters_tried.find(letter) != -1:
                print "Vous avez déjà joué la lettre ", letter
            else:
                guesses += 1
                letters_tried = letters_tried + " " + letter
                first_index = word.find(letter)
                if first_index == -1:
                    letters_wrong += 1
                    print "Sorry, ", letter, " is not what we are looking for"
                else:
                    print "Félicitations, ", letter, " is correct"
                    letters_right += 1
                    for i in range(word_length):
                        if letter == word[i]:
                            clue[i] = letter
        else:
            print "Un autre choix ?"
        if letters_wrong > 0:
            hangedman(letters_wrong - 1)
        print " ".join(clue)
        print "Guesses : ", letters_tried
        print "letters_wrong", letters_wrong
        if letters_wrong == tries:
            print "Fin du jeu"
            print "Le mot était ", word
            computer_score += 1
            break
        if "".join(clue) == word:
            print "Gagné !!!"
            print "Le mot était ", word
            player_score += 1
    return play_again()


def guess_letter():
    print
    letter = raw_input("Trouvez le mot mystère\n")
    letter.strip()
    letter.lower()
    print
    return letter


def play_again():
    answer = raw_input("Souhaitez vous rejouer ? O/n")
    if answer in ("o", "O", "y", "Y", "Bien sûr"):
        return answer
    else:
        print "Merci d'avoir joué, A bientôt !"


def scores():
    global player_score, computer_score
    print "MEILLEURS SCORES"
    print "Joueur : ", player_score
    print "Ordinateur : ", computer_score


if __name__ == '__main__':
    print "Jouons au jeu du Pendu"
    while game():
        pass
    scores()
