from tkinter import *
from PIL import Image,ImageTk
from random import randint

window = Tk()
window.title("STONE PAPER SCISSOR GAME")
window.configure(background="#f0b3ff")

stone_img = ImageTk.PhotoImage(Image.open("stone.png"))
stone_img_comp = ImageTk.PhotoImage(Image.open("stone_comp.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper_comp.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissor.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissor_comp.png"))

user_label = Label(window,image=paper_img,bg="#f0b3ff")
comp_label = Label(window,image=paper_img_comp,bg="#f0b3ff")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

playerscore = Label(window,text=0,font=100,bg="#f0b3ff",fg="black")
compscore = Label(window,text=0,font=100,bg="#f0b3ff",fg="black")
compscore.grid(row=1,column=1)
playerscore.grid(row=1,column=3)

user_indicator = Label(window,font=50,text="USER",bg="#f0b3ff",fg="black")
comp_indicator = Label(window,font=50,text="COMPUTER",bg="#f0b3ff",fg="black")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

msg = Label(window, font=100, bg="#f0b3ff",fg="black")
msg.grid(row=3,column=2)

def updateMessage(x):
    msg['text'] = x


def updateuserscore():
    score = int(playerscore["text"])
    score += 1
    playerscore["text"] = str(score)

def updatecompscore():
    score = int(compscore["text"])
    score += 1
    compscore["text"] = str(score)

def checkwinner(player,computer):
    if player == computer:
        updateMessage("It's a tie!!")
    elif player == "stone":
        if computer == "paper":
            updateMessage("You Loose")
            updatecompscore()
        else:
            updateMessage("You Win")
            updateuserscore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You Loose")
            updatecompscore()
        else:
            updateMessage("You Win")
            updateuserscore()
    elif player == "scissor":
        if computer == "stone":
            updateMessage("You Loose")
            updatecompscore()
        else:
            updateMessage("You Win")
            updateuserscore()
    else:
        pass

    

choices = ["stone","paper","scissor"]
def updateChoice(x):

    compchoice = choices[randint(0,2)]
    if compchoice == "stone":
        comp_label.configure(image=stone_img_comp)
    elif compchoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)


    if x=="stone":
        user_label.configure(image=stone_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    checkwinner(x,compchoice)

stone = Button(window,width=20,height=2,text="STONE",bg="#FF3E4D",fg="white",command = lambda:updateChoice("stone")).grid(row=2,column=1)
paper = Button(window,width=20,height=2,text="PAPER",bg="#FAD02E",fg="white",command = lambda:updateChoice("paper")).grid(row=2,column=2)
scissor = Button(window,width=20,height=2,text="SCISSOR",bg="#03cffc",fg="white",command = lambda:updateChoice("scissor")).grid(row=2,column=3)
window.mainloop()