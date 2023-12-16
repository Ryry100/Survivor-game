from tkinter import *
window = Tk()
def destroy_window():
    window.destroy()
def create_window():
    new_window = Toplevel()
    new_window.title='ANOTHER WINDOW'
    new_window.geometry('500x300')
    Label(new_window,text="YAY! You created another window!").pack()
    Button(new_window,text='Close all windows',command=destroy_window).pack()
    Button(new_window,text="Create a new window",command=create_window).pack()
window.geometry("999x299")
window.title("My First Window")

Label(window,text='this is a window').pack()

Button(window,text='this will create a new window',command=create_window).pack()
window.mainloop()