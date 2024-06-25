# GUI imports
import ttkbootstrap as ttk

# Graphical imports
import numpy as np
import matplotlib.pyplot as plt

# My imports
from ArduinoConnection import ArduinoConnection as ac
from ArduinoConnection import get_ports
from settings import config


# Inicia Clase Window (ventana principal)
app = ttk.Window(themename=config["style"])

# App Configuration
app.geometry(config["geometry"])
app.title(config["title"])
app.iconbitmap(config["icon"])

#  App Menu
menu = ttk.Menu(app, tearoff=True)

# File Menu
file_menu = ttk.Menu(menu, tearoff=True)
file_menu.add_command(label="Borrar todo", command=lambda: print("Borrar todo"))
file_menu.add_command(label="Guardar en xlsx", command=lambda: print("Guardar[xlsx]"))
menu.add_cascade(label="Archivo", menu=file_menu)

# Herramientas Menu
tools_menu = ttk.Menu(menu, tearoff=True)
port_submenu = ttk.Menu(tools_menu, tearoff=True)  # Submenu de puerto


def update_ports():
    port_submenu.delete(0, "end")
    for puerto in get_ports():
        port_submenu.add_radiobutton(label=puerto, command=lambda: print(puerto))  # Se agrega radiobutton
    app.after(250, update_ports)


tools_menu.add_cascade(label="Puerto", menu=port_submenu)
menu.add_cascade(label="Herramientas", menu=tools_menu)
# Add Menu
app.config(menu=menu)

# Actualizaciones
update_ports()

# Running App
app.mainloop()