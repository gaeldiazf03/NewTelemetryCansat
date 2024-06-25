# GUI imports
import ttkbootstrap as ttk

# Graphical imports
# import numpy as np
# import matplotlib.pyplot as plt

# My imports
# from ArduinoConnection import ArduinoConnection as ac
from ArduinoConnection import get_ports
from settings import themename


class SerialMonitorApp(ttk.Window):
    _bauds: list[str] = ['9600', '115200']

    def __init__(self, geometry="1700x723", title="Probando Frames", icon="img\\sinFondo.ico", *args, **kwargs):
        super().__init__(themename=themename, *args, **kwargs)

        # Configuración de la ventana principal
        self.geometry(geometry)
        self.title(title)
        self.iconbitmap(icon)

        self.previous_ports = []  # Variable para almacenar la lista de puertos anterior

        # Crea menu y submenus
        self.menu = ttk.Menu(self, tearoff=True)  # Se crea el objeto menu
        self.tools_menu = ttk.Menu(self.menu, tearoff=True)  # Primer menu de herramientas
        self.file_menu = ttk.Menu(self.menu, tearoff=True)
        self.port_submenu = ttk.Menu(self.tools_menu, tearoff=True)  # submenu de herramientas (puertos)
        self.baud_submenu = ttk.Menu(self.tools_menu, tearoff=True)  # Submenu de herramientas (baudios)
        self.create_menu()  # Función para crear los menus

        # Inicia llamada a la función de actualización de puertos
        self.update_ports()

    def create_menu(self):
        # menu de archivo
        self.file_menu.add_command(label="Reiniciar", command=lambda: print("Reiniciar app"))  # Reiniciar app
        self.file_menu.add_command(label="Guardar en xlsx", command=lambda: print("Guardar[xlsx]"))  # Guarda xlsx

        # menu de herramientas
        self.tools_menu.add_cascade(label="Puerto", menu=self.port_submenu)
        self.tools_menu.add_cascade(label="Baudios", menu=self.baud_submenu)

        for baud in self._bauds:
            self.baud_submenu.add_radiobutton(label=baud, command=lambda b=baud: print(b))

        # Se agregan a cascada en el menu
        self.menu.add_cascade(label="Archivo", menu=self.file_menu)
        self.menu.add_cascade(label="Herramientas", menu=self.tools_menu)

        self.config(menu=self.menu)  # Asigna los menús a la aplicación

    def update_ports(self):
        current_ports = get_ports()

        # Si los puertos no han cambiado, no actualizamos el menu
        if current_ports != self.previous_ports:
            self.previous_ports = current_ports  # Actualizamos lista de puertos
            self.port_submenu.delete(0, ttk.END)  # Limpia los elementos del submenu de puertos

            # Añade los nuevos puertos al submenu
            for puerto in current_ports:
                self.port_submenu.add_radiobutton(label=puerto, command=lambda p=puerto: print(p))

        self.after(250, self.update_ports)  # Programa la siguiente actualización en 250 milisegundos


# Ejecución de la aplicación
if __name__ == "__main__":
    app = SerialMonitorApp()
    app.mainloop()
