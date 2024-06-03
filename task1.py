import tkinter as tk
import playsound as p

def playsound(event):
    print(event)
    p.playsound("audio/animals_dogs_x2_barking_small_001.mp3")
    
def playsound(event):
    print(event)
    p.playsound("audio/All Trampoline Bounce Sounds- Sound Effect (Free).mp3")

def playsound(event):
    print(event)
    p.playsound("audio/animals_dogs_x2_barking_small_001.mp3")

def playsound(event):
    print(event)
    p.playsound("audio/animals_dogs_x2_barking_small_001.mp3")

def playsound(event):
    print(event)
    p.playsound("audio/animals_dogs_x2_barking_small_001.mp3")

win = tk.Tk()

b1 = tk.Button(win,text="Click to play")
b2 = tk.Button(win,text="Click to play")
b3 = tk.Button(win,text="Click to play")
b4 = tk.Button(win,text="Click to play")
b5 = tk.Button(win,text="Click to play")

b1.bind("<Button>",b1)
b2.bind("<Button>",playsound)
b3.bind("<Button>",playsound)
b4.bind("<Button>",playsound)
b5.bind("<Button>",playsound)

b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()

win.mainloop()