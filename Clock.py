from tkinter import Tk
from tkinter import Label
from tkinter import Button
import time

print("Joon")

#main screen
main_screen=Tk()
main_screen.title("Count down ")
#labels
Time_show=Label(text="",fg="red",font=("ariel",25))
Time_show.pack(padx=10)    

def clock():
    hour=time.strftime("%H")
    minute=time.strftime("%M")
    second=time.strftime("%S")
    Time_show.config(text=hour+":"+ minute+":"+second )
    Time_show.after(1000,clock)
#button
Start_button=Button(text="start",command=clock)
Start_button.pack(pady=10,padx=120)

main_screen.mainloop()