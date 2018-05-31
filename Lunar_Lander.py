from gpiozero import Button, LED
from time import sleep

left_thruster=Button(12)
main_thruster=Button(13)
right_thruster=Button(19)
lose=LED(20)
win=LED(21)
right_light=LED(26)
middle_light=LED(22)
left_light=LED(27)

def liftoff ():
    if main_thruster.when_pressed:
        middle_light.on
        sleep(1)
        middle_light.off
        return (True)
    else:
        return(False)

def left ():
    if left_thruster.when_pressed:
        left_light.on
        sleep(1)
        left_light.off
        return (True)
    else:
        return(False)

def right ():
    if right_thruster.when_pressed:
        right_light.on
        sleep(1)
        right_light.off
        return (True)
    else:
        return(False)
def Lose ():
    lose.on
    sleep(3)
    lose.off

def Win ():
    win.on
    sleep(3)
    win.off
    
    


    
    
        
        
        
            
            
        
        
    
    


