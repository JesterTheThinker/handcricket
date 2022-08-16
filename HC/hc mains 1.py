from tkinter import *
from random import randint
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title('Hand Cricket by Fireblaster and Jester')
root.geometry("600x500")
root.config(bg='white')


no_ls = ["1", "2", "3", "4", "5", "6"]

pick_no = randint(0, 5)


img_lbl = Label(root, text=no_ls[pick_no])
img_lbl.pack(pady=20)

def play():
    pick_no = randint(0, 5)
    
    img_lbl.config(text=no_ls[pick_no])
    
    if user_choice.get() == "1":
        user_choice_value = 0
    elif user_choice.get() == "2":
        user_choice_value = 1
    elif user_choice.get() == "3":
        user_choice_value = 2
    elif user_choice.get() == "4":
        user_choice_value = 3
    elif user_choice.get() == "5":
        user_choice_value = 4
    elif user_choice.get() == "6":
        user_choice_value = 5
        
    #if user picks 1
    if user_choice_value == 0:
        if pick_number == 0:
            win_lose_label.config(text="You're OUT!!")
        else:
            win_lose_label.config(text="you scored 1 run")

 
user_choice= ttk.Combobox(root, value=("1", "2", "3", "4", "5", "6"))
user_choice.current(0)
user_choice.pack(pady=20)

play_b = Button(root, text="PLAY")
play_b.pack(pady=10)

root.mainloop()