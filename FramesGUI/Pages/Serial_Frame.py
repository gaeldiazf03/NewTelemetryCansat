# GUI imports
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText

# Tools imports
import time
from ToolsGUI import ArduinoConnection


font = ("Cascadia Code", 10, 'bold')  # Usado en esta página


class SerialContainer(ttk.Frame):
    _time_str = "<%d/%m/%Y, %H:%M:%S>"

    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)
        self.configure(padding=(15, 30, 15, 30))

        self.vector: ArduinoConnection = ArduinoConnection()

        self.serial_lblframe = ttk.Labelframe(
            self,
            text='Serial',
            style='info.TLabelFrame'
        )
        self.serial_lblframe.pack(fill=BOTH, expand=True)

        self.str_serial = ScrolledText(
            self.serial_lblframe,
            wrap=WORD,
            font=font,
            autohide=True,
            hbar=True
        )
        self.str_serial.text['state'] = 'disabled'
        self.str_serial.pack(fill=BOTH, expand=True, padx=15, pady=15)

        self.logic_scrolledText()

    def logic_scrolledText(self, *args, **kwargs) -> None:
        time_tuple = time.localtime()
        str_time = time.strftime(self._time_str, time_tuple)

        if self.vector.check_connection():
            data = self.vector.get_reading()
            if data:
                self.str_serial.text['state'] = 'normal'
                self.str_serial.text.insert(END, f'{str_time} {data}\n')
                self.str_serial.text.see(END)
                self.str_serial.text['state'] = 'disabled'
        self.after(100, self.logic_scrolledText)


if __name__ == '__main__':
    arduino = ArduinoConnection()
    arduino.connect("COM4", 115200)
    arduino.start_reading()

    app = ttk.Window()
    app.title('Serial')
    app.geometry('500x500')

    serial = SerialContainer(app)
    serial.pack(fill=BOTH, expand=True)

    app.mainloop()
    arduino.disconnect()
