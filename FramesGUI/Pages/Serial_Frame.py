# GUI imports
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import scrolledtext

# Tools imports
import time
from ToolsGUI import ArduinoConnection


font = ("Cascadia Code", 10, 'bold')


class SerialContainer(ttk.Frame):
    _time_str = "<%d/%m/%Y, %H:%M:%S>"

    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)
        self.configure(padding=(15, 30, 15, 30))

        self.serial_variable: ttk.StringVar = ttk.StringVar()
        self.serial_variable.trace('w', self.logic_scrolledText)

        self.serial_lblframe = ttk.Labelframe(
            self,
            text='Serial',
            style='info.TLabelFrame'
        )
        self.serial_lblframe.pack(fill=BOTH, expand=True)

        self.str_serial = scrolledtext.ScrolledText(
            self.serial_lblframe,
            wrap=WORD,
            font=font,
            state='disabled'
        )
        self.str_serial.pack(fill=BOTH, expand=True, padx=15, pady=15)

        self.logic_scrolledText()

    def set_serial(self, str_serial: str) -> None:
        self.serial_variable.set(str_serial)

    def get_serial(self) -> str:
        return self.serial_variable.get()

    def logic_scrolledText(self, *args, **kwargs) -> None:
        time_tuple = time.localtime()
        time_str = time.strftime(self._time_str, time_tuple)
        new_serial = self.get_serial()

        self.str_serial['state'] = 'normal'
        self.str_serial.insert(END, f'{time_str} {new_serial}\n')
        self.str_serial.see(END)
        self.str_serial['state'] = 'disabled'


if __name__ == '__main__':
    arduino = ArduinoConnection()
    arduino.connect("COM4", 115200)
    arduino.start_reading()

    app = ttk.Window()
    app.title('Serial')
    app.geometry('500x500')

    serial = SerialContainer(app)
    serial.pack(fill=BOTH, expand=True)

    def read_serial() -> None:
        try:
            reads = arduino.get_reading()
            if reads:
                serial.set_serial(reads)
                print(serial.get_serial())
        except Exception as e:
            print(e)

    read_serial()
    app.after(200, read_serial)

    app.mainloop()

    arduino.disconnect()
