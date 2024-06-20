import tkinter as tk
from tkinter import ttk
import serial.tools.list_ports
# import threading
# import time

class COMPortsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Puertos COM Disponibles")

        self.label = ttk.Label(root, text="Puertos COM disponibles:")
        self.label.pack(pady=10)

        self.ports_listbox = tk.Listbox(root, width=40, height=10)
        self.ports_listbox.pack(pady=5)

        self.update_button = ttk.Button(root, text="Actualizar", command=self.update_ports)
        self.update_button.pack(pady=5)

        self.close_button = ttk.Button(root, text="Cerrar", command=root.quit)
        self.close_button.pack(pady=5)

        self.updating = True
        self.update_ports()

    def get_ports(self):
        return [port.device for port in serial.tools.list_ports.comports()]

    def update_ports(self):
        self.ports_listbox.delete(0, tk.END)
        ports = self.get_ports()
        for port in ports:
            self.ports_listbox.insert(tk.END, port)
        
        if self.updating:
            # Actualizar cada 2 segundos
            self.root.after(2000, self.update_ports)

    def stop_updating(self):
        self.updating = False

def main():
    root = tk.Tk()
    app = COMPortsApp(root)

    def on_close():
        app.stop_updating()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

if __name__ == "__main__":
    main()
