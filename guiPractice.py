import tkinter as tk

#making a window
root = tk.Tk() #root is just an arbitrary name 
root.geometry('900x500') #this is the pixel count for the size of the window
root.title('budget program gui')

label = tk.Label(root, text='you can put anything in here for the text', font = ('Arial',11)) 
label.pack()

root.mainloop()