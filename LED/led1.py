from gpiozero import LED
from time import sleep

#gpip 17 is on pin 11
#the other end of the circuit is to ground

red = LED(17)
while True:
    red.on()
    sleep(1)
    red.off()
    sleep(1)
