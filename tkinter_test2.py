import tkinter as tk


window = tk.Tk()
window.title("Server Status")

canvas = tk.Canvas(window, height=600, width=1000, bg='#263D42')
canvas.pack()

txtf = tk.Entry(window, width=10)
txtf.pack()

window.mainloop()