import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
import threading
import time

# My ports
from ToolsGUI.ArduinoConnection import get_ports, ArduinoConnection
from settings import bauds_list, font, colores, themename


class MenuFrame(ttk.Frame):
    _bauds: list[str] = bauds_list
    _str_port = "No port selected"

    def __init__(self, parent, *args, **kwargs):
        super().__init__(master=parent, *args, **kwargs)

        # Variables de control
        self.previous_ports: list[str] = []  # Lista para almacenar los puertos
        self.selected_port: tk.StringVar = tk.StringVar()
        self.selected_baud: tk.StringVar = tk.StringVar()
        self.selected_baud.set("Baudios:")

        self.arduino_conn: ArduinoConnection = ArduinoConnection()
        self.running = False  # Flag to control the reading thread

        self.configure(width=1700, height=70, bootstyle=DARK, padding=(5, 10))

        # Menubutton Configuration
        self.style_menubutton = ttk.Style()
        self.style_menubutton.configure('Custom.TMenubutton', font=font, background=colores['primary'])
        # Button Configuration
        self.style_button = ttk.Style()
        self.style_button.configure('MyCustomButton.TButton', font=font, background=colores['primary'])

        self.add_spacer()  # Initial Separation

        self.file_menu = ttk.Menubutton(self, text='Archivo', style='Custom.TMenubutton')
        self.file_menu.pack(side='left', padx=100)
        self.archivos = ttk.Menu(self.file_menu, font=font)
        self.archivos.add_command(label="Reiniciar", command=lambda: print("reiniciar app"))
        self.archivos.add_command(label="Guardar", command=lambda: print("guardar xlsx"))
        self.file_menu["menu"] = self.archivos

        self.add_spacer()  # Separation
        self.add_spacer()  # Separation
        self.add_spacer()  # Separation
        self.add_spacer()  # Initial Separation

        self.puertos_menu = ttk.Menubutton(
            self,
            textvariable=self.selected_port,
            style='Custom.TMenubutton')
        self.puertos_menu.pack(side='left', padx=100)
        self.puertos = ttk.Menu(self.file_menu, font=font)
        self.update_ports()
        self.puertos_menu["menu"] = self.puertos

        self.add_spacer(False)  # Separation

        self.baudios_puerto = ttk.Menubutton(
            self,
            textvariable=self.selected_baud,
            style='Custom.TMenubutton')
        self.baudios_puerto.pack(side='left')
        self.bauds = ttk.Menu(self.baudios_puerto, font=font)
        for baud in self._bauds:
            self.bauds.add_radiobutton(
                label=baud,
                value=baud,
                variable=self.selected_baud,
                command=lambda b=baud: self.set_baud(b))
        self.baudios_puerto["menu"] = self.bauds

        self.add_spacer(False)

        self.btn_start_connection = ttk.Button(
            self,
            text='Not Connected',
            style='MyCustomButton.TButton',
            command=self.init_connection
        )
        self.btn_start_connection.pack(side='left', padx=100)

        self.add_spacer(False)

    def update_ports(self):
        current_ports = get_ports()

        if current_ports != self.previous_ports:
            self.previous_ports = current_ports
            self.puertos.delete(0, 'end')

            for port in current_ports:
                self.puertos.add_radiobutton(
                    label=port,
                    value=port,
                    variable=self.selected_port,
                    command=lambda p=port: self.set_port(p))

        if self.selected_port.get() not in current_ports:
            self.selected_port.set(self._str_port)

        if len(current_ports) < 1:
            self.selected_port.set("No port available")

        self.after(250, self.update_ports)

    def set_baud(self, baud):
        self.selected_baud.set(baud)
        self.baudios_puerto["text"] = baud
        if self.arduino_conn.check_connection():
            self.arduino_conn.disconnect()

    def get_baud(self):
        return int(self.selected_baud.get())

    def set_port(self, port):
        self.selected_port.set(port)
        self.puertos_menu["text"] = port
        if self.arduino_conn.check_connection():
            self.arduino_conn.disconnect()

    def get_port(self):
        return self.selected_port.get()

    def init_connection(self):
        threading.Thread(target=self._connect_and_update_button).start()

    def _connect_and_update_button(self):
        try:
            self.arduino_conn.connect(self.get_port(), self.get_baud())
            print("Connection established")

            self.running = True
            self.update_button_state("Connected", self.end_connection)
            self.start_reading_thread()  # Start reading in a separate thread
        except Exception as e:
            print(f"Error during connection: {e}")

    def end_connection(self):
        try:
            self.arduino_conn.disconnect()
            print("Connection closed")

            self.running = False
            self.update_button_state("Not Connected", self.init_connection)
        except Exception as e:
            print(f"Error during disconnection: {e}")

    def update_button_state(self, text, command):
        # Update the button in the main thread
        self.btn_start_connection["text"] = text
        self.btn_start_connection["command"] = command

    def start_reading_thread(self):
        thread = threading.Thread(target=self.print2terminal)
        thread.daemon = True
        thread.start()

    def print2terminal(self):
        while self.running:
            reading = self.arduino_conn.read()
            if reading:
                try:
                    print(reading)
                except Exception as e:
                    print(f"Error decoding reading: {e}")

            time.sleep(0.25)  # Sleep for 250ms to avoid too frequent reading

    def add_spacer(self, expansion=True):
        spacer = ttk.Frame(self)  # Este ancho se debe de editar
        spacer.pack(side='left', expand=expansion)


if __name__ == '__main__':
    app = ttk.Window(themename=themename)
    app.title('Probando Menus')
    app.geometry('1700x723')

    frame = MenuFrame(app)
    frame.pack(fill="x")

    other_button = ttk.Button(app, text='Otro')
    other_button.pack()

    app.mainloop()
