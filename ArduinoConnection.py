import serial
import serial.tools.list_ports
import curses
import os
from measurement import singleton


@singleton
class ArduinoConnection:
    def __init__(self) -> None:
        self.vector = None
        self.baudrates = [9600, 115200]
        self.puertos = self.list_ports()
        self.reading = self.read()        

    def connect(self, port: str, baud: int = 115200) -> None:
        try:
            self.vector = serial.Serial(port, baud, timeout=0.1)
        except serial.SerialException:
            print("Could not connect to Arduino, check your connection and try again.")

    def disconnect(self) -> None:
        try:
            self.vector.close()
        except AttributeError:  # Si la conexión no es creada
            print("There is no serial connection!")

    def read(self) -> str:
        try:
            return str(self.vector.readline())
        except AttributeError:
            print("Couldn't read from Arduino!")

    @staticmethod
    def get_ports() -> list[str]:
        return [port.device for port in serial.tools.list_ports.comports()]
    

def example(stdscr):
    stdscr.clear()
    stdscr.nodelay(True)
    curses.curs_set(0)  # Ocultar el cursor
    vector = ArduinoConnection()
    lectura = vector.connect("COM13")

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, str(vector.get_ports()))

        stdscr.addstr(1, 0, "Lectura:")
        stdscr.addstr(2, 0, vector.read())

        stdscr.refresh()
        if stdscr.getch() == ord('q'):
            break


def main():
    curses.wrapper(example)


if __name__ == '__main__':
    os.system("cls")
    main()
