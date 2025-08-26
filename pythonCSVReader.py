import csv
import os
import tkinter as tk
from tkinter import filedialog
#Python reading program

#Using this to locate the home directory & documents directory
home_dir = os.path.expanduser("~")
docum_dir = os.path.join(home_dir,"Documents")

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    #file dialog to open the home dir & document directory
    initialdir=docum_dir,
    title="select a file",
    filetypes=(("csv file","*.csv"),("All files","*.*"))
)

if file_path:
   print("you have selected file:"+ file_path)
else:
   print("No File Selected.")


# with open('data.csv', 'r') as file:
#     csv_read = csv.reader(file)
#     header = next(csv_read)
#     for row in csv_read:
#         print(row)
