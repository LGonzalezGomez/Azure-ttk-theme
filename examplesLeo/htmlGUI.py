# %%
from tkinterhtml import HtmlFrame

import tkinter as tk
from pathlib import Path

html_path = Path("C:/Users/leogonzalez.VILARRIBA/OneDrive - VILAR RIBA/Rutes_FFerrer/output")

url=html_path / "Microlineplot_ruta_2022-08-17.html"
root = tk.Tk()

frame = HtmlFrame(root, horizontal_scrollbar="auto")
 
frame.set_content(url)
frame.pack()
root.mainloop()

# %% TODO: No funciona al cargar un html perse
from tkinterweb import HtmlFrame #import the HtmlFrame widget
try:
  import tkinter as tk #python3
except ImportError:
  import Tkinter as tk #python2

from pathlib import Path


html_path = Path('examplesLeo')
url=html_path / 'Microlineplot_ruta_2022-08-17.html'

root = tk.Tk() #create the Tkinter window

### The important part: create the html widget and attach it to the window
myhtmlframe = HtmlFrame(root) #create HTML browser
# myhtmlframe.load_html('examplesLeo/Microlineplot_ruta_2022-08-17.html')
myhtmlframe.load_website('https://github.com/Andereoo/TkinterWeb/blob/main/tkinterweb/docs')

myhtmlframe.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window

root.mainloop()
# %%
