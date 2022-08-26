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


# on = 1
# def reset_frame(evt):
#     global on, frame
#     if on:
#         frame.destroy()
#         create_frame0()
#         on = 0
#     else:
#         frame.destroy()
#         create_frame1()
#         on = 1
#     return on


def create_frame0():
    "create frame "
    # Entry
    frame = tk.Frame(root)
    entry_data = ttk.Entry(root, textvariable = data, width = 22)
    entry_data.place(x=20, y=20)
    # entry_data.insert(0)

    # Read-only combobox
    readonlycombo = ttk.Combobox(root, state='readonly', value=readonlycombo_list)
    readonlycombo.current(0)
    readonlycombo.place(x=20, y=70)

    label_vehicles = tk.Label(root, text = "# Vehicles ")
    label_vehicles.place(x= 20, y = 125)
    entry_vehicles = ttk.Entry(root, width = 10)
    entry_vehicles.place(x=90, y=120)

    check_vehicles = ttk.Checkbutton(root, text='Emprar tots els vehicles?', variable=all_vehicles, offvalue=0, onvalue=1)
    check_vehicles.place(x=20, y=170)

    check_long = ttk.Checkbutton(root, text='Penalitzar diferència temps entre rutes?', variable=pen_longroute, offvalue=0, onvalue=1)
    check_long.place(x=20, y=220)

    def button_function():
        print('Button callback')
        print(readonlycombo.current())


    # Accentbutton
    accentbutton = ttk.Button(root, text='Compute routes', style='Accentbutton', command=button_function)
    accentbutton.place(x=400, y=450)


    # Sizegrip
    sizegrip = ttk.Sizegrip(root)
    sizegrip.pack(padx=5, pady=5, side='bottom', anchor='se')


"create frame "
frame = tk.Frame(root)
frame.pack(side = "left")
# Entry
entry_data = ttk.Entry(frame, textvariable = data, width = 22)
entry_data.place(x=20, y=20)
# entry_data.insert(0)

# Read-only combobox
readonlycombo = ttk.Combobox(frame, state='readonly', value=readonlycombo_list)
readonlycombo.current(0)
readonlycombo.place(x=20, y=70)

label_vehicles = tk.Label(frame, text = "# Vehicles ")
label_vehicles.place(x= 20, y = 125)
entry_vehicles = ttk.Entry(frame, width = 10)
entry_vehicles.place(x=90, y=120)

check_vehicles = ttk.Checkbutton(frame, text='Emprar tots els vehicles?', variable=all_vehicles, offvalue=0, onvalue=1)
check_vehicles.place(x=20, y=170)

check_long = ttk.Checkbutton(frame, text='Penalitzar diferència temps entre rutes?', variable=pen_longroute, offvalue=0, onvalue=1)
check_long.place(x=20, y=220)

def button_function():
    print('Button callback')
    print(readonlycombo.current())


# Accentbutton
accentbutton = ttk.Button(frame, text='Compute routes', style='Accentbutton', command=button_function)
accentbutton.place(x=400, y=250)


# Sizegrip
sizegrip = ttk.Sizegrip(frame)
sizegrip.pack(padx=5, pady=5, side='bottom', anchor='se')


frame1 = tk.Frame(root)
frame1.pack(side = "right")
# Create a Frame for the Checkbuttons
#TODO: Do not place them until a Route is selected!
checkframe = ttk.LabelFrame(frame1, text='Checkbuttons', width=210, height=200)

# Checkbuttons
check1 = ttk.Checkbutton(checkframe, text='Unchecked', variable=a, offvalue=0, onvalue=1)

check2 = ttk.Checkbutton(checkframe, text='Checked', variable=b, offvalue=0, onvalue=1)

check3 = ttk.Checkbutton(checkframe, text='Third state', variable=c, offvalue=0, onvalue=1)
check3.state(['alternate'])

check4 = ttk.Checkbutton(checkframe, text='Disabled', state='disabled')

checkframe.place(x=300, y=12)
check1.place(x=20, y=20)
check2.place(x=20, y=60)
check3.place(x=20, y=100)
check4.place(x=20, y=140)
 





# img_path = Path("C:/Users/leogonzalez.VILARRIBA/Desktop/FFerrer_VRP/imatges")
# photo = tk.PhotoImage(file = img_path / 'vehicle_5.png')
# root.wm_iconphoto(False, photo)

root.mainloop()
# %%
