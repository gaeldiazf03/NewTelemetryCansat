import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from settings import geometry, themename, colores
from PagesManagerGUI import PagesManager


class MainFrame(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(bootstyle=LIGHT)
        self.pack_propagate(False)

        # Temporal Style
        self.style = ttk.Style()
        self.style.configure('Custom.TFrame', background=colores['light'])
        self.configure(style='Custom.TFrame')

        # Page Manager
        self.configure_frame = PagesManager(self)
        self.configure_frame.pack(side='left', expand=False, fill='y')


if __name__ == '__main__':
    root = ttk.Window(themename=themename)
    root.title('Probando main GUI')
    root.geometry(geometry)

    # Main Frame
    main_frame = MainFrame(root)
    main_frame.pack(expand=True, fill='both')

    # Principal Mainloop
    root.mainloop()
