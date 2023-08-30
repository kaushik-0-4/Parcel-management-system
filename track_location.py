from tkinter import *
from PIL import ImageTk, Image
#import chennai_places

#import chennai_places
master = Tk()
master.title('kj')
master.minsize(300,250)
Label(master, text='Enter city name').grid(row=0)
entry= Entry(master)
entry.grid(row=0, column=1)

def new_window():
    x=entry.get()
    print(x)
    master.destroy()
#master.destroy() 
    #def search():
    
    if x=="chennai":
        import chennai_places
    elif x=="madurai":# or "Madurai" or "MADURAI":
        import madurai
btn = Button(master, text = 'Click me !', command = new_window)
btn.place(x=100, y=20)

    
    

master.mainloop()
