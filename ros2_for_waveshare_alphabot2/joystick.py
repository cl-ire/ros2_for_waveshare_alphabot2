#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import RPi.GPIO as GPIO

# Joystick
CTR = 7  # Center
A = 8    # Up
B = 9    # Right
C = 10   # Left
D = 11   # Down

class JoystickDriver(Node):
    def __init__(self, ctr=7, a=8, b=9, c=10, d=11):
        super().__init__('joystick_driver')
        self.get_logger().info("Node 'joystick' configuring driver")

        self.CTR = ctr
        self.A = a
        self.B = b
        self.C = c
        self.D = d

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.CTR, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(self.A, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(self.B, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(self.C, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(self.D, GPIO.IN, GPIO.PUD_UP)

        self.rate = self.create_rate(self.get_parameter_or('~rate', 10))

        # Setup publisher for joystick
        self.pub = self.create_publisher(String, '/joystick', 4)
        self.get_logger().info("Node 'joystick' configured.")

    def __del__(self):
        GPIO.cleanup()

    def run(self):
        self.get_logger().info("Node 'joystick' running.")
        
        imput_last = String(data="No Imput jet")
        imput = String(data="No Imput jet")
        while rclpy.ok():
            
            if GPIO.input(self.CTR) == GPIO.LOW:
                imput = String(data="Center")
            elif GPIO.input(self.A) == GPIO.LOW:
                imput = String(data="Up")                    
            elif GPIO.input(self.B) == GPIO.LOW:
                imput = String(data="Right")
            elif GPIO.input(self.C) == GPIO.LOW:
                imput = String(data="Left")
            elif GPIO.input(self.D) == GPIO.LOW:
                imput = String(data="Down")
            else:
                imput = String(data="No Imput")

            if imput != imput_last:
                if imput != String(data="No Imput"):
                    self.pub.publish(imput)
                    self.get_logger().info("Node 'joystick' {}".format(imput.data))
                imput_last = imput

def main():
    
    rclpy.init()
    node = JoystickDriver()
    try:
        node.run()
    finally:
        node.__del__()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
