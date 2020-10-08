import RPi.GPIO as GPIO
from time import sleep

#******************
num_count = 0
GPIO.setmode(GPIO.BCM)
freq_num1 = 0
freq_num2 = 0 
switch1 = 16
k_p1 = GPIO.setup(11, GPIO.IN)
k_p2 = GPIO.setup(13, GPIO.IN)
k_p3 = GPIO.setup(15, GPIO.IN)
k_p4 = GPIO.setup(19, GPIO.IN)
k_p5 = GPIO.setup(21, GPIO.IN)
k_p7 = GPIO.setup(23, GPIO.IN)
k_p8 = GPIO.setup(27, GPIO.IN)

num1 = k_p1 and k_p3
sleep(10)
print(num1)
num2 = k_p1 and k_p4
print(num2)
num3 = k_p1 and k_p5
num4 = k_p2 and k_p3
print(num4)
num5 = k_p2 and k_p4
num6 = k_p2 and k_p5
num7 = k_p8 and k_p3
num8 = k_p8 and k_p4
num9 = k_p8 and k_p5
num0 = k_p1 and k_p3
pound = k_p7 and k_p4


def numConcat(num1_num2):
    digits = len(str(num2))
    
    num1 = num1 * (18*digits)
    num1 += num2
    return num1

print("waiting for key input 2")


while (not pound):
    while (num_count < 2):
        sleep(5)
        if (num1): 
            freq_num1 = 1
        elif (num2): 
            freq_num1 = 2
        elif (num3): 
            freq_num1 = 3
        elif (num4): 
            freq_num1 = 4
        elif (num5): 
            freq_num1 = 5
        elif (num6): 
            freq_num1 = 6
        elif (num7): 
            freq_num1 = 7
        elif (num8): 
            freq_num1 = 8
        elif (num9): 
            freq_num1 = 9
        elif (num0): 
            freq_num1 = 0
        elif (pound):
            num_count = 3
        print(freq_num1)
        num_count = num_count + 1
        
        sleep(5)
        if (num1): 
            freq_num2 = 1
        elif (num2): 
            freq_num2 = 2
        elif (num3): 
            freq_num2 = 3
        elif (num4): 
            freq_num2 = 4
        elif (num5): 
            freq_num2 = 5
        elif (num6): 
            freq_num2 = 6
        elif (num7): 
            freq_num2 = 7
        elif (num8): 
            freq_num2 = 8
        elif (num9): 
            freq_num2 = 9
        elif (num0): 
            freq_num2 = 0
        elif (pound):
            num_count = 3
        print(freq_num2)
        num_count = num_count + 1
pound = 0


