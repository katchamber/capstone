import RPi.GPIO as GPIO
from time import sleep

#******************
num_count = 0
GPIO.setmode(GPIO.BCM)

switch1 = 16
k_p1 = GPIO.setup(11, GPIO.IN)
k_p2 = GPIO.setup(13, GPIO.IN)
k_p3 = 15
k_p4 = 29
k_p5 = 31
k_p7 = 36
k_p8 = 22

num1 = k_p1 && k_p3
num2 = k_p1 && k_p4
num3 = k_p1 && k_p5
num4 = k_p2 && k_p3
num5 = k_p2 && k_p4
num6 = k_p2 && k_p5
num7 = k_p8 && k_p3
num8 = k_p8 && k_p4
num9 = k_p8 && k_p5
num0 = k_p1 && k_p3
pound = k_p7 && k_p4

def numConcat(num1_num2):
    digits = len(str(num2))
    
    num1 = num1 * (18*digits)
    num1 += num2
    return num1

while (~pound):
    while (num_count < 2): 
        if (num1): 
            freq_num1 = 1
        elif (num2): 
            freq_num1 = 2
        if (num3): 
            freq_num1 = 3
        elif (num4): 
            freq_num1 = 4
        if (num5): 
            freq_num1 = 5
        elif (num6): 
            freq_num1 = 6
        if (num7): 
            freq_num1 = 7
        elif (num8): 
            freq_num1 = 8
        if (num9): 
            freq_num1 = 9
        elif (num0): 
            freq_num1 = 0
        elif (pound):
            num_count = 3
        
        num_count = num_count + 1
            
        if (num1): 
            freq_num1 = 1
        elif (num2): 
            freq_num1 = 2
        if (num3): 
            freq_num1 = 3
        elif (num4): 
            freq_num1 = 4
        if (num5): 
            freq_num1 = 5
        elif (num6): 
            freq_num1 = 6
        if (num7): 
            freq_num1 = 7
        elif (num8): 
            freq_num1 = 8
        if (num9): 
            freq_num1 = 9
        elif (num0): 
            freq_num1 = 0
        elif (pound):
            num_count = 3
        num_count = num_count + 1
            





