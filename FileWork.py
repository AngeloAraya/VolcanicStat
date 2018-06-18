from tkinter import filedialog
from tkinter import Tk
import TarWork
 
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Seleccione Archivo",filetypes = (("tar.gz files","*.tar.gz"),("all files","*.*")))

folder = "ImageProc/data/"+root.filename[-47:].strip()[:-7]

TarWork.extract_file(root.filename,folder)


