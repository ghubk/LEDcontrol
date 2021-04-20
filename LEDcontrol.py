from tkinter import *
import RPi.GPIO as GPIO
import time

window = Tk()
window.geometry("1000x600")
window.title("LED Control")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

def onblue():
    GPIO.output(13,True)

def onred():
    GPIO.output(15,True)

def offblue():
    GPIO.output(13,False)

def offred():
    GPIO.output(15,False)

B1 = Button(window, text ="RED ON", width= 20, bg="red", fg="black", command=onred)
B1.place(x=150,y=50)

B2 = Button(window, text="RED OFF", width= 20, bg="red", fg="black", command=offred)
B2.place(x= 350, y= 50)

B3 = Button(window, text="BLUE ON", width= 20, bg="blue", fg="black", command=onblue)
B3.place(x= 150, y= 20)

B4 = Button(window, text="BLUE OFF", width = 20, bg="blue", fg="black", command=offblue)
B4.place(x= 350, y= 20)

window.mainloop()