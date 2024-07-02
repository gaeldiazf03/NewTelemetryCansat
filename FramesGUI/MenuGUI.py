import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk

# My ports
from ToolsGUI.ArduinoConnection import get_ports
from settings import bauds_list, font, colores, themename


class Menu_Frame(ttk.Frame):
    _bauds: list[str] = bauds_list
    _str_port = "No port selected"

    def __init__(self, parent, *args, **kwargs):
        super().__init__(master=parent, *args, **kwargs)

        # Variables de control
        self.previous_ports: list[str] = []  # Lista para almacenar los puertos
        self.selected_port: tk.StringVar = tk.StringVar()
        self.selected_baud: tk.StringVar = tk.StringVar()
        self.selected_baud.set("Baudios:")

        self.configure(width=1700, height=70, bootstyle=DARK, padding=(5, 10))

        # Menubutton Configuration
        self.style_menubutton = ttk.Style()
        self.style_menubutton.configure('Custom.TMenubutton', font=font, background=colores['primary'])

        self.add_spacer(False)  # Initial Separation

        self.file_menu = ttk.Menubutton(self, text='Archivo', style='Custom.TMenubutton')
        self.file_menu.pack(side='left', padx=100)
        self.archivos = ttk.Menu(self.file_menu, font=font)
        self.archivos.add_command(label="Reiniciar", command=lambda: print("reiniciar app"))
        self.archivos.add_command(label="Guardar", command=lambda: print("guardar xlsx"))
        self.file_menu["menu"] = self.archivos

        self.add_spacer()  # Separation
        self.add_spacer()  # Separation
        self.add_spacer()  # Separation

        self.puertos_menu = ttk.Menubutton(
            self,
            textvariable=self.selected_port,
            style='Custom.TMenubutton')
        self.puertos_menu.pack(side='left')
        self.puertos = ttk.Menu(self.file_menu, font=font)
        self.update_ports()
        self.puertos_menu["menu"] = self.puertos

        self.add_spacer(False)  # Separation

        self.baudios_puerto = ttk.Menubutton(
            self,
            textvariable=self.selected_baud,
            style='Custom.TMenubutton')
        self.baudios_puerto.pack(side='left', padx=100)
        self.bauds = ttk.Menu(self.baudios_puerto, font=font)
        for baud in self._bauds:
            self.bauds.add_radiobutton(
                label=baud,
                value=baud,
                variable=self.selected_baud,
                command=lambda b=baud: self.set_baud(b))
        self.baudios_puerto["menu"] = self.bauds

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

    def get_baud(self):
        return self.selected_baud.get()

    def set_port(self, port):
        self.selected_port.set(port)
        self.puertos_menu["text"] = port

    def get_port(self):
        return self.selected_port.get()

    # Function just to add design
    def add_spacer(self, expansion=True):
        spacer = ttk.Frame(self)  # Este ancho se debe de editar
        spacer.pack(side='left', expand=expansion)


if __name__ == '__main__':
    app = ttk.Window(themename=themename)
    app.title('Probando Menus')
    app.geometry('1700x723')

    frame = Menu_Frame(app)
    frame.pack(fill="x")

    other_button = ttk.Button(app, text='Otro')
    other_button.pack()

    app.mainloop()
