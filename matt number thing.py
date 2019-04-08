from gpiozero import LED
from time import sleep

LED10=LED(6) #middle
LED5=LED(16) #dot
LED1=LED(21) #bottom left
LED2=LED(20) #bottom middle
LED4=LED(26) #bottom right
LED6=LED(19) #top right
LED7=LED(13) #top middle
LED9=LED(12) #top left

#7 seg#2

LED1B=LED(5)
LED2B=LED(1)
LED4B=LED(0)
LED5B=LED(7)
LED6B=LED(8)
LED7B=LED(11)
LED9B=LED(25)
LED10B=LED(9)

def alloffB():
    LED1B.off()
    LED2B.off()
    LED4B.off()
    LED5B.off()
    LED6B.off()
    LED7B.off()
    LED9B.off()
    LED10B.off()
    return

def alloff():
    LED1.off()
    LED2.off()
    LED4.off()
    LED5.off()
    LED6.off()
    LED7.off()
    LED9.off()
    LED10.off()
    return


def display1():
    LED4.on()
    LED6.on()
    return

def display2():
    LED7.on()
    LED6.on()
    LED10.on()
    LED1.on()
    LED2.on()
    return

def display3():
    LED7.on()
    LED6.on()
    LED10.on()
    LED4.on()
    LED2.on()
    return

def display4():
    LED9.on()
    LED10.on()
    LED4.on()
    LED6.on()
    return

def display5():
    LED7.on()
    LED9.on()
    LED10.on()
    LED4.on()
    LED2.on()
    return

def display6():
    LED7.on()
    LED9.on()
    LED1.on()
    LED2.on()
    LED4.on()
    LED10.on()
    return

def display7():
    LED7.on()
    LED6.on()
    LED4.on()
    return

def display8():
    LED7.on()
    LED6.on()
    LED4.on()
    LED2.on()
    LED1.on()
    LED9.on()
    LED10.on()
    return

def display9():
    LED9.on()
    LED10.on()
    LED7.on()
    LED6.on()
    LED4.on()
    return

def display0():
    LED7.on()
    LED9.on()
    LED6.on()
    LED1.on()
    LED2.on()
    LED4.on()
    return

def display1B():
    LED6B.on()
    LED4B.on()
    return

def display2B():
    LED7B.on()
    LED6B.on()
    LED10B.on()
    LED1B.on()
    LED2B.on()
    return

def display3B():
    LED7B.on()
    LED6B.on()
    LED10B.on()
    LED4B.on()
    LED2B.on()
    return

def display4B():
    LED9B.on()
    LED10B.on()
    LED6B.on()
    LED4B.on()
    return

def display5B():
    LED7B.on()
    LED9B.on()
    LED10B.on()
    LED4B.on()
    LED2B.on()
    return

def display6B():
    LED7B.on()
    LED9B.on()
    LED1B.on()
    LED2B.on()
    LED4B.on()
    LED10B.on()
    return

def display7B():
    LED7B.on()
    LED6B.on()
    LED4B.on()
    return

def display8B():
    LED7B.on()
    LED6B.on()
    LED4B.on()
    LED2B.on()
    LED1B.on()
    LED9B.on()
    LED10B.on()
    return

def display9B():
    LED7B.on()
    LED9B.on()
    LED10B.on()
    LED6B.on()
    LED4B.on()
    return

def display0B():
    LED7B.on()
    LED9B.on()
    LED6B.on()
    LED1B.on()
    LED2B.on()
    LED4B.on()
    return

    
###executable code here

alloff()
display1()
sleep(1)
alloff()
display2()
sleep(1)
alloff()
display3()
sleep(1)
alloff()
display4()
sleep(1)
alloff()
display5()
sleep(1)
alloff()
display6()
sleep(1)
alloff()
display7()
sleep(1)
alloff()
display8()
sleep(1)
alloff()
display9()
sleep(1)
alloff()
display0()
sleep(1)
alloff()
display1B()
sleep(1)
alloffB()
display2B()
sleep(1)
alloffB()
display3B()
sleep(1)
alloffB()
display4B()
sleep(1)
alloffB()
display5B()
sleep(1)
alloffB()
display6B()
sleep(1)
alloffB()
display7B()
sleep(1)
alloffB()
display8B()
sleep(1)
alloffB()
display9B()
sleep(1)
alloffB()
display0B()
sleep(1)
alloffB()

while True:
    x=input("what number?")
    alloff()
    alloffB()
    first=x[0]
    second=x[1]

    if first=="1":
        display1()
    elif first=="2":
        display2()
    elif first=="3":
        display3()
    elif first=="4":
        display4()
    elif first=="5":
        display5()
    elif first=="6":
        display6()
    elif first=="7":
        display7()
    elif first=="8":
        display8()
    elif first=="9":
        display9()
    elif first=="0":
        display0()
    if second=="1":
        display1B()
    elif second=="2":
        display2B()
    elif second=="3":
        display3B()
    elif second=="4":
        display4B()
    elif second=="5":
        display5B()
    elif second=="6":
        display6B()
    elif second=="7":
        display7B
    elif second=="8":
        display8B()
    elif second=="9":
        display9B()
    elif second=="0":
        display0B()
    
    
    
 
 
def A():
    LED1.on()
    LED4.on()
    LED10.on()
    LED9.on()
    LED6.on()
    LED7.on()
    return

def a():
    LED10.on()
    LED1.on()
    LED2.on()
    LED4.on()
    LED5.on()
    return

def B():
    LED1.on()
    LED2.on()
    LED4.on()
    LED5.on()
    LED6.on()
    LED7.on()
    LED9.on()
    LED10.on()
    return

def b():
    LED9.on()
    LED1.on()
    LED2.on()
    LED10.on()
    LED4.on()
    return

def c():
    LED10.on()
    LED1.on()
    LED2.on()
    return

def D():
    LED7.on()
    LED9.on()
    LED6.on()
    LED1.on()
    LED2.on()
    LED4.on()
    LED10.on()
    LED5.on()
    return




