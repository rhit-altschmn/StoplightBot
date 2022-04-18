#generic motor test

from ev3dev2.auto import *
from ev3dev2.motor import MediumMotor,OUTPUT_A

m = MediumMotor(OUTPUT_A)

m.run_timed(time_sp=3000, speed_sp=500)



