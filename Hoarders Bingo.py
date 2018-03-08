from tkinter import *
from random import randint
from functools import partial

hoarder_traits=["Isolated", "In denial", "Shipping boxes", "Obesity", "Enabling spouse",
                "Passive family", "Feces", "Disfuntional kitchen", "Cats", "Sleeps in trash cocoon",
                "\"I'm not a hoarder\"", "Illness caused by hoard", "Old or decrepit electronics",
                "Filthy refrigerator", "Paper overload", "Pests", "Scrap vehicles or metal",
                "Embarrased others may see hoard", "\"I'm a collector\"", "House has structural damage",
                "Deer paths", "Can't resist bargains", "Dumpster diving", "House smells foul",
                "Items = memories", "Trash over family", "Childish behavior", "\"I can sell it\"",
                "Creepy dolls", "Authority intervention threat", "Expired food", "Disfunctional toilet",
                "Lives or sleeps off-site", "\"It's still safe to eat\""]

hoarder_bingo = Tk()
hoarder_bingo.title("Hoarder Bingo Game")
hoarder_bingo.geometry("480x480")

main_frame = Frame(hoarder_bingo)
main_frame.grid(row=5, column=5)

score_check = []

def clicked_box(row, col):
    if str(row)+str(col) not in score_check:
        score_check.extend([(str(row) + str(col))])
        tile[row, col].config(bg="green", relief=SUNKEN)
        tracker()

def select_trait(data):
    if data != []:
        index = randint(0,len(hoarder_traits)-1)
        elem = data[index]
        data[index] = data[-1]
        del data[-1]
        return elem
    else:
        return elem

def enter_name(*ignore):
    hoarder_name.config(state=DISABLED)

def bingo():
    name = hoarder_name.get() + " is a BINGO certified hoarder!"
    completed = Label(hoarder_bingo, text=name, fg="white", bg="blue")
    completed.grid(row=5, column=0, columnspan=5, sticky=N+S+E+W)

def tracker():
    #Vertical
    if (('00' in score_check) and ('01' in score_check) and ('02' in score_check) and ('03' in score_check) and ('04' in score_check)):
        bingo()
    elif (('10' in score_check) and ('11' in score_check) and ('12' in score_check) and ('13' in score_check) and ('14' in score_check)):
        bingo()
    elif (('20' in score_check) and ('21' in score_check) and ('22' in score_check) and ('23' in score_check) and ('24' in score_check)):
        bingo()
    elif (('30' in score_check) and ('31' in score_check) and ('32' in score_check) and ('33' in score_check) and ('34' in score_check)):
        bingo()
    elif (('40' in score_check) and ('41' in score_check) and ('42' in score_check) and ('43' in score_check) and ('44' in score_check)):
        bingo()
    #Horizontal
    elif (('00' in score_check) and ('10' in score_check) and ('20' in score_check) and ('30' in score_check) and ('40' in score_check)):
        bingo()
    elif (('01' in score_check) and ('11' in score_check) and ('21' in score_check) and ('31' in score_check) and ('41' in score_check)):
        bingo()
    elif (('02' in score_check) and ('12' in score_check) and ('22' in score_check) and ('32' in score_check) and ('42' in score_check)):
        bingo()
    elif (('03' in score_check) and ('13' in score_check) and ('23' in score_check) and ('33' in score_check) and ('43' in score_check)):
        bingo()
    elif (('04' in score_check) and ('14' in score_check) and ('24' in score_check) and ('34' in score_check) and ('44' in score_check)):
        bingo()
    #Diagonal
    elif (('00' in score_check) and ('11' in score_check) and ('22' in score_check) and ('33' in score_check) and ('44' in score_check)):
        bingo()
    elif (('40' in score_check) and ('31' in score_check) and ('22' in score_check) and ('13' in score_check) and ('04' in score_check)):
        bingo()

tile = {}
for x in range(5):
    for y in range(5):
        if x == 2 and y == 2:
            tile[x,y] = Button(hoarder_bingo, text="Is a hoarder (Free space)", wraplength=80, command=partial(clicked_box, x, y))
        else:
            tile[x,y] = Button(hoarder_bingo, text=select_trait(hoarder_traits), wraplength=80, command=partial(clicked_box, x, y))
        tile[x,y].grid(column=x, row=y, sticky=N+S+E+W)

for x in range(5):
    Grid.columnconfigure(hoarder_bingo, x, weight=1)

for y in range(5):
    Grid.rowconfigure(hoarder_bingo, y, weight=1)

hoarder_name = Entry()
hoarder_name.grid(row=5, column=0, columnspan=5)
hoarder_name.bind("<Return>", enter_name)

hoarder_bingo.mainloop()
