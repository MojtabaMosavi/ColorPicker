import tkinter as tk
from tkinter import *


class colorPicker(tk.Frame):
    ''' A simple color picker GUI, provides rgb and hexa representation
    of picked color '''
    
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        mainFrame = tk.Frame(master).grid(row = 0 ,column = 0, sticky = (N,S,W,E),
        columnspan = 6 , rowspan =5 )
        width, height = 450 ,300
        master.geometry(str(width) + 'x' + str(height))

        self.canvas = tk.Canvas(mainFrame,width = width * (1.9/3)  , height = height)
        self.canvas.create_rectangle(0,0,300,200, fill = '#ffffff')
        self.canvas.grid( row = 0 ,column =3, rowspan = 10,columnspan =3 ,
        sticky = (N,S,W,E))

        self.scaleOne = tk.IntVar()
        self.scaleTwo = tk.IntVar()
        self.scaleThree = tk.IntVar()

        self.scaleO = tk.Scale(mainFrame, from_ = 0 , to = 225 ,
        orient = tk.HORIZONTAL , variable = self.scaleOne )
        self.scaleO.grid(row = 1 , column =0,columnspan=3 ,sticky = (N,W,E,S))

        self.scaleT = tk.Scale(mainFrame, from_ = 0 , to = 225 ,
        orient = tk.HORIZONTAL , variable = self.scaleTwo)
        self.scaleT.grid(row = 3 , column =0 , columnspan = 3, sticky = (N,W,E,S) )

        self.scaleTh = tk.Scale(mainFrame, from_ = 0 , to = 225 ,
        orient = tk.HORIZONTAL , variable = self.scaleThree)
        self.scaleTh.grid(row = 5 , column =0, columnspan = 3 ,sticky=(N,W,E,S))

        #self.Button = tk.Button(mainFrame,text='change', command = self.changeColor)
        #self.Button.grid(row = 3 ,column = 0)

        label_blue = tk.Label(mainFrame,text='Blue value ').grid(row=0,column=0,
        columnspan = 3 ,sticky=(S))
        label_red = tk.Label(mainFrame,text='Red Value ').grid(row=2,column=0,
        sticky=(N,W,E,S), columnspan = 3)
        label_green = tk.Label(mainFrame,text='Green Value ').grid(row=4,column=0,
        sticky=(N,W,E,S) ,columnspan = 3 )

        colors = {'white':(255,255,255),'black':(0,0,0),'dark slate gray':(47,79,79)
        ,'yellow':(255,255,0),'gold':(255,215,0)}

        self.variable = tk.StringVar()
        self.variable.set('white')

        scrolbar = tk.OptionMenu(mainFrame,self.variable, *colors).grid(row = 5 ,column = 3 )

        hex_label = tk.Label(mainFrame,text='Hex').grid(row=3,column=3)
        rgb_label = tk.Label(mainFrame,text='RGB').grid(row=4,column=3)

        self.hexColor = StringVar()
        self.Rgb = StringVar()

        self.labelH = Entry(mainFrame , textvariable = self.hexColor).grid(row=3,column=4)

        self.labelRgb = Entry(mainFrame, textvariable = self.Rgb).grid(row=4,column=4)

        #self.master.resizable(False,False)

        # checking the value of variable associated with scales
        # to adjust the color accordingly
        self.scaleOne.trace('w',self.callback)
        self.scaleTwo.trace('w',self.callback)
        self.scaleThree.trace('w',self.callback)
        self.variable.trace('w',self.callbackBackground)

        # tracking the change of color to input hexa representation
        self.scaleOne.trace('w',self.callback_hexa)
        self.scaleTwo.trace('w',self.callback_hexa)
        self.scaleThree.trace('w',self.callback_hexa)

        # tracking the change of color to input rgb representation
        self.scaleOne.trace('w',self.callbackrgbValue)
        self.scaleTwo.trace('w',self.callbackrgbValue)
        self.scaleThree.trace('w',self.callbackrgbValue)

        # making the mainFame adjust accordingly to it's parent
        self.master.rowconfigure(0,weight=1)
        self.master.columnconfigure(0,weight=1)

        # dynamic resizability for all the childer of mainFrame
        for child in self.master.slaves():
            child.rowconfigure(0,weight=1)
            child.columnconfigure(0,weight=1)

    def callback(self,*arg):
        ''' CallBack function to cahange the color of canvas '''
        return self.canvas.create_rectangle(0,0,300,200, fill = self.changeColor())

    def callbackBackground(self,*arg):
        ''' Callback function for OptionMenu '''
        return self.canvas.create_rectangle(0,0,300,200, fill = self.variable.get())

    def callback_hexa(self,*arg):
        ''' Callback function to display a hexadecimal representation
        of current color of the scrren'''
        self.hexColor.set(self.changeColor())

    # scope of a variable should be minimized as much as possible
    # this is a clear mess !
    # not good programming habit
    def callbackrgbValue(self,*arg):
        ''' Creates a (Red,green,Blue) representation by accessing scale instance variables '''
        self.Rgb.set(str(self.scaleOne.get()) +','+str(self.scaleTwo.get())+
        ','+ str(self.scaleThree.get()))

    # colud this this method be improved
    # do you need three variables for concatination ?
    def changeColor(self):
        ''' method to calculate the right equivelant hexadecimal of the color '''
        rgb_b= hex(self.scaleO.get())
        rgb_r = hex(self.scaleT.get())
        rgb_g = hex(self.scaleTh.get())

        # unnecessarily defined !
        #blueValue = ''
        #redValue = ''
        #greenValue = ''
        rgbColor = '#'

        if self.scaleO.get() < 15:
            rgbColor += str(rgb_b[2:]) + '0'
        else:
            rgbColor += rgb_b[2:]

        if self.scaleT.get() < 15:
            rgbColor += str(rgb_r[2:]) + '0'
        else:
            rgbColor += rgb_r[2:]

        if self.scaleTh.get() < 15:
            rgbColor  += str(rgb_g[2:]) + '0'
        else:
            rgbColor += rgb_g[2:]

        return rgbColor


if __name__ == '__main__':
    root = tk.Tk()
    a = colorPicker(root)
    root.title('Color Picker')
    root.mainloop()
