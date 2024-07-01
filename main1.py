# GUI imports
import ttkbootstrap as ttk

# Graphical imports
# import numpy as np
# import matplotlib.pyplot as plt

# My imports
# from ArduinoConnection import ArduinoConnection as ac
from settings import themename
from MenuGUI import Menu_Frame


class SerialMonitorApp(ttk.Window):
    def __init__(self, geometry="1700x723", title="Probando Frames", icon="img\\sinFondo.ico", *args, **kwargs):
        super().__init__(themename=themename, *args, **kwargs)

        # Variable ttk que se utilizaran
        self.str_port = ttk.StringVar()
        self.str_port.set("No port")

        # Configuración de la ventana principal
        self.geometry(geometry)
        self.title(title)
        self.iconbitmap(icon)

        self.previous_ports = []  # Variable para almacenar la lista de puertos anterior

        # Crea menu y submenus
        self.menu_frame = Menu_Frame(self)
        self.menu_frame.configure(width=1700, height=70)
        self.menu_frame.pack(expand=False, fill="x")

        # Declarando Frames
        '''
        self.options_frames = OptionsFrame(self)
        self.options_frames.pack(pady=5)
        self.options_frames.pack_propagate(False)
        '''

        # Probando
        self.bind("<Delete>", self.probando_delete)
        self.bind("<Control-w>", self.exiting)

    def exiting(self, event):
        self.destroy()

    @staticmethod
    def probando_delete(event):
        print("Reiniciar gráficos")


# Ejecución de la aplicación
if __name__ == "__main__":
    app = SerialMonitorApp()
    app.mainloop()
