# Funciónes para la GUI
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter import messagebox
from time import sleep

from ToolsGUI.ArduinoConnection import get_ports, ArduinoConnection  # Mis funciones importadas
from settings import bauds_list, font, colores, themename  # Para CSS, pura decoración
from typing import List  # Es para especificar variables


class MenuFrame(ttk.Frame):
    _bauds: List[str] = bauds_list

    def __init__(self, parent, *args, **kwargs) -> None:
        super().__init__(master=parent, *args, **kwargs)

        # Variables de control
        self.previous_ports: list[str] = []  # Lista para almacenar los puertos
        self.selected_port: tk.StringVar = tk.StringVar()  # Selección de puerto
        self.selected_port.set("Not port")
        self.selected_baud: tk.StringVar = tk.StringVar()  # Selección de baudios
        self.selected_baud.set("Baudios:")
        self.arduino_conn: ArduinoConnection = ArduinoConnection()  # Define conexión arduino

        self.configure(  # Configuración del Frame
            width=1700,
            height=70,
            bootstyle=DARK,
            padding=(5, 10)
        )

        # Menubutton Configuration Style
        self.style_menubutton = ttk.Style()
        self.style_menubutton.configure('Custom.TMenubutton', font=font, background=colores['primary'])
        # Button Configuration Style
        self.style_button = ttk.Style()
        self.style_button.configure('MyCustomButton.TButton', font=font, background=colores['primary'])

        self.add_spacer()  # Separation

        # MenuButton referente al Archivo
        self.file_menu = ttk.Menubutton(self, text='Archivo', style='Custom.TMenubutton')
        self.file_menu.pack(side='left', padx=100)
        # Menu dentro del MenuButton
        self.archivos = ttk.Menu(self.file_menu, font=font)
        self.archivos.add_command(label="Reiniciar", command=self.reset_connection)
        self.archivos.add_command(label="Guardar", command=lambda: print("guardar xlsx"))
        # Se anexan al MenuButton
        self.file_menu["menu"] = self.archivos

        self.add_spacer()  # Separation
        self.add_spacer()  # Separation
        self.add_spacer()  # Separation
        self.add_spacer()  # Separation

        # MenuButton referente a los puertos
        self.puertos_menu = ttk.Menubutton(self, textvariable=self.selected_port, style='Custom.TMenubutton')
        self.puertos_menu.pack(side='left', padx=100)
        # Menu dentro del MenuButton
        self.puertos = ttk.Menu(self.file_menu, font=font)
        # Se anexan al MenuButton
        self.puertos_menu["menu"] = self.puertos

        # MenuButton referente a los baudios
        self.baudios_puerto = ttk.Menubutton(self, text='Baudios:', style='Custom.TMenubutton')
        self.baudios_puerto.pack(side='left')
        # Menu dentro del MenuButton
        self.bauds = ttk.Menu(self.baudios_puerto, font=font)
        for baud in self._bauds:  # Se ingresa a un ciclo para mostrar baudios
            self.bauds.add_radiobutton(
                label=baud,
                value=baud,
                variable=self.selected_baud,
                command=lambda b=baud: self.set_baud(b)
            )
        # Se anexan al MenuButton
        self.baudios_puerto["menu"] = self.bauds

        # Botón para conectarse al arduino
        self.btn_start_connection = ttk.Button(
            self,
            text='Not Connected',
            style='MyCustomButton.TButton',
            command=self.init_connection
        )
        self.btn_start_connection.pack(side='left', padx=100)

        self.update_ports()  # Constantemente se actualizan los puertos
        self.print2terminal()  # Intentará imprimir

    '''Referente a los puertos y los baudios'''
    def update_ports(self) -> None:
        current_ports = get_ports()

        if current_ports != self.previous_ports:
            self.previous_ports = current_ports
            self.puertos.delete(0, 'end')

            if self.selected_port.get() not in current_ports:
                self.selected_port.set("No port selected")

            if len(current_ports) < 1:
                self.selected_port.set("No port available")
            else:
                for port in current_ports:
                    self.puertos.add_radiobutton(
                        label=port,
                        value=port,
                        variable=self.selected_port,
                        command=lambda p=port: self.set_port(p))

        self.after(1000, self.update_ports)

    def set_baud(self, baud) -> None:
        self.selected_baud.set(baud)
        self.baudios_puerto["text"] = baud
        if self.arduino_conn.check_connection() is True:
            self.arduino_conn.disconnect()

    def set_port(self, port) -> None:
        self.selected_port.set(port)
        self.puertos_menu["text"] = port
        if self.arduino_conn.check_connection() is True:
            self.arduino_conn.disconnect()

    def get_baud(self) -> int:
        return int(self.selected_baud.get())

    def get_port(self) -> str:
        return self.selected_port.get()

    '''Referente a la conexión a arduino'''
    def init_connection(self) -> None:
        try:
            self.arduino_conn.connect(self.get_port(), self.get_baud())
            self.arduino_conn.reset_connection()
            self.arduino_conn.start_reading()
        except ValueError:
            print("Error con los baudios")
            messagebox.showerror(
                "Error con los baudios",
                "Ha ocurrido un error en la selección de los baudios"
            )
        except Exception as e:
            print(Exception(e))
            messagebox.showerror(
                "Error de conexión",
                "El puerto COM no esta disponible o no está seleccionado"
            )
        else:
            self.btn_start_connection["text"] = "Connected"
            self.btn_start_connection["command"] = self.end_connection
            print("Connection established")
            messagebox.showinfo(
                "Conexión Establecida",
                f"Se ha conectado a Arduino en el puerto {self.get_port()}, los baudios están disponibles en la velocidad {self.get_baud()}"
            )

    def end_connection(self) -> None:
        try:
            self.arduino_conn.disconnect()
        except Exception as e:
            print(f"Error: {e}")
        else:
            self.btn_start_connection["text"] = "Not Connected"
            self.btn_start_connection["command"] = self.init_connection
            print("Connection closed")

    def reset_connection(self):
        self.end_connection()
        sleep(1)
        self.init_connection()

    def print2terminal(self) -> None:
        if self.arduino_conn.check_connection():
            data = self.arduino_conn.get_reading()
            if data:
                print(data)
        self.after(100, self.print2terminal)

    # Function just to add design
    def add_spacer(self, expansion=True):
        spacer = ttk.Frame(self)  # Este ancho se debe de editar
        spacer.pack(side='left', expand=expansion)


if __name__ == '__main__':
    connection: ArduinoConnection = ArduinoConnection()

    app = ttk.Window(themename=themename)
    app.title('Probando Menus')
    app.geometry('1700x723')

    frame = MenuFrame(app)
    frame.pack(fill="x")

    app.mainloop()

    # Bloque de seguridad
    if connection.check_connection() is True:
        connection.disconnect()
        print("Connection Ended")
    else:
        print("Connection has been not established")
