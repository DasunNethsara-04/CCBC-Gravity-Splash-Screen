from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import os


def open_dialog():
	path = filedialog.askopenfilename(filetypes=[('Executable Files', '*.exe')], defaultextension=('.exe'), title='Choose a application to run')
	print(path)
	a = open('path.txt', 'w')
	a.write(path)
	a.close()
	choice = messagebox.askyesno("Restart", "\'GRAVITY '22 App Launcher\' needs a restart! Would you like to restart it now?")
	if choice:
		root.destroy()

root = Tk()

# images
a = ImageTk.PhotoImage(Image.open('1.png').resize((10, 10)))
b = ImageTk.PhotoImage(Image.open('2.png').resize((10, 10)))
img = Image.open('Welcome250px.png').resize((100, 100))
img = ImageTk.PhotoImage(img)

width_of_window = 427
height_of_window = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = (screen_width / 2) - (width_of_window / 2)
y_cordinate = (screen_height / 2) - (height_of_window / 2)
root.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_cordinate, y_cordinate))
root.config(bg='#272727')
root.overrideredirect(True)

Frame(root, width=427, height=250, bg='#272727').place(x=0, y=0)
Label(root, image=img, bd=0, bg='#272727').place(x=160, y=10)
Label(root, text="GRAVITY '22", font=('Game of squids', 29, 'bold'), fg='#ff0', bg='#272727').place(x=50, y=100)
Label(root, text="Powered by Dasun Nethsara", font=('Poppins', 12), fg='white', bg='#272727').place(x=95, y=150)
Label(root, text="Loading...", font=('Calibri', 11), fg='white', bg='#272727').place(x=10, y=215)

app_path = open('.\\path.txt', 'r')
if app_path.read() == '':
	open_dialog()
else:
	app_path = open('.\\path.txt', 'r')
	path = app_path.read()
	app_path.close()

# animation
for i in range(3):
    Label(root, image=a, bd=0, relief=SUNKEN).place(x=180, y=195)
    Label(root, image=b, bd=0, relief=SUNKEN).place(x=200, y=195)
    Label(root, image=b, bd=0, relief=SUNKEN).place(x=220, y=195)
    Label(root, image=b, bd=0, relief=SUNKEN).place(x=240, y=195)
    root.update_idletasks()
    time.sleep(0.5)

    Label(root, image=b, bd=0, relief=SUNKEN).place(x=180, y=195)
    Label(root, image=a, bd=0, relief=SUNKEN).place(x=200, y=195)
    Label(root, image=b, bd=0, relief=SUNKEN).place(x=220, y=195)
    Label(root, image=b, bd=0, relief=SUNKEN).place(x=240, y=195)
    root.update_idletasks()
    time.sleep(0.5)

    Label(root, image=b, bd=0, relief=SUNKEN).place(x=180, y=195)
    Label(root, image=b, bd=0, relief=SUNKEN).place(x=200, y=195)
    Label(root, image=a, bd=0, relief=SUNKEN).place(x=220, y=195)
    Label(root, image=b, bd=0, relief=SUNKEN).place(x=240, y=195)
    root.update_idletasks()
    time.sleep(0.5)

    Label(root, image=b, bd=0, relief=SUNKEN).place(x=180, y=195)
    Label(root, image=b, bd=0, relief=SUNKEN).place(x=200, y=195)
    Label(root, image=b, bd=0, relief=SUNKEN).place(x=220, y=195)
    Label(root, image=a, bd=0, relief=SUNKEN).place(x=240, y=195)
    root.update_idletasks()
    time.sleep(0.5)


root.destroy()

# starting the application took from txt file
'''try:
	os.startfile(path)
except:
	messagebox.showerror("Error", "Path has not provided!")
'''
root.mainloop()