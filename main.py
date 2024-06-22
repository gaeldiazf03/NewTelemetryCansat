import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class App(ttk.Window):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry('1700x723')  # Tamaño de la ventana (ratio 2.35:1)
        self.title('Probando ttkboostrap')
        icono = ttk.PhotoImage(file='img\\sinFondo.png')
        self.iconphoto(False, icono, icono)

        self.Frame_izq = ttk.Frame(self)
        self.Frame_der = ttk.Frame(self)
        self.Frame_izq.pack(side=LEFT)
        self.Frame_der.pack(side=RIGHT)


def main():
    configure = {
        "themename": "solar"  # Determina el tema de la ventana
    }

    app = App(**configure)
    app.mainloop()


if __name__ == "__main__":
    main()
