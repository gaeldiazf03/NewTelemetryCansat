import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import Frame, Label, Canvas, Scrollbar
from ToolsGUI import ArduinoConnection
import threading
import queue


class SerialContainer(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(padding=(15, 30, 15, 30))

        self.serial_data_queue = queue.Queue()  # Cola para los datos seriales

        self.canvas = Canvas(self)
        self.scroll_y = Scrollbar(self, orient='vertical', command=self.canvas.yview)

        self.scroll_frame = ttk.Frame(self.canvas)
        self.scroll_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scroll_y.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scroll_y.pack(side="right", fill="y")

        self.update_serial_text()  # Iniciar la actualización de la GUI

    def update_serial_text(self):
        # Procesar los datos en la cola y actualizarlos en la GUI
        while not self.serial_data_queue.empty():
            data = self.serial_data_queue.get()
            label = Label(self.scroll_frame, text=data, anchor='w', justify='left')
            label.pack(fill='x')

        # Programar la siguiente actualización
        self.after(100, self.update_serial_text)


class SerialReader:
    def __init__(self, port, baudrate, data_queue):
        self.port = port
        self.baudrate = baudrate
        self.data_queue = data_queue
        self.serial = ArduinoConnection()
        self.serial.connect(port, baudrate)
        self.running = True

    def read_serial(self):
        while self.running:
            try:
                data = self.serial.read()
                self.data_queue.put(data)  # Poner datos en la cola
            except Exception as e:
                print(f"Error leyendo del puerto serial: {e}")

    def start_reading(self):
        threading.Thread(target=self.read_serial, daemon=True).start()

    def stop_reading(self):
        self.running = False
        self.serial.disconnect()


if __name__ == '__main__':
    app = ttk.Window()
    app.title('Serial')
    app.geometry('500x500')

    serial_frame = SerialContainer(app)
    serial_frame.pack(fill=BOTH, expand=True)

    # Iniciar la lectura serial
    serial_reader = SerialReader("COM4", 115200, serial_frame.serial_data_queue)
    serial_reader.start_reading()

    app.mainloop()

    serial_reader.stop_reading()
