import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
import threading
import time
import os
from pyzkfp import ZKFP2

zkfp2 = ZKFP2()
zkfp2.Init()

device_count = zkfp2.GetDeviceCount()
if device_count == 0:
    print("No devices found")
    exit()
zkfp2.OpenDevice(0)

subject_number = 52
subject_try = 1
current_image_path = "assets/finger.png"
get_image_path = lambda: f"assets/fingerprints/finger_{subject_number}_{subject_try}.png"


def update_image():
    global subject_try, one_more_time_button

    text = f"Файл: {get_image_path()}\nИспытуемый: {subject_number}, Попытка: {subject_try}"
    if subject_try == 0:
        text = f"Файл: -\nИспытуемый: {subject_number}, Попытка: -"

    label_text.config(text=text)

    if os.path.exists(current_image_path):
        image = Image.open(current_image_path)
        image = image.resize((300, 375), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo

        if subject_try == 0:
            label.config(image=None)
            label.image = None
            one_more_time_button["state"] = tk.DISABLED
        else:
            one_more_time_button["state"] = tk.NORMAL

        subject_try += 1


def watch_for_changes():
    last_mtime = None
    while True:
        if os.path.exists(current_image_path):
            mtime = os.path.getmtime(current_image_path)
            if last_mtime is None:
                last_mtime = mtime
            elif mtime > last_mtime:
                last_mtime = mtime
                root.after(0, update_image)
        time.sleep(1)


def scan_fingerprint():
    while True:
        capture = zkfp2.AcquireFingerprint()
        if capture:
            tmp, img = capture
            image = Image.frombytes("L", (300, 375), img)

            image.save(current_image_path, "PNG")
            image.save(get_image_path(), "PNG")


def next_subject():
    global subject_number, subject_try

    subject_number += 1
    subject_try = 0

    update_image()


def one_more_time_subject():
    global subject_try

    subject_try -= 2
    update_image()


def start_scanner_thread():
    scanner_thread = threading.Thread(target=scan_fingerprint, daemon=True)
    scanner_thread.start()


def start_watcher_thread():
    watcher_thread = threading.Thread(target=watch_for_changes, daemon=True)
    watcher_thread.start()


root = tk.Tk()
root.title("Tkinter Fingerprint Viewer")
root.geometry("500x500")

label = Label(root)
label.pack(expand=True)

label_text = Label(root, text=f"Файл: -\nИспытуемый: {subject_number}, Попытка: -", font=("Arial", 12))
label_text.pack()

next_button = Button(root, text="Следующий испытуемый", font=("Arial", 14), command=next_subject)
next_button.pack()

one_more_time_button = Button(root, text="Повторить попытку", font=("Arial", 14), command=one_more_time_subject)
one_more_time_button["state"] = tk.DISABLED
one_more_time_button.pack()

start_scanner_thread()
start_watcher_thread()

root.mainloop()
