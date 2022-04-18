#!/usr/bin/env python3

from ev3dev2.motor import MediumMotor,OUTPUT_A


motor = MediumMotor("out4")
motor.run_forever()