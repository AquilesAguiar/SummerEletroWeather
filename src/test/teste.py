from pyA20.gpio import gpio
from pyA20.gpio import port

import time

PA_11 = led = 11

gpio.init()

gpio.setcfg( PA_11, gpio.OUTPUT )

response_gpio = gpio.output(led, 1)

print(response_gpio)

number = 0
text = "Deligando"

for i in range(20):
    print(text)
    gpio.output( PA_11, number )
    number = 1 if number == 0 else 0
    text = "Ligando o Led" if number == 0 else "Desligando o Led"
    time.sleep(2)
