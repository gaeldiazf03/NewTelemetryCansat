import serial.tools.list_ports
import time
import curses

def get_ports():
    return [port.device for port in serial.tools.list_ports.comports()]

def display_ports(stdscr):
    stdscr.clear()
    stdscr.nodelay(True)
    curses.curs_set(0)  # Ocultar el cursor
    
    while True:
        stdscr.clear()
        ports = get_ports()
        
        stdscr.addstr(0, 0, "Puertos COM disponibles:")
        for idx, port in enumerate(ports, start=1):
            stdscr.addstr(idx, 0, port)
        
        stdscr.refresh()
        # time.sleep(2)  # Actualizar cada 2 segundos

        # Salir al presionar la tecla 'q'
        if stdscr.getch() == ord('q'):
            break

def main():
    curses.wrapper(display_ports)

if __name__ == "__main__":
    main()