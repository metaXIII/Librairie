#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from Tkinter import *

import RockPaperScissor
import hangmantutorial
import pokerdice

root = Tk()
root.title("Mega collection de micro-jeux")

mainframe = Frame(root, height=200, width=500)
mainframe.pack_propagate(0)
mainframe.pack(padx=5, pady=5)

intro = Label(mainframe, text=""" Bienvenue dans la collection de micro jeux, Sélectionnez l'un des jeux suivants :""")
intro.pack(side=TOP)

# rps_button = Button(mainframe, text="Caillou, Papier, Ciseaux ", command=RockPaperScissor.gui)
# rps_button.pack()

# hm_button = Button(mainframe, text="Pendu", command=hangmantutorial.start)
# hm_button.pack()

# pd_button = Button(mainframe, text="Pokerdice", command=pokerdice.start())
# pd_button.pack()

exit_button = Button(mainframe, text="Quitter", command=root.destroy)
exit_button.pack(side=BOTTOM)

root.mainloop()
