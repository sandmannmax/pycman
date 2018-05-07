import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'C:\Users\sandm\AppData\Local\Programs\Python\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\sandm\AppData\Local\Programs\Python\Python36\tcl\tk8.6'

setup(name="Pycman",options={"build_exe":{"packages":["pygame","os"],"include_files":["pacman.png","background.png","icon.png","punkt.png"]}},executables = [Executable("main.py")])
