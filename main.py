# GUI imports
import ttkbootstrap as ttk

# My imports
import settings as st
from FramesGUI import MenuFrame, MainFrame
from ToolsGUI import ArduinoConnection


class SerialMonitorApp(ttk.Window):
    def __init__(self,
                 geometry=st.geometry,
                 title=st.title,
                 icon=st.icon,
                 *args, **kwargs
                 ) -> None:
        super().__init__(themename=st.themename, *args, **kwargs)

        self.resizable(False, False)

        # Configuración de la ventana principal
        self.geometry(geometry)
        self.title(title)
        self.iconbitmap(icon)

        # <FRAME> Crea menu y submenus
        self.menu_frame = MenuFrame(self)
        self.menu_frame.pack(expand=False, fill="x")

        # <FRAME> Crea paginas diferentes
        self.pages_frame = MainFrame(self)
        self.pages_frame.pack(expand=True, fill="both")

        # Probando
        self.bind("<Delete>", self.probando_delete)
        self.bind("<Control-w>", self.exiting)
        self.bind("<Control-W>", self.exiting)

    # noinspection PyUnusedLocal
    def exiting(self, event) -> None:
        self.destroy()

    @staticmethod
    def probando_delete(event) -> None:
        print("Reiniciar gráficos")


# Ejecución de la aplicación
if __name__ == "__main__":
    connection: ArduinoConnection = ArduinoConnection()

    app = SerialMonitorApp()
    app.mainloop()

    # Bloque de seguridad
    if connection.check_connection() is True:
        connection.disconnect()
    else:
        pass
