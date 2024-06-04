import tkinter as tk
import playsound as p
from tkinter import *
from tkinter import ttk

def BOOM(event):
    print(event)
    p.playsound("audio/Vine_boom_dunk.mp3")
    
def bounce(event):
    print(event)
    p.playsound("audio/All_Trampoline_Bounce_Sounds-Sound_Effect_(Free).mp3")

def AmongUs(event):
    print(event)
    p.playsound("audio/Among_Us_Sound_Effect.mp3")

def minecraft(event):
    print(event)
    p.playsound("audio/Minecraft_Eating.mp3")

def suspense(event):
    print(event)
    p.playsound("audio/SUSPENSE_SOUND_EFFECTS.mp3")

win = tk.Tk()
win.title("Sound Board")

vineboomimg = PhotoImage(file = "vineboom.png",width=250, height=250)
bounceimg = PhotoImage(file = "bounce.png",width=250, height=250)
amongusimg = PhotoImage(file = "amongus.png",width=250, height=250)
minecraftimg = PhotoImage(file = "minecraft.png",width=250, height=250)
suspenseimg = PhotoImage(file = "suspense.png",width=250, height=250)
bounceimg = PhotoImage(file = "bounce.png",width=250, height=250)

b1 = tk.Button(win,text="Click to play", image=vineboomimg)
b2 = tk.Button(win,text="Click to play", image=bounceimg)
b3 = tk.Button(win,text="Click to play", image=amongusimg)
b4 = tk.Button(win,text="Click to play", image=minecraftimg)
b5 = tk.Button(win,text="Click to play", image=suspenseimg)

l1 = tk.Label(win, text="Vine Boom")
l2 = tk.Label(win, text="Bounce")
l3 = tk.Label(win, text="Among Us Effect")
l4 = tk.Label(win, text="Minecraft Eating")
l5 = tk.Label(win, text="Suspense")

b1.bind("<Button>",BOOM)
b2.bind("<Button>",bounce)
b3.bind("<Button>",AmongUs)
b4.bind("<Button>",minecraft)
b5.bind("<Button>",suspense)

l1.grid(row=2, column=1)
b1.grid(row=1, column=1)
l2.grid(row=2, column=2)
b2.grid(row=1, column=2)
l3.grid(row=2, column=3)
b3.grid(row=1, column=3)
l4.grid(row=4, column=1)
b4.grid(row=3, column=1)
l5.grid(row=4, column=2)
b5.grid(row=3, column=2)


win.mainloop()