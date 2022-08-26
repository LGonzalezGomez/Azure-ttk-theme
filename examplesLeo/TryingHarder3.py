# %% TODO: Get current list of routes and plot them in checkbox. Disable some or add others with ticks!
import tkinter as tk
from tkinter import ttk
from pathlib import Path
import json
from datetime import datetime, date
from HtmlWindow import *

import time


with open(Path("examplesLeo")/ "config_rutes.json", "r") as jsonfile: #Here we have the config file with the predefined routes
    rutes_predeterminades = json.load(jsonfile)



readonlycombo_list = ['Selecciona ruta']
for k in rutes_predeterminades.keys():
    readonlycombo_list.append(k)
readonlycombo_list.append("Nova ruta")

root = tk.Tk()
root.title('Rutes Vilar i Riba')

img_path = Path("C:/Users/leogonzalez.VILARRIBA/Desktop/FFerrer_VRP/imatges")
photo = tk.PhotoImage(file = img_path / 'vehicle_5.png')
root.wm_iconphoto(False, photo)

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
new_ruta = tk.StringVar(value = "###")
num_vehicles = tk.IntVar() #TODO: Change value when selecting route!
all_vehicles = tk.IntVar(value = 1)
pen_longroute = tk.IntVar(value = 1)
a = tk.IntVar()
b = tk.IntVar(value=1)
c = tk.IntVar()

rutes_seleccionades = [tk.IntVar(value = 0) for i in range(50)]

solving_routes = False
running = False

def create_frame_summarySim(newWindow, num_vehicles, data, rutes_calcular):
    global frame_sum
    
    def button_call(num_vehicles, data, rutes_calcular, newWindow):
        def solve_routes(num_vehicles, data, rutes_calcular):
            global running
            if running:
                print("It is running")
                time.sleep(2)
                 #erase children and create new plot
                for widget in newWindow.winfo_children():
                    widget.destroy()
                newWindow.title("Rutes Calculades...")
                running = False
            tk.Label(newWindow, text ="Rutes solucionades. Aqui es mostraria el plot!").pack() 

            sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
            app = MainFrame(newWindow)
            # Tk must be initialized before CEF otherwise fatal error (Issue #306)
            cef.Initialize() 
            app.mainloop()
            # cef.shutdown()


        solve_routes(num_vehicles, data, rutes_calcular)

    frame_sum = tk.Frame(newWindow)
    frame_sum.pack(side = "left", anchor = "nw")
    # Entry
    label_data = tk.Label(frame_sum, text = f"Data --> {data} ", width = 30, justify="left", anchor="w")
    label_data.grid(row = 0, column= 0)
    label_Nvehicles = tk.Label(frame_sum, text = f"# Vehicles --> {num_vehicles}", width = 30, justify="left", anchor="w")
    label_Nvehicles.grid(row = 1, column= 0)
    if(all_vehicles.get()):
        text = f"Emprant tota la flota"
    if(all_vehicles.get()):
        text = f"Minimitzant nombre vehicles emprats"
    label_Tvehicles = tk.Label(frame_sum, text = text, width = 30, justify="left", anchor="w")
    label_Tvehicles.grid(row = 2, column= 0)

    if(pen_longroute.get()):
        text = f"Penalitzant rutes llargues"
    if(pen_longroute.get()):
        text = f"No penalitzant rutes llargues"
    label_long = tk.Label(frame_sum, text = text, width = 30, justify="left", anchor="w")
    label_long.grid(row = 3, column= 0)

    checkframe = ttk.LabelFrame(frame_sum, text='Rutes seleccionades', width=210, height=500)
    for row, num_ruta in enumerate(rutes_calcular):
        l = tk.Label(checkframe, text = str(num_ruta))
        l.grid(row = row+4, column = 0)
    checkframe.grid(row = 4, column= 0, pady = 10)

    accentbutton = ttk.Button(frame_sum, text='Confirm compute routes', style='Accentbutton', command=lambda: button_call(num_vehicles, data, rutes_calcular, newWindow))
    accentbutton.grid(row =6, column= 0)
    




