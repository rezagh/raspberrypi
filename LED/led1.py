from gpiozero import LED,PWMLED
from time import sleep
from signal import pause

#red = LED(14)
red=PWMLED(14)
#while True:
    #red.on()
    #sleep(1)
    #red.off()
    #sleep(1)

red.blink()
pause()

