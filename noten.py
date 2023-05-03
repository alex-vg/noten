from tkinter import *

root = Tk()

v = StringVar()
v.set("")  # initializing the choice, i.e. Python

noten = [
    ("1", "sehr gut"),
    ("2", "gut"),
    ("3", "befriedigend"),
    ("4", "ausreichend"),
    ("5", "mangelhaft"),
    ("6", "ungenügend"),
    ("15 NP", "sehr gut + (NP)"),
    ("14 NP", "sehr gut (NP)"),
    ("13 NP", "sehr gut - (NP)"),
    ("12 NP", "gut + (NP)"),
    ("11 NP", "gut (NP)"),
    ("10 NP", "gut - (NP)"),
    (" 9 NP", "befriedigend + (NP)"),
    (" 8 NP", "befriedigend (NP)"),
    (" 7 NP", "befriedigend - (NP)"),
    (" 6 NP", "ausreichend + (NP)"),
    (" 5 NP", "ausreichend (NP)"),
    (" 4 NP", "ausreichend - (NP)"),
    (" 3 NP", "mangelhaft + (NP)"),
    (" 2 NP", "mangelhaft (NP)"),
    (" 1 NP", "mangelhaft - (NP)"),
    (" 0 NP", "ungenügend (NP)"),
]

def showChoice():
    print(v.get())


label = Label(root, textvariable=v)
label.pack()

Label(root,
      text="""Wähle deine Note:""",
      justify = LEFT,
      padx = 20).pack()

for txt, val in noten:
    Radiobutton(root,
                text=txt,
                padx = 20,
                variable=v,
                command=showChoice,
                value=val).pack(anchor=W)

mainloop()