import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from settings import geometry, themename


class PagesManager(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(width=220, height=723, bootstyle=DARK)  # Temporal Style
        self.pack_propagate(False)

        self.monitor_btn = ttk.Button


if __name__ == '__main__':
    app = ttk.Window(themename=themename)
    app.title('PagesManagerGUI')
    app.geometry(geometry)

    frame = PagesManager(app)
    frame.pack(side=LEFT)

    app.mainloop()
