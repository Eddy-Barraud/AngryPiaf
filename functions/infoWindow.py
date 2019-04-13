import tkinter	
from threading import Thread
import functions.init as init
from time import sleep

class infoWindow(Thread):
    def __init__(self):
        ''' Constructor. '''
        Thread.__init__(self)
 
    def run(self):
        root = tkinter.Tk()
        root.title("Values")
        root.minsize(width=200, height=409)
        root.geometry('+2+155')
        win = tkinter.Frame(root)
        win.pack()
        verif=tkinter.Label(win, text='')
        verif.pack()        
        
        while init.running:
            init.values=f'verif: {init.verif} \ninMove: {init.inMove} \ncoord: {init.coord}\n'
            init.values+=f'coord (m): [{init.coord[0]/100},{(350-init.coord[1])/100}] \nbird.pointnb: {init.bird.pointnb}\n'
            init.values+=f'bird.vitesse (m/s): {round(init.bird.vitesse,2)}\n'
            init.values+=init.valuesTraj
            verif.config(text=init.values)
            win.update_idletasks()
            win.update()
            init.clock.tick(60)

# Run following code when the program starts

# Declare objects of MyThread class
threadedWindow = infoWindow()

# Start running the threads!
threadedWindow.start()
# Wait for the threads to finish...
#myThreadOb1.join()
