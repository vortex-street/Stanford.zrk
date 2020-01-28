import tkinter as tk
import time
import cv2
from pygame import mixer
from pydub import AudioSegment

prompt = 'The terrible troll raises his sword'
password = 'Attack troll with nasty knife'
password2 = 'Attack troll with nasty knife.'
password3 = 'attack troll with nasty knife'
video = r'/Users/nickthomas/PycharmProjects/Intersect/Stanford.zrk.mp4'
audio = r'/Users/nickthomas/PycharmProjects/Intersect/Stanford.zrk.mp3'
song = AudioSegment.from_mp3(audio)


class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        pad = 3
        self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.bind('<Escape>', self.toggle_geom)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom


def print_string(string):
    for char in string:
        prompt_label.configure(text=prompt_label.cget('text') + char)
        prompt_label.update()
        time.sleep(.077)


def intersect(event):
    code = entry.get()
    if code == password or code == password2 or code == password3:
        time.sleep(2)
        play_av()
        self_destruct()
        exit_program()
    else:
        error['text'] = 'Incorrect ID. System will self-destruct in 5 seconds.'
        error.update()
        exit_program()


def play_av():
    mixer.init()
    mixer.music.load(audio)
    mixer.music.play()
    file_name = video
    window_name = "window"
    wait_ms = 27

    cap = cv2.VideoCapture(file_name)
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Reached end of video, exiting.")
            break

        cv2.imshow(window_name, frame)
        if cv2.waitKey(wait_ms) & 0x7F == ord('q'):
            print("Exit requested.")
            break

    cap.release()
    cv2.destroyAllWindows()


def self_destruct():
    for t in range(3, 0, -1):
        time.sleep(1)
        error['text'] = 'Self destruct in: ' + str(t)
        error.update()


def exit_program():
    time.sleep(5)
    root.destroy()


root = tk.Tk()
app = FullScreenApp(root)

frame = tk.Frame(root, bg='black')
frame.place(relwidth=1, relheight=1)

prompt_label = tk.Label(frame, bg='black', fg='white', text='', font=('arial', 100, 'bold'), anchor='s')
prompt_label.place(relx=0.2, rely=0.4)


entry = tk.Entry(frame, font=('arial', 100, 'bold'), bg='black', fg='white', cursor='ibeam', selectborderwidth=0)
entry.place(relx=0.2, rely=0.5, relwidth=0.6)
entry.bind('<Return>', intersect)

error = tk.Label(frame, bg='black', fg='white', text='', font=('arial', 100, 'bold'), anchor='s')
error.place(rely=0.8, relheight=0.2)

print_string(prompt)

root.mainloop()
