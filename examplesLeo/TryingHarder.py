# %% TODO: Get current list of routes and plot them in checkbox. Disable some or add others with ticks!
import tkinter as tk
from tkinter import ttk
from pathlib import Path
import json
from datetime import datetime, date
import random
import string


with open(Path("examplesLeo")/ "config_rutes.json", "r") as jsonfile: #Here we have the config file with the predefined routes
    rutes_predeterminades = json.load(jsonfile)

readonlycombo_list = ['Selecciona ruta']
for k in rutes_predeterminades.keys():
    readonlycombo_list.append(k)
readonlycombo_list.append("Nova ruta")

root = tk.Tk()
root.title('Rutes Vilar i Riba')
# Place the window in the center of the screen
windowWidth = 650
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

# Create control variables
data = tk.StringVar(value = date.today().strftime("%d/%m/%Y"))
num_vehicles = tk.IntVar() #TODO: Change value when selecting route!
all_vehicles = tk.IntVar(value = 1)
pen_longroute = tk.IntVar(value = 1)
a = tk.IntVar()
b = tk.IntVar(value=1)
c = tk.IntVar()



    

def create_frame1():
    global frame, data, num_vehicles, rutes_seleccionades, premadeList
    frame = tk.Frame(root)
    frame.pack(side = "left", anchor = "nw")
    # Entry
    label_data = tk.Label(frame, text = "Data ")
    label_data.grid(row = 0, column= 0)
    entry_data = ttk.Entry(frame, textvariable = data, width = 10)
    entry_data.grid(row = 0, column= 1)
    readonlycombo = ttk.Combobox(frame, state='readonly', value=readonlycombo_list)
    readonlycombo.current(0)
    readonlycombo.grid(row = 1, column = 0)

    label_vehicles = tk.Label(frame, text = "# Vehicles ")
    label_vehicles.grid(row = 2, column= 0)
    entry_vehicles = ttk.Entry(frame, textvariable= num_vehicles, width = 10)
    entry_vehicles.grid(row = 2, column= 1)

    check_vehicles = ttk.Checkbutton(frame, text='Emprar tots els vehicles?', variable=all_vehicles, offvalue=0, onvalue=1)
    check_vehicles.grid(row = 3, column= 0)

    check_long = ttk.Checkbutton(frame, text='Penalitzar diferència temps entre rutes?', variable=pen_longroute, offvalue=0, onvalue=1)
    check_long.grid(row = 4, column= 0)


    def button_function():
        print('Button callback')
        print(num_vehicles.get())


    


    frame1 = tk.Frame(root)
    frame1.pack(side = "right", anchor = "nw")
    # Create a Frame for the Checkbuttons
    #TODO: Do not place them until a Route is selected!
    checkframe = ttk.LabelFrame(frame1, text='Rutes seleccionades', width=210, height=500)

    # Checkbuttons
    
    

    for row, checkBoxName in enumerate(premadeList):
        c = tk.Checkbutton(checkframe, text=checkBoxName)
        c.place(x = 20, y = 20+40*row)
    b = tk.Button(checkframe, text="Add")
    b.pack()

    # check1 = ttk.Checkbutton(checkframe, text='Unchecked', variable=a, offvalue=0, onvalue=1)

    # check2 = ttk.Checkbutton(checkframe, text='Checked', variable=b, offvalue=0, onvalue=1)

    # check3 = ttk.Checkbutton(checkframe, text='Third state', variable=c, offvalue=0, onvalue=1)
    # check3.state(['alternate'])

    # check4 = ttk.Checkbutton(checkframe, text='Disabled', state='disabled')

    checkframe.pack()
    # check1.place(x=20, y=20)
    # check2.place(x=20, y=60)
    # check3.place(x=20, y=100)
    # check4.place(x=20, y=140)

    # Accentbutton
    accentbutton = ttk.Button(frame1, text='Compute routes', style='Accentbutton', command=button_function)
    accentbutton.pack()


    def callbackFunc(event):
        global premadeList
        opt = readonlycombo.current()
        print(opt)
        print(rutes_predeterminades[readonlycombo.get()])
        if opt != 0:
            frame1.pack_forget()
            frame1.pack(side = "top", anchor= "n")
        else:
            frame1.pack_forget()


    frame1.pack_forget()
    readonlycombo.bind("<<ComboboxSelected>>", callbackFunc)
    
premadeList = []
create_frame1()


root.mainloop()
# %%
