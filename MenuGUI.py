import ttkbootstrap as ttk
import tkinter as tk

# My ports
from ArduinoConnection import get_ports
from settings import bauds_list


class Menu_Frame(ttk.Frame):
    _bauds: list[str] = bauds_list
    _str_port = "No port selected"

    def __init__(self, parent, *args, **kwargs):
        super().__init__(master=parent, *args, **kwargs)

        # Variables de control
        self.previous_ports: list[str] = []  # Lista para almacenar los puertos
        self.selected_port: tk.StringVar = tk.StringVar()
        self.selected_baud: tk.StringVar = tk.StringVar()

        # Frame Configuration
        """
        self.configure(padding=(30, 5, 30, 10))
        self.style = ttk.Style()
        self.style.configure('Custom.TFrame', background='black')
        self.config(style='Custom.TFrame')
        """

        self.add_spacer(False)  # Initial Separation

        self.file_menu = ttk.Menubutton(self, text='Archivo')
        self.file_menu.pack(side='left', padx=100)
        self.archivos = ttk.Menu(self.file_menu)
        self.archivos.add_command(label="Reiniciar", command=lambda: print("reiniciar app"))
        self.archivos.add_command(label="Guardar", command=lambda: print("guardar xlsx"))
        self.file_menu["menu"] = self.archivos

        self.add_spacer()  # Separation
        self.add_spacer()  # Separation
        self.add_spacer()  # Separation

        self.puertos_menu = ttk.Menubutton(
            self,
            text=self._str_port,
            textvariable=self.selected_port)
        self.puertos_menu.pack(side='left')
        self.puertos = ttk.Menu(self.file_menu)
        self.update_ports()
        self.puertos_menu["menu"] = self.puertos

        self.add_spacer(False)  # Separation

        self.baudios_puerto = ttk.Menubutton(self, text='Baudios:')
        self.baudios_puerto.pack(side='left', padx=100)
        self.bauds = ttk.Menu(self.baudios_puerto)
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
    app = ttk.Window()
    app.title('Probando Menus')
    app.geometry('1700x723')

    frame = Menu_Frame(app)
    frame.configure(width=1700, height=70)
    frame.pack(fill="x")

    other_button = ttk.Button(app, text='Otro')
    other_button.pack()

    app.mainloop()
