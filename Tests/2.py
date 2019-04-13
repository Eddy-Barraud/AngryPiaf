import tkinter	
from threading import Thread
import time
testt=0
class infoWindow(Thread):
    def __init__(self):
        ''' Constructor. '''
        Thread.__init__(self)
 
    def run(self):
        root = tkinter.Tk()
        root.minsize(width=300, height=150)
        root.geometry('300x150+20+20')
        win = tkinter.Frame(root)
        win.pack()
        a=tkinter.Label(win, text=testt)
        a.pack(side=tkinter.TOP)
        for i in range(5):
            tkinter.Label(win, text="hello"+ str(i) + "!").pack(side=tkinter.TOP)
        while True:
            #win.mainloop()
            a.config(text="test \n back space")
            win.update_idletasks()
            win.update()


# Run following code when the program starts

# Declare objects of MyThread class
threadedWindow = infoWindow()

# Start running the threads!
threadedWindow.start()
# Wait for the threads to finish...
#myThreadOb1.join()
for i in range(20):
    testt=i
    time.sleep(0.1)