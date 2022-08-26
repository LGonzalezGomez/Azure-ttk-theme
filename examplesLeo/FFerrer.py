# Importing Tkinter and Ttk
# %%
import tkinter as tk
from tkinter import ttk
from datetime import datetime, date
from pathlib import Path
import json


#Create options to select routes
with open(Path("examplesLeo")/ "config_rutes.json", "r") as jsonfile: #Here we have the config file with the predefined routes
    rutes_predeterminades = json.load(jsonfile)

readonlycombo_list = ['Selecciona ruta']

for k in rutes_predeterminades.keys():
    readonlycombo_list.append(k)
readonlycombo_list.append("Nova ruta")
# Create the window
root = tk.Tk()
root.title('Rutes Vilar i Riba')

# Place the window in the center of the screen
windowWidth = 550
windowHeight = 530
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
xCordinate = int((screenWidth/2) - (windowWidth/2))
yCordinate = int((screenHeight/2) - (windowHeight/2))
root.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, xCordinate, yCordinate))

# Create a style
style = ttk.Style(root)
style.configure("Button", background="red")
style.map('Button', background=[('active','red')])
# Import the tcl file
root.tk.call('source', 'azure dark/azure dark.tcl')

# Set the theme with the theme_use method
style.theme_use('azure')

# Creating lists
option_list = ['', 'OptionMenu', 'Value 1', 'Value 2']


# Create control variables
data = tk.StringVar(value = date.today().strftime("%d/%m/%Y"))
num_vehicles = tk.IntVar() #TODO: Change value when selecting route!
all_vehicles = tk.IntVar(value = 1)
pen_longroute = tk.IntVar(value = 1)
a = tk.IntVar()
b = tk.IntVar(value=1)
c = tk.IntVar()
d = tk.IntVar(value=2)
e = tk.StringVar(value=option_list[1])
f = tk.IntVar()
g = tk.IntVar(value=75)
h = tk.IntVar()





# Separator
# separator = ttk.Separator()
# separator.place(x=20, y=235, width=210)




# Entry
entry_data = ttk.Entry(root, textvariable = data, width = 22)
# entry_data.place(x=20, y=20)
entry_data.grid(row = 0, column= 0)
# entry_data.insert(0)


# # Combobox
# combobox = ttk.Combobox(root, value=combo_list)
# combobox.current(0)
# combobox.place(x=20, y=70)

# Read-only combobox
readonlycombo = ttk.Combobox(root, state='readonly', value=readonlycombo_list)
readonlycombo.current(0)
# readonlycombo.place(x=20, y=70)
readonlycombo.grid(row = 1, column= 0)

label_vehicles = tk.Label(root, text = "# Vehicles ")
# label_vehicles.place(x= 20, y = 125)
label_vehicles.grid(row = 2, column= 0)
entry_vehicles = ttk.Entry(root, width = 10)
# entry_vehicles.place(x=90, y=120)
entry_vehicles.grid(row = 3, column= 0)

check_vehicles = ttk.Checkbutton(root, text='Emprar tots els vehicles?', variable=all_vehicles, offvalue=0, onvalue=1)
# check_vehicles.place(x=20, y=170)
check_vehicles.grid(row = 4, column= 0)

check_long = ttk.Checkbutton(root, text='Penalitzar diferència temps entre rutes?', variable=pen_longroute, offvalue=0, onvalue=1)
# check_long.place(x=20, y=220)
check_long.grid(row = 5, column= 0)

def button_function():
    print('Button callback')
    print(readonlycombo.current())


# Accentbutton
accentbutton = ttk.Button(root, text='Compute routes', style='Accentbutton', command=button_function)
accentbutton.place(x=400, y=450)


# # Sizegrip
# sizegrip = ttk.Sizegrip(root)
# sizegrip.pack(padx=5, pady=5, side='bottom', anchor='se')

# Create a Frame for the Checkbuttons
#TODO: Do not place them until a Route is selected!
checkframe = ttk.LabelFrame(root, text='Checkbuttons', width=210, height=400)


# Checkbuttons
check1 = ttk.Checkbutton(checkframe, text='Unchecked', variable=a, offvalue=0, onvalue=1)


check2 = ttk.Checkbutton(checkframe, text='Checked', variable=b, offvalue=0, onvalue=1)


check3 = ttk.Checkbutton(checkframe, text='Third state', variable=c, offvalue=0, onvalue=1)
check3.state(['alternate'])


check4 = ttk.Checkbutton(checkframe, text='Disabled', state='disabled')


if readonlycombo.current() > 0:
    checkframe.place(x=300, y=12)
    check1.place(x=300, y=20)
    check2.place(x=300, y=60)
    check3.place(x=300, y=100)
    check4.place(x=300, y=140)

# img_path = Path("C:/Users/leogonzalez.VILARRIBA/Desktop/FFerrer_VRP/imatges")
# photo = tk.PhotoImage(file = img_path / 'vehicle_5.png')
# root.wm_iconphoto(False, photo)

root.mainloop()
# %%
