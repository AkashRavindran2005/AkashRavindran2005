#pip install pywhatkit
import pywhatkit
from tkinter import filedialog
import webbrowser

def ascii_art():
    file_path=filedialog.askopenfilename()
    pywhatkit.image_to_ascii_art(file_path,r'ascii_art.txt')
    webbrowser.open_new_tab('ascii_art.txt.txt')
