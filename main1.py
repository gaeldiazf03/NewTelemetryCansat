# GUI imports
import ttkbootstrap as ttk

# Graphical imports
# import numpy as np
# import matplotlib.pyplot as plt

# My imports
# from ArduinoConnection import ArduinoConnection as ac
import settings as st
from FramesGUI import Menu_Frame


class SerialMonitorApp(ttk.Window):
    def __init__(self,
                 geometry=st.geometry,
                 title=st.title,
                 icon=st.icon,
                 *args, **kwargs
                 ) -> None:
        super().__init__(themename=st.themename, *args, **kwargs)

        self.resizable(False, False)

        # Variable ttk que se utilizaran
        self.str_port = ttk.StringVar()
        self.str_port.set("No port")

        # Configuración de la ventana principal
        self.geometry(geometry)
        self.title(title)
        self.iconbitmap(icon)

        self.previous_ports = []  # Variable para almacenar la lista de puertos anterior

        # <FRAME> Crea menu y submenus
        self.menu_frame = Menu_Frame(self)
        self.menu_frame.pack(expand=False, fill="x")

        # <FRAME> Crea paginas diferentes

        # Probando
        self.bind("<Delete>", self.probando_delete)
        self.bind("<Control-w>", self.exiting)

    # noinspection PyUnusedLocal
    def exiting(self, event) -> None:
        self.destroy()

    @staticmethod
    def probando_delete(event) -> None:
        print("Reiniciar gráficos")


# Ejecución de la aplicación
if __name__ == "__main__":
    app = SerialMonitorApp()
    app.mainloop()
