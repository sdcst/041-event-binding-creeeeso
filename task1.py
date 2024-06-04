import tkinter as tk
import playsound as p

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

b1 = tk.Button(win,text="Click to play")
b2 = tk.Button(win,text="Click to play")
b3 = tk.Button(win,text="Click to play")
b4 = tk.Button(win,text="Click to play")
b5 = tk.Button(win,text="Click to play")

l1 = tk.Label(win, text="Sound Board")
l2 = tk.Label(win, text="Bounce")
l3 = tk.Label(win, text="Among Us Effect")
l4 = tk.Label(win, text="Minecraft Eating")
l5 = tk.Label(win, text="Suspense")
l6 = tk.Label(win, text="Sound Board")

b1.bind("<Button>",BOOM)
b2.bind("<Button>",bounce)
b3.bind("<Button>",AmongUs)
b4.bind("<Button>",minecraft)
b5.bind("<Button>",suspense)

l1.grid(row=1, column=1)
b1.grid(row=1, column=2)
l2.grid(row=2, column=1)
b2.grid(row=2, column=2)
l3.grid(row=3, column=1)
b3.grid(row=3, column=2)
l4.grid(row=4, column=1)
b4.grid(row=4, column=2)
l5.grid(row=5, column=1)
b5.grid(row=5, column=2)

win.mainloop()