import csv
import os
import csv
import tkinter as tk
from datetime import datetime
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

#converting Bytes to MB
def byteConvert(fileSize):
   mb_bytes = fileSize / (1024 * 1024)
   return mb_bytes

#converting time to human readable time
def filetime(filetime):
   mtime_date = datetime.fromtimestamp(filetime)
   return mtime_date

#counting csv rows
def c_rows(f_path):
   with open(f_path,'r', newline='') as file:
       reader = csv.reader(file)
       header = next(reader, None)
       row_count = sum(1 for row in reader)
   return row_count

#counting csv columns
def c_columns(f_path):
   with open(f_path, 'r', newline='') as file:
       reader = csv.reader(file)
       header = next(reader, None)
       if header is not None:
           return len(header)
       else:
           return 0

#Getting the total 
def count_t_cells(countr,countc):
   num_r = countr
   num_c = countc

   total_c = (num_r + 1)* num_c
   return total_c

#printing an overview
def print_view(f_p):
	with open(f_p, 'r' , newline='') as file:
		csv_reader = csv.reader(file)
		for row in csv_reader:
			print(row)

#This method is for displaying the data
def displayData(file_path):
   file_mod = filetime(os.path.getmtime(file_path))
   file_size = os.path.getsize(file_path)
   file_rowz = c_rows(file_path)
   file_columnz = c_columns(file_path)
   total_cellz = count_t_cells(file_rowz,file_columnz)
   conv_size = byteConvert(file_size)

   print("File Location: " + file_path)
   print("The file is this big: " + str(conv_size))
   print("The last time this was modified was:" + str(file_mod))
   print("This file contains this many rows: " + str(file_rowz))
   print("This file contains this many columns: " + str(file_columnz))
   print("This File contains this many cells: " + str(total_cellz))
   print("Do you want an overview of the file?")
   print_view(file_path)

if file_path:
   displayData(file_path)
else:
   print("No File Selected. ")
