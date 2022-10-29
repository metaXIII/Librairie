#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import random
from Tkinter import *
from ttk import *


def gui():
    rock = 1
    paper = 2
    scissor = 3

    names = {rock: "Rock", paper: "Paper", scissor: "Scissor"}
    rules = {rock: scissor, paper: rock, scissor: paper}

    player_score = 0
    computer_score = 0

    def start():
        while game():
            pass

    def game():
        player = player_choice.get()
        computer = random.randint(1, 3)
        computer_choice.set(names[computer])
        result(player, computer)

    def result(player, computer):
        if player == computer:
            result_set.set("Match Nul ! ")
        else:
            if rules[player] == computer:
                result_set.set("Vous avez gagné ! ")
                new_score = player_score.get()
                new_score += 1
                player_score.set(new_score)
            else:
                result_set.set("L'ordinateur rit car vous avez perdu ! ")
                new_score = computer_score.get()
                new_score += 1
                computer_score.set(new_score)

    rps_windows = Toplevel()
    rps_windows.title("Pierre caillou ciseaux")

    player_choice = IntVar()
    computer_choice = StringVar()
    result_set = StringVar()
    player_choice.set(1)
    player_score = IntVar()
    computer_score = IntVar()

    rps_frame = Frame(rps_windows, padding='3 3 12 12', width=300)
    rps_frame.grid(column=0, row=0, sticky=(N, W, E, S))
    rps_frame.columnconfigure(0, weight=1)
    rps_frame.rowconfigure(0, weight=1)

    Label(rps_frame, text="Joueur").grid(column=1, row=1, sticky=W)

    Radiobutton(rps_frame, text="Caillou", variable=player_choice, value=1).grid(column=1, row=2, sticky=W)
    Radiobutton(rps_frame, text="Papier", variable=player_choice, value=2).grid(column=1, row=3, sticky=W)
    Radiobutton(rps_frame, text="Ciseaux", variable=player_choice, value=3).grid(column=1, row=4, sticky=W)

    Label(rps_frame, text="Ordinateur").grid(column=3, row=1, sticky=W)
    Label(rps_frame, textvariable=computer_choice).grid(column=3, row=3, sticky=W)

    Button(rps_frame, text="Tour", command=start).grid(column=2, row=2)

    Label(rps_frame, text="Score").grid(column=1, row=5, sticky=W)
    Label(rps_frame, textvariable=player_score).grid(column=1, row=6, sticky=W)

    Label(rps_frame, text="Score").grid(column=3, row=5, sticky=W)
    Label(rps_frame, textvariable=computer_score).grid(column=3, row=6, sticky=W)

    Label(rps_frame, textvariable=result_set).grid(column=2, row=7)


if __name__ == '__main__':
    gui()
