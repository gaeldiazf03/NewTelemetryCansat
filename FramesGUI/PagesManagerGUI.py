import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from settings import geometry, themename, font, colores


class PagesManager(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(width=150, height=723, bootstyle=DARK)  # Style
        self.pack_propagate(False)

        self.style_btn = ttk.Style()    # Button Style
        self.style_btn.configure(       # Botón en estado normal (estático)
            'Custom.TButton',
            font=font,
            foreground=colores['light'],
            background=colores['dark'],
            bordercolor=colores['dark'],
            borderwidth=0,
            relief="solid"
        )
        self.style_btn.map(             # Botón cuando está enfocado (dinámico)
            'Custom.TButton',
            background=[('active', colores['background']), ('!active', colores['dark'])],
            focuscolor=[('!active', colores['background'])],
            bordercolor=[('focus', colores['dark'])],
            relief=[('focus', colores['dark'])]
        )

        # Buttons
        self.monitor_btn = ttk.Button(
            self,
            text='Monitor',
            style='Custom.TButton',
            command=lambda: self.logic_indicator(self.monitor_indicator)
        )
        self.monitor_btn.place(y=200, relx=0.44, anchor=CENTER)
        self.monitor_indicator = ttk.Label(
            self,
            text=' \n',
            background=colores['dark']
        )
        self.monitor_indicator.place(y=201, relx=0.06, anchor=CENTER)

        self.serial_btn = ttk.Button(
            self,
            text='Serial',
            style='Custom.TButton',
            command=lambda: self.logic_indicator(self.serial_indicator)
        )
        self.serial_btn.place(y=300, relx=0.4, anchor=CENTER)
        self.serial_indicator = ttk.Label(
            self,
            text=' \n',
            background=colores['dark']
        )
        self.serial_indicator.place(y=301, relx=0.06, anchor=CENTER)

        self.registro_btn = ttk.Button(
            self,
            text='Excel',
            style='Custom.TButton',
            command=lambda: self.logic_indicator(self.registro_indicator)
        )
        self.registro_btn.place(y=400, relx=0.35, anchor=CENTER)
        self.registro_indicator = ttk.Label(
            self,
            text=' \n',
            background=colores['dark']
        )
        self.registro_indicator.place(y=401, relx=0.06, anchor=CENTER)

    # Comandos
    def logic_indicator(self, lbl: ttk.Label):
        self.logic_hideIndicator()

        lbl['background'] = colores['primary']

    def logic_hideIndicator(self):
        self.monitor_indicator['background'] = colores['dark']
        self.serial_indicator['background'] = colores['dark']
        self.registro_indicator['background'] = colores['dark']


if __name__ == '__main__':
    app = ttk.Window(themename=themename)
    app.title('PagesManagerGUI')
    app.geometry(geometry)

    frame = PagesManager(app)
    frame.pack(side=LEFT)

    app.mainloop()
