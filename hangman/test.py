from tkinter import *


if __name__ == '__main__':
    root = Tk()
    root.geometry("600x300")
    canv = Canvas(root,width=300,height=300)
    canv.pack()
    canv.create_line( width=1)

    for i in range(26):
        print(i)
    root.mainloop()