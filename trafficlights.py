from gpiozero import Button, TrafficLights, Buzzer
from time import sleep

button = Button(21)
lights = TrafficLights(25, 16, 12)
buzzer = Buzzer(18)

while True:
    button.wait_for_press()
    lights.green.on()
    sleep(1)
    lights.green.off()
    sleep(1)
    lights.amber.on()
    sleep(1)
    lights.amber.off()
    sleep(1)
    lights.red.on()
    sleep(1)
    lights.amber.on()
    sleep(1)
    lights.off()
    lights.green.on()
    sleep(1)
    lights.off()
