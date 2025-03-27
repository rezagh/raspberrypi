from gpiozero import PWMLED
from signal import pause
red=PWMLED(17)
red.pulse() # make device fade in / out
#pause() # keeps the script running remove and try. no need for while loop we had before.


