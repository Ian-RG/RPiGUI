import RPi.GPIO as GPIO
from tkinter import *
import tkinter.font

blue = 2
red = 3
green = 4
blueState = False
redState = False
greenState = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(blue, GPIO.OUT)
GPIO.output(blue, GPIO.LOW)
GPIO.setup(red, GPIO.OUT)
GPIO.output(red, GPIO.LOW)
GPIO.setup(green, GPIO.OUT)
GPIO.output(green, GPIO.LOW)

window = Tk()
window.title("LED Toggler")
myFont = tkinter.font.Font(family = "Helvetica", size = 12, weight = "bold")

def toggleBlue():
    global blueState
    global blueButton
    GPIO.output(blue, GPIO.LOW if blueState else GPIO.HIGH)
    blueButton["text"] = blueButton["text"].rsplit(' ', 1)[0] + (" On" if blueState else " Off")
    blueState = not blueState

def toggleRed():
    global redState
    global redButton
    GPIO.output(red, GPIO.LOW if redState else GPIO.HIGH)
    redButton["text"] = redButton["text"].rsplit(' ', 1)[0] + (" On" if redState else " Off")
    redState = not redState
    
def toggleGreen():
    global greenState
    global greenButton
    GPIO.output(green, GPIO.LOW if greenState else GPIO.HIGH)
    greenButton["text"] = greenButton["text"].rsplit(' ', 1)[0] + (" On" if greenState else " Off")
    greenState = not greenState

def close():
    GPIO.cleanup()
    window.destroy()
    

blueButton = Button(window, text = "Blue Led On", font = myFont, command = toggleBlue, bg = "blue", height = 1, width = 24)
blueButton.grid(row = 0, column = 0)

redButton = Button(window, text = "Red Led On", font = myFont, command = toggleRed, bg = "red", height = 1, width = 24)
redButton.grid(row = 1, column = 0)

greenButton = Button(window, text = "Green Led On", font = myFont, command = toggleGreen, bg = "green", height = 1, width = 24)
greenButton.grid(row = 2, column = 0)

exitButton = Button(window, text = "Exit", font = myFont, command = close, bg = "yellow", height = 1, width = 12)
exitButton.grid(row = 3, column = 0)

window.protocol("WM_DELETE_WINDOW", close)

window.mainloop()

