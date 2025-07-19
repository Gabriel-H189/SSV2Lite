import tkinter as tk
import winsound
import random
import time
import datetime
import tkinter.ttk
import threading
import configparser


random.seed()

def _scare():
    global timer_entry, comb, xt, yt
    
    timer = int(timer_entry.get())
    sound = comb.get() + ".wav"
    min_time = int(xt.get())
    max_time = int(yt.get())

    seagulls = 0
    while timer > 0:
        winsound.PlaySound(sound, winsound.SND_ASYNC)
        pause = random.randint(min_time, max_time)
        timer -= pause
        seagulls += 1
        print("Approximately", seagulls, "seagull(s) were scared on", datetime.datetime.now())
        # if timer == 0:
            # break
        time.sleep(pause)

def scare():
    global timer_entry, comb, xt, yt

    threading.Thread(target=_scare).start()

# Read config file
parser = configparser.ConfigParser()
parser.read("ss_config.ini")

config = parser.sections()

cfg_timer = int(parser[config[0]]["scaring_time"])
cfg_min_time = int(parser[config[0]]["min_time"])
cfg_max_time = int(parser[config[0]]["max_time"])
cfg_sound = parser[config[0]]["default_sound"]

# define a root element
root = tk.Tk()
root.title("Seagull Scaring V2 Lite")
root.geometry("400x400")
root.attributes("-topmost", 1)
root.resizable(False, False)

icon = tk.PhotoImage("logo.png")
image = tk.Label(root, image=icon)
image.pack(pady=2)

label = tk.Label(root, text="Seagull Scaring", font=("calibri", 13))
label.pack()

tk.Label(root, text="Time to run for: ").pack()
timer_entry = tk.Entry(root)
timer_entry.pack(pady=3)
timer_entry.insert(0, str(cfg_timer))

tk.Label(root, text="Minimum time to wait: ").pack()
xt = tk.Entry(root)
xt.pack(pady=3)
xt.insert(0, str(cfg_min_time))

tk.Label(root, text="Maximum time to wait: ").pack()
yt = tk.Entry(root)
yt.pack(pady=3)
yt.insert(0, str(cfg_max_time))

sounds = ["seagull", "angry seagull", "confused seagull", "disgust seagull", "alarm seagull", "robot seagull", "Seagull 2", "sea gull"]
comb = tkinter.ttk.Combobox(root, values=sounds)
comb.pack(pady=5)
comb.set(cfg_sound)

btn = tk.Button(root, text="scare the gulls", command=scare)
btn.pack()

if __name__ == "__main__":
    root.mainloop()
