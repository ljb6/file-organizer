from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from manager import organize

disorganized_directory = ""
destiny_directory = ""

def select_arc1():
  global disorganized_directory
  selected_file = filedialog.askdirectory()
  dir1.set(selected_file)
  disorganized_directory = selected_file

def select_arc2():
  global destiny_directory
  selected_file = filedialog.askdirectory()
  dir2.set(selected_file)
  destiny_directory = selected_file

window = Tk()
window.title('File Manager')
window.geometry("500x300")

frm = ttk.Frame(window, padding=40)
frm.pack(expand=True, fill="both")

label1 = ttk.Label(frm, text="Select origin directory:")
label1.pack()

dir1 = StringVar()
rdir1 = ttk.Label(frm, textvariable=dir1)
rdir1.pack()

button1 = ttk.Button(frm, text="Select", command=select_arc1)
button1.pack()

# Widgets do segundo grupo
label2 = ttk.Label(frm, text="")
label3 = ttk.Label(frm, text="Select destination directory:")
label2.pack()
label3.pack()

dir2 = StringVar()
rdir2 = ttk.Label(frm, textvariable=dir2)
rdir2.pack()

button2 = ttk.Button(frm, text="Select", command=select_arc2)
button2.pack()

def start_managment():  
  organize(disorganized_directory, destiny_directory + '/')
  print('Done')
  window.destroy()

button3 = ttk.Label(frm, text="")
button4 = ttk.Button(frm, text="Start", command=start_managment)
button3.pack()
button4.pack()

window.mainloop()
