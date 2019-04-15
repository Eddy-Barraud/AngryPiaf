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
        root.geometry('+30+155')
        win = tkinter.Frame(root)
        win.pack()
        txt = 'b : respawn bird only\n'
        txt += 'SPACE : reload game\n'
        txt += 'ESCAPE : quit'
        praticalInfos = tkinter.Label(win,text=txt)
        praticalInfos.config(font=("Arial", 12),justify=tkinter.LEFT)
        praticalInfos.pack()
        verif=tkinter.Label(win, text='',font=("Arial", 12),justify=tkinter.LEFT,width=20)
        verif.pack(anchor='nw')        
        
        while init.running:
            init.values=f'fps: {round(init.clock.get_fps(),2)}\nverif: {init.verif} \ninMove: {init.inMove} \ncoord: {init.coord}\n'
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