def openNewWindow(num_vehicles, data, rutes_calcular):
    print(running)

            
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    windowWidth = screenHeight
    windowHeight = screenHeight
    xCordinate = int((screenWidth/2) - (windowWidth/2))
    yCordinate = int((screenHeight/2) - (windowHeight/2))
    # Toplevel object which will
    # be treated as a new window
    newWindow = tk.Toplevel(root)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Calculant Rutes...")
 
    # sets the geometry of toplevel
    # newWindow.geometry("200x200")
    newWindow.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, xCordinate, yCordinate))
    
    create_frame_summarySim(newWindow, num_vehicles, data, rutes_calcular)

    # solving_routes = True
    # # A Label widget to show in toplevel
    # tk.Label(newWindow,
    #       text ="Calculant Rutes. Quan el càlcul hagi finalitzat sortirà un missatge i un mapa interactiu s'obrirà.").pack()    
    # newWindow.grab_set()
    
    

    # # time.sleep(10)
    # solving_routes = solve_routes(num_vehicles, data, rutes_calcular)

    # if solving_routes == False:
    #     #erase children and create new plot
    #     for widget in newWindow.winfo_children():
    #         widget.destroy()
    #     newWindow.title("Rutes Calculades...")
    #     #create new plot
    #     tk.Label(newWindow,
    #       text ="Rutes solucionades. Aqui es mostraria el plot!").pack()    

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
        global running
        print(running)
        running = True
        print(num_vehicles.get())
        print(data.get())
        rutes_calcular = []
        for num, ruta in enumerate(rutes_seleccionades):
            if (ruta.get()):
                rutes_calcular.append(premadeList[num])
        print(rutes_calcular)
        openNewWindow(num_vehicles.get(), data.get(), rutes_calcular)

        # time.sleep(20)




    


    frame1 = tk.Frame(root)
    frame1.pack(side = "right", anchor = "nw")
    # Create a Frame for the Checkbuttons
    #TODO: Do not place them until a Route is selected!
    # checkframe = ttk.LabelFrame(frame1, text='Rutes seleccionades', width=210, height=500)

    # Checkbuttons
    def Buttone(premadeList, row, rowname):
        if rowname not in premadeList:
            premadeList.append(str(rowname))
        rutes_seleccionades[row+1] = tk.IntVar(value = 1)
        for widget in frame1.winfo_children():
            widget.destroy()
        checkframe = ttk.LabelFrame(frame1, text='Rutes seleccionades', width=210, height=500)
        for row, checkBoxName in enumerate(premadeList):
            c = ttk.Checkbutton(checkframe, text= str(checkBoxName), variable=rutes_seleccionades[row], offvalue=0, onvalue=1)
            c.grid(row = row, column = 0)
            # c.place(x = 20, y = 20+40*row)
        new_row_text = ttk.Entry(checkframe, textvariable = new_ruta, width = 10)
        new_row_text.grid(row = row+1, column= 0)
        b = ttk.Button(checkframe, text="Add", command= lambda: Buttone(premadeList, row, new_row_text.get()))
        b.grid(row = row+1, column = 1)
        checkframe.grid(row = 0, column= 0)

        accentbutton = ttk.Button(frame1, text='Compute routes', style='Accentbutton', command=button_function)
        accentbutton.grid(row =1, column= 0)
    



    def callbackFunc(event):
        global premadeList, rutes_seleccionades
        opt = readonlycombo.current()
        print(opt)
        
        if readonlycombo.get() == "Nova ruta":
            print("FER NOVA RUTA")
            
        elif opt != 0:
            for widget in frame1.winfo_children():
                widget.destroy()
            premadeList = rutes_predeterminades[readonlycombo.get()]
            checkframe = ttk.LabelFrame(frame1, text='Rutes seleccionades', width=210, height=500)
            for row, checkBoxName in enumerate(premadeList):
                rutes_seleccionades[row] = tk.IntVar(value = 1)
                c = ttk.Checkbutton(checkframe, text= str(checkBoxName), variable=rutes_seleccionades[row], offvalue=0, onvalue=1)
                c.grid(row = row, column= 0)
                # c.place(x = 20, y = 20+40*row)
            new_row_text = ttk.Entry(checkframe, textvariable = new_ruta, width = 10)
            new_row_text.grid(row = row+1, column= 0)
            b = ttk.Button(checkframe, text="Add", command= lambda: Buttone(premadeList, row, new_row_text.get()))
            b.grid(row = row+1, column = 1)
            checkframe.grid(row = 0, column= 0)

            accentbutton = ttk.Button(frame1, text='Compute routes', style='Accentbutton', command=button_function)
            accentbutton.grid(row =1, column= 0)
            
        else:
            for widget in frame1.winfo_children():
                widget.destroy()


    readonlycombo.bind("<<ComboboxSelected>>", callbackFunc)
    
premadeList = []
create_frame1()


root.mainloop()
# %%