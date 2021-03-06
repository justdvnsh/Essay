import tkinter as tk
from tasky.start_page import StartPage

class Tasky(tk.TK):

    def _init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

     def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

app = Tasky()
app.mainloop()