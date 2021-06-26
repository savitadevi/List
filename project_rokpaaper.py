from tkinter import *
import tkinter as tk
import tkinter
import random
window=tkinter.Tk()
window.geometry("1200x800")
window.configure(bg='Mediumseagreen',highlightbackground="Black",highlightthickness = 15)
# button_border=(window,highlightbackground="black",highlightthickness = 2, bd=0)
window.title("Rock_paper_scissors_game")
button1=tk.Button(text="Rock Paper Scissors Game",width=75,font=("Arial Bold",20),bd=8)
button2=tk.Button(text="USER v/s COMPUTER",width=75,font=("Arial Bold",20),bd=8)

button1.config(bg='light green')
button2.config(bg='light blue')
button1.pack()
button2.pack()

computer_value =["Rock","Paper","Scissors"]
def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l3.config(text = "")
    l4.config(text = "")
 
def rock():
    c_v = computer_value[(random.randint(0,2))]
    if c_v == "Rock":
        winner= "Match Draw"
    elif c_v=="Scissor":
        winner= "User Win"
    else:
        winner= "Computer Win"
    l3.config(text = c_v)
    l4.config(text =winner)
    
    
def paper():
    c_v = computer_value[(random.randint(0, 2))]
    if c_v == "Paper":
        winner= "Match Draw"
    elif c_v=="Scissor":
        winner= "Computer Win"
    else:
        winner= "User Win"
    l3.config(text = c_v)
    l4.config(text =winner)
    
    
def scissor():
    c_v = computer_value[(random.randint(0,2))]
    if c_v == "Rock":
        winner= "Computer Win"
    elif c_v == "Scissor":
        winner= "Match Draw"
    else:
        winner= "User Win"
    l3.config(text =c_v)
    l4.config(text =winner)
frame1 = Frame(window)
frame1.pack()
b1=Button(frame1,text="Rock",width=15,font=("Arial Bold",20),bd=12,command = rock)
b1.config(bg='red')

b2=Button(frame1,text="Paper",width=15,font=("Arial Bold",20),bd=12,command = paper)
b2.config(bg='green')

b3=Button(frame1,text="Scissors",width=15,font=("Arial Bold",20),bd=12,command = scissor)
b3.config(bg='blue')

b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack()


l2= Button(window,text = "Computer choice showing in white Box",font = "normal 0 bold",bg = "pink",width = 75 ,borderwidth = 2,relief = "solid",bd=4)
l2.pack(pady = 20)

l3 = Label(window,text = "",font = "normal 20 bold",bg = "white",width = 15 ,borderwidth = 2,relief = "solid")
l3.pack(pady = 20)

l4 = Button(window,text = "",font = "normal 20 bold",bg = "yellow",width = 15 ,borderwidth = 5,bd=8,relief = "solid")
l4.pack(pady = 20)

Button(text="Restart",width=15,bg="DodgerBlue",font=("Arial Bold",20),bd=12,command = reset_game).pack(side='bottom')
window.mainloop()