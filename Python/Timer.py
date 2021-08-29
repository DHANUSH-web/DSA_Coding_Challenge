from tkinter import *
from tkinter import messagebox
from time import sleep
import pygame  # to play music / beep sound

window = Tk()
window.title("PyTimer")
window['bg'] = "white"
window.geometry("400x300")
window.resizable(0, 0)

# initialize pygame
pygame.init()
pygame.mixer.music.load("assets/beeps.wav")


def closeApp():
    window.destroy()
    quit()


def timer():
    try:
        x = minutes.get().split(" " or ",")
        m = int(x[0]) - 1

        if len(x) > 1:
            m += 1
            s = int(x[1])

        while m >= 0:
            s = 59
            while s >= 0:
                sleep(1)
                # time formatting
                if m < 10:
                    m1 = f"0{m}"
                else:
                    m1 = str(m)

                if s < 10:
                    s1 = f"0{s}"
                else:
                    s1 = str(s)

                count["text"] = f"{m1} : {s1}"
                s -= 1
                count.update()

            m -= 1
            count.update()

        count["text"] = "Finish"
        pygame.mixer.music.play()
        stop["state"] = NORMAL

    except ValueError as e:
        messagebox.showerror("Value Error", f"Enter Positive integers only\n\nError: {e}")


def stopTone():
    pygame.mixer.music.stop()


count = Label(window, text="00 : 00", font=("Arial", 70, "bold"), relief="flat")

# modify the values
cnt = IntVar()
minutes = Entry(window, textvariable=cnt, font=("arial", 20, "bold"), relief="solid", bd=0, bg="white",
                highlightbackground="#0080ff", highlightcolor="#0080ff", highlightthickness=2)

# frame to add buttons
frame = Frame(window, bg="white", relief="flat")

# button to start
start = Button(frame, text="Start", font=("Monospace", 14, "bold"), cursor="hand2",
               bg="#1dd1a1", fg="white", relief="flat", command=timer)

# button to stop tone ringing
stop = Button(frame, text="Stop", font=("Monospace", 14, "bold"), cursor="hand2",
              bg="#192a56", fg="white", relief="flat", command=stopTone)

# button to close the window
close = Button(frame, text="Close", font=("Monospace", 14, "bold"), cursor="hand2", fg="white",
               bg="#ff6b6b", relief="flat", command=closeApp)

# packing the window
count.pack(side="top", padx=20, pady=20, fill="both")
minutes.pack(side="top", padx=20, pady=12, fill="x")
frame.pack(side="bottom", padx=15, pady=20, fill="both", expand=True)
start.pack(side="left", padx=5, fill="both", expand=True)
stop.pack(side="left", padx=5, fill="both", expand=True)
close.pack(side="right", padx=5, fill="both", expand=True)
window.mainloop()
