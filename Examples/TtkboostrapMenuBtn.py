import ttkbootstrap as ttk


class CansatMenus(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.btn = ttk.Menubutton(self, text='Menu')
        self.btn.pack(padx=50, pady=10)

        self.item = ttk.StringVar()
        self.inside = ttk.Menu(self.btn)

        for i in range(50):
            self.inside.add_radiobutton(
                label=str(i),
                variable=self.item,
                command=lambda x=i: self.stuff(x))

        # Asociando
        self.btn["menu"] = self.inside

        self.lbl = ttk.Label(self, textvariable=self.item)
        self.lbl.pack(padx=50, pady=10)

    def stuff(self, sex):
        self.btn.config(text=sex)
        print(sex)
        self.item.set(sex)


if __name__ == '__main__':
    app = ttk.Window()
    app.title('Cansat')
    CansatMenus(app).pack()
    app.mainloop()
