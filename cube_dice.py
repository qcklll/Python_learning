from tkinter import *

root = Tk()
root.title("Cube dice")
root.geometry("1920x1080")
btn = Button(root, text="Нажми!")
btn.config(command=lambda: print("Привет, Tkinter!"))
btn.pack(padx=250, pady=30)
root.mainloop()