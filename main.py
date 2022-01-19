from wand.image import Image
import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from showinfm import show_in_file_manager

root = tk.Tk()
root.withdraw()

weaponType = simpledialog.askstring(title="Weapon Type", prompt="What weapon is this skin for?")
colName = filedialog.askopenfilename(title="Color image file", filetypes=(("PNG files", "*.png"), ("All files", "*.*")), initialdir=".")
ilmName = filedialog.askopenfilename(title="Illumination image file", filetypes=(("PNG files", "*.png"), ("All files", "*.*")), initialdir=".")
outputName = simpledialog.askstring(title="Output name", prompt="What do you want to call the output skin?")

colImage = Image(filename=colName)
ilmImage = Image(filename=ilmName)

colDDS = colImage.convert("dds")
colDDS.compression = "dxt1"
ilmDDS = ilmImage.convert("dds")
ilmDDS.compression = "dxt1"

os.makedirs(outputName)

resolutions = [2048, 1024, 512]

for res in resolutions:
    os.makedirs(f"{outputName}/{res}")
    colDDSClone = colDDS.clone()
    colDDSClone.resolution = (res, res)
    colDDSClone.save(filename=f"{outputName}/{res}/{weaponType}_Default_col.dds")

    ilmDDSClone = ilmDDS.clone()
    ilmDDSClone.resolution = (res, res)
    ilmDDSClone.save(filename=f"{outputName}/{res}/{weaponType}_Default_ilm.dds")

shutil.make_archive(outputName, 'zip', '.', f'{outputName}')
shutil.rmtree(outputName)

show_in_file_manager(".")