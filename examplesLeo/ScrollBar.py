# %% 
import tkinter as tk
from tkinter import ttk
from pathlib import Path
import json
from datetime import datetime, date
from HtmlWindow import *
import webbrowser

import time 

with open(Path("examplesLeo")/ "config_rutes.json", "r") as jsonfile: #Here we have the config file with the predefined routes
    rutes_predeterminades = json.load(jsonfile)


class ScrollbarFrame(tk.Frame):
    """
    Extends class tk.Frame to support a scrollable Frame 
    This class is independent from the widgets to be scrolled and 
    can be used to replace a standard tk.Frame
    """
    def __init__(self, parent, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)

        # The Scrollbar, layout to the right
        vsb = tk.Scrollbar(self, orient="vertical")
        # vsb.pack(side="right", fill="y")
        vsb.grid(row = 0, column= 1, sticky = "NESE")#, rowspan= 10



        # The Canvas which supports the Scrollbar Interface, layout to the left
        self.canvas = tk.Canvas(self, borderwidth=0)
        # self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.grid(row = 0, column= 0, rowspan=3, sticky = "NESE")#rowspan= 10, columnspan= 2, sticky = tk.NSEW)

        # Bind the Scrollbar to the self.canvas Scrollbar Interface
        self.canvas.configure(yscrollcommand=vsb.set)
        vsb.configure(command=self.canvas.yview)

        # The Frame to be scrolled, layout into the canvas
        # All widgets to be scrolled have to use this Frame as parent
        self.scrolled_frame = tk.Frame(self.canvas, background=self.canvas.cget('bg'))
        self.canvas.create_window((4, 4), window=self.scrolled_frame, anchor="nw")

        # Configures the scrollregion of the Canvas dynamically
        self.scrolled_frame.bind("<Configure>", self.on_configure)

    def on_configure(self, event):
        """Set the scroll region to encompass the scrolled frame"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    
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
windowWidth = 640
windowHeight = 550
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
xCordinate = int((screenWidth/2) - (windowWidth/2))
yCordinate = int((screenHeight/2) - (windowHeight/2))
root.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, xCordinate, yCordinate))
print(screenWidth, screenHeight )
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
cur_opt = 0

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
            #Open Excel file

            y = data.split("/")[-1]
            m = data.split("/")[-2]
            if len(m) <2:
                m = '0' + m
            d = data.split("/")[-0]
            if len(m) <2:
                d = '0' + d
            print(y,m,d)

            
            webbrowser.open(f'C:\\Users\\leogonzalez.VILARRIBA\\OneDrive - VILAR RIBA\\Rutes_FFerrer\\output\\Guessmicroroutes_solutions{y}-{m}-{d}.xlsx') 

            
            # map_path = f'C:/Users/leogonzalez.VILARRIBA/OneDrive - VILAR RIBA/Rutes_FFerrer/Microlineplot_ruta_{y}-{m}-{d}' #TODO: NO PUEDE HABER ESPACIOS EN EL NOMBRE!
            map_path =  'C:/Users/leogonzalez.VILARRIBA/Documents/GitHub/Azure-ttk-theme/examplesLeo/Microlineplot_ruta_2022-08-17'
            app = MainFrame(newWindow, url_path = map_path)
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

    accentbutton = ttk.Button(frame_sum, text='Confirmar càlcul rutes', style='Accentbutton', command=lambda: button_call(num_vehicles, data, rutes_calcular, newWindow))
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
    readonlycombo.current(1)
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
        running = True
        rutes_calcular = []
        for num, ruta in enumerate(rutes_seleccionades):
            if (ruta.get()):
                rutes_calcular.append(premadeList[num])

        num = num_vehicles.get()
        if num == 0:
            num = len(rutes_calcular)
        print(data.get(), num, rutes_calcular)
        openNewWindow(num, data.get(), rutes_calcular)

        # time.sleep(20)




    
    def onFrameConfigure(canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame1 = tk.Frame(root)

    frame1.pack(side = "right", anchor = "nw", fill = "both")

    canvas = tk.Canvas(frame1, borderwidth=0)
    frame2 = tk.Frame(canvas)
    vsb = tk.Scrollbar(frame1, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    # vsb.grid(row=0, column=2, sticky="ns")
    canvas.pack(side="left", fill="both", expand=True)
    # canvas.grid(row=0, column=0, rowspan=1, sticky="ns")
    canvas.create_window((4,4), window=frame2, anchor="nw")



    # Create a Frame for the Checkbuttons
    # checkframe = ttk.LabelFrame(frame1, text='Rutes seleccionades', width=210, height=500)


    # Checkbuttons
    def Buttone(premadeList, row, rowname):
        global frame, num_vehicles
        if rowname not in premadeList:
            premadeList.append(str(rowname))
        rutes_seleccionades[row+1] = tk.IntVar(value = 1)
        for widget in frame2.winfo_children():
            print(widget)
            if ~ ( isinstance(widget, tk.Scrollbar) or isinstance(widget,  tk.Canvas) ):
                    widget.destroy()
        checkframe = ttk.LabelFrame(frame2, text='Rutes seleccionades', width=210, height=500)
        for row, checkBoxName in enumerate(premadeList):
            c = ttk.Checkbutton(checkframe, text= str(checkBoxName), variable=rutes_seleccionades[row], offvalue=0, onvalue=1, width = 10)
            c.grid(row = row, column = 0)
            # c.place(x = 20, y = 20+40*row)
        new_row_text = ttk.Entry(checkframe, textvariable = new_ruta) #, width = 10
        new_row_text.grid(row = row+1, column= 0)
        b = ttk.Button(checkframe, text="Add", command= lambda: Buttone(premadeList, row, new_row_text.get()))
        b.grid(row = row+1, column = 1)
        # checkframe.grid(row = 0, column= 0)
        checkframe.pack()#

        accentbutton = ttk.Button(frame2, text='Compute routes', style='Accentbutton', command=button_function)
        # accentbutton.grid(row =1, column= 0)
        accentbutton.pack()#side = "left", fill = "x")

        #Change number vehicles
        nombre_seleccionats = 0
        
        for ruta in rutes_seleccionades:
            if (ruta.get() != 0):
                nombre_seleccionats += 1

        #Change left frame
        # cur_opt = readonlycombo.current()
        num_vehicles = tk.IntVar( value = nombre_seleccionats)
        for widget in frame.winfo_children():
            widget.destroy()
            
        label_data = tk.Label(frame, text = "Data ")
        label_data.grid(row = 0, column= 0)
        entry_data = ttk.Entry(frame, textvariable = data, width = 10)
        entry_data.grid(row = 0, column= 1)
        readonlycombo = ttk.Combobox(frame, state='readonly', value=readonlycombo_list)
        readonlycombo.current(cur_opt)
        readonlycombo.grid(row = 1, column = 0)

        label_vehicles = tk.Label(frame, text = "# Vehicles ")
        label_vehicles.grid(row = 2, column= 0)
        entry_vehicles = ttk.Entry(frame, textvariable= num_vehicles, width = 10)
        entry_vehicles.grid(row = 2, column= 1)

        check_vehicles = ttk.Checkbutton(frame, text='Emprar tots els vehicles?', variable=all_vehicles, offvalue=0, onvalue=1)
        check_vehicles.grid(row = 3, column= 0)

        check_long = ttk.Checkbutton(frame, text='Penalitzar diferència temps entre rutes?', variable=pen_longroute, offvalue=0, onvalue=1)
        check_long.grid(row = 4, column= 0)

        canvas.configure(scrollregion=canvas.bbox("all"))





    def callbackFunc(event):
        global premadeList, rutes_seleccionades, cur_opt
        cur_opt = readonlycombo.current()
        print(f"cur_opt = {cur_opt}")
        if readonlycombo.get() == "Nova ruta": #TODO: Fer aixo!!
            print("FER NOVA RUTA")
            
        elif cur_opt != 0:
            for widget in frame2.winfo_children():
                print(widget)
                if ~ ( isinstance(widget, tk.Scrollbar) or isinstance(widget,  tk.Canvas) ):
                    widget.destroy()
            premadeList = rutes_predeterminades[readonlycombo.get()]
            checkframe = ttk.LabelFrame(frame2, text='Rutes seleccionades', width=420, height=500)
            for row, checkBoxName in enumerate(premadeList):
                rutes_seleccionades[row] = tk.IntVar(value = 1)
                c = ttk.Checkbutton(checkframe, text= str(checkBoxName), variable=rutes_seleccionades[row], offvalue=0, onvalue=1, width = 10)
                c.grid(row = row, column= 0)
                # c.place(x = 20, y = 20+40*row)
                
            new_row_text = ttk.Entry(checkframe, textvariable = new_ruta, width = 10)
            new_row_text.grid(row = row+1, column= 0)
            b = ttk.Button(checkframe, text="Add", command= lambda: Buttone(premadeList, row, new_row_text.get()))
            b.grid(row = row+1, column = 1)
            # checkframe.grid(row = 0, column= 0, columnspan=2)
            checkframe.pack()#

            accentbutton = ttk.Button(frame2, text='Compute routes', style='Accentbutton', command=button_function)
            # accentbutton.grid(row =1, column= 0)
            accentbutton.pack()#side = "left", fill = "x")
            
        else:
            for widget in frame2.winfo_children():
                if ~ ( isinstance(widget, tk.Scrollbar) or isinstance(widget,  tk.Canvas) ):
                    widget.destroy()


    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120) ), "units")

    readonlycombo.bind("<<ComboboxSelected>>", callbackFunc)
    frame1.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
    root.bind_all("<MouseWheel>", _on_mousewheel)
    
premadeList = []
create_frame1()


root.mainloop()
# %%