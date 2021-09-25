import spidev
import ws2812

SPI = spidev.SpiDev()
SPI.open(0,0)

QTD_LEDS = 5

CORES = []

def setColor(r, g, b):
    return [ g, r, b ]

def desligarFita():
    return [ setColor( 0,0,0 ) ] * QTD_LEDS

def setFitaAllColor(r, g, b):
    return [ setColor(r,g,b) ] * QTD_LEDS


ws2812.write2812( SPI, desligarFita() )

