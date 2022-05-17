import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)

root.mainloop()