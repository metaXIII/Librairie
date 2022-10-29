#!/usr/bin/env python2
# coding=utf-8

from Tkinter import *
from ttk import *
from random import *

word = 0
word_length = 0
clue = 0
tries = 5


def gui():
    global word, word_length, clue
    dictionary = ["gnu", "kernel", "linux", "pingouin", "ubuntu"]
    word = choice(dictionary)
    word_length = len(word)
    clue = word_length * ["_"]

    def hangedman(hangman):
        graphic = [
            """
            +----------+
            |
            |
            |
            |
            =================
            """,
            """
            +----------+
            |            |
            |            O
            |
            |
            =================
            """,
            """
            +----------+
            |            |
            |            O
            |           -|
            |
            =================
            """,
            """
            +----------+
            |            |
            |            O
            |           -|-
            |
            =================
            """,
            """
            +----------+
            |            |
            |            O
            |           -|-
            |           /
            =================
            """,
            """
            +----------+
            |            |
            |            O
            |           -|-
            |           / \\
            =================
            """
        ]
        graphic_set = graphic[hangman]
        hm_graphic.set(graphic_set)

    def game():
        global tries
        letters_wrong = incorrect_guesses.get()
        if letters_wrong == tries:
            reset_game()
            return
        letter = guess_letter()
        first_index = word.find(letter)
        if first_index == -1:
            letters_wrong += 1
            incorrect_guesses.set(letters_wrong)
        else:
            for i in range(word_length):
                if letter == word[i]:
                    clue[i] = letter
        hangedman(letters_wrong)
        clue_set = " ".join(clue)
        word_output.set(clue_set)
        if letters_wrong == tries:
            result_text = "Fin du jeu, le mot était " + word
            result_set.set(result_text)
            new_score = computer_score.get()
            new_score += 1
            computer_score.set(new_score)
        if "".join(clue) == word:
            result_text = "Gagné, le mot était " + word
            result_set.set(result_text)
            new_score = player_score.get()
            new_score += 1
            player_score.set(new_score)

    def guess_letter():
        letter = letter_guesses.get()
        letter.strip()
        letter.lower()
        return letter

    def reset_game():
        global word, word_length, clue, result_set, letter_guesses
        incorrect_guesses.set(0)
        hangedman(0)
        result_set = ""
        letter_guesses = ""
        word = choice(dictionary)
        word_length = len(word)
        clue = word_length * ["_"]
        new_clue = "".join(clue)
        word_output.set(new_clue)

    hm_windows = Toplevel()
    hm_windows.title("Pendu")
    incorrect_guesses = IntVar()
    incorrect_guesses.set(0)
    player_score = IntVar()
    player_score.set(0)
    computer_score = IntVar()
    computer_score.set(0)
    result_set = StringVar()
    word_output = StringVar()
    hm_graphic = StringVar()
    letter_guesses = StringVar()

    hm_frame = Frame(hm_windows, padding='3 3 12 12', width=300)
    hm_frame.grid(column=0, row=0, sticky=(N, W, E, S))
    hm_frame.columnconfigure(0, weight=1)
    hm_frame.rowconfigure(0, weight=1)

    Label(hm_frame, textvariable=hm_graphic).grid(column=2, row=1)
    Label(hm_frame, text='Mot').grid(column=2, row=2)
    Label(hm_frame, textvariable=word_output).grid(column=2, row=3)

    Label(hm_frame, text='Saisissez une lettre').grid(column=2, row=4)
    hm_entry = Entry(hm_frame, exportselection=0, textvariable=letter_guesses).grid(column=2, row=5)
    hm_entry_button = Button(hm_frame, text='Guess', command=game).grid(column=2, row=6)

    Label(hm_frame, text="Gains").grid(column=1, row=7, sticky=W)
    Label(hm_frame, textvariable=player_score).grid(column=1, row=8, sticky=W)
    Label(hm_frame, text="Pertes").grid(column=3, row=7, sticky=W)
    Label(hm_frame, textvariable=computer_score).grid(column=3, row=8, sticky=W)
    Label(hm_frame, textvariable=result_set).grid(column=2, row=9)
    replay_button = Button(hm_frame, text="Remise à zéro", command=reset_game).grid(column=2, row=10)


if __name__ == '__main__':
    gui()
