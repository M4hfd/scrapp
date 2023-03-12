from tkinter import *
import pyautogui
from tkinter import filedialog



def screenshot():
    save_path = filedialog.asksaveasfilename(defaultextension="screenshot.png")
    if save_path:
        screenshot = pyautogui.screenshot()
        screenshot.save(save_path)


def close():
    window.destroy()


window = Tk()
window.title('ScrApp')
window.geometry('200x150')

frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)

screen_button = Button(
    frame,
    text='Сделать скриншот',
    command=screenshot
)
screen_button.grid(row=5, column=2)

close_b = Button(
    frame,
    text='Выйти',
    command=close
)
close_b.grid(row=6, column=2)

window.mainloop()
