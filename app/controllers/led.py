from rpi_ws281x import PixelStrip, Color
import argparse

class led():
    def __init__(self, led_count : int, led_pin : int, led_freq_hz : int, led_dma : int, led_brightness : int, led_invert : bool, led_channel : int):
        self.LED_COUNT = led_count           # Número de LEDs da fita
        self.LED_PIN = led_pin               # Pino GPIO onde o a fita está conectada (PWM e SPI)
        self.LED_FREQ_HZ = led_freq_hz       # Frequência de sinal do LED em hertz (Normalmente 800khz)
        self.LED_DMA = led_dma               # Canal DMA usado para geração do sinal (Sei lá tenta o 10)
        self.LED_BRIGHTNESS = led_brightness # Quanto mais próximo do 0 mais escuro e mais claro é proximo do 255
        self.LED_INVERT = led_invert         # True para inverter o sinal (Apenas quando usar um NPN transistor level shift)
        self.LED_CHANNEL = led_channel       # Altere para 1 para as GPIOs (13, 19, 41, 45 ou 53)
        
        self.strip = PixelStrip(self.LED_COUNT, self.LED_PIN, self.LED_FREQ_HZ, self.LED_DMA, self.LED_INVERT, self.LED_BRIGHTNESS, self.LED_CHANNEL)
        # Inicializa a biblioteca
        self.strip.begin()

        def oneCollor(color : Color) -> None:
            for x in range(0, self.LED_COUNT):
                self.setPixelColor(x, color)
            
            self.strip.show()
        
        def coresClima(self,json,chaveJson):
            return

        

if __name__ == '__main__':
    fitaLed = led(60, 18, 8000, 10, 255, False, 0)
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

   

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            print('Ligando em uma cor')
            fitaLed.oneCollor(Color(0, 255, 0))

    except KeyboardInterrupt:
        if args.clear:
            fitaLed.oneCollor(Color(0, 0, 0))
