import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import scrolledtext
from settings import font
import serial
import threading
import queue
import time


class SerialContainer(ttk.Frame):
    _time_str = "<%d/%m/%Y, %H:%M:%S>"

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(padding=(15, 30, 15, 30))

        self.serial_data_queue = queue.Queue()  # Cola para los datos seriales
        self.serial_lblframe = ttk.Labelframe(
            self,
            text='Serial',
            style='info.TLabelFrame'
        )
        self.serial_lblframe.pack(fill=BOTH, expand=True)

        self.str_serial = scrolledtext.ScrolledText(
            self.serial_lblframe,
            wrap=WORD,
            font=font
        )
        self.str_serial.pack(fill=BOTH, expand=True, padx=15, pady=15)

        self.update_serial_text()  # Iniciar la actualización de la GUI

    def update_serial_text(self):
        # Procesar los datos en la cola y actualizarlos en la GUI
        if not self.serial_data_queue.empty():
            data = self.serial_data_queue.get()
            time_tuple = time.localtime()
            time_str = time.strftime(self._time_str, time_tuple)
            self.str_serial['state'] = 'normal'
            self.str_serial.insert(END, f'{time_str} {data}\n')
            self.str_serial.see(END)
            self.str_serial['state'] = 'disabled'

        # Programar la siguiente actualización
        self.after(100, self.update_serial_text)


class SerialReader:
    def __init__(self, port, baudrate, data_queue):
        self.port = port
        self.baudrate = baudrate
        self.data_queue = data_queue
        self.serial = serial.Serial(port, baudrate)
        self.running = True

    def read_serial(self):
        while self.running:
            try:
                data = self.serial.readline().decode('utf-8').strip()
                self.data_queue.put(data)  # Poner datos en la cola
            except Exception as e:
                print(f"Error leyendo del puerto serial: {e}")

    def start_reading(self):
        threading.Thread(target=self.read_serial, daemon=True).start()

    def stop_reading(self):
        self.running = False
        self.serial.close()


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
