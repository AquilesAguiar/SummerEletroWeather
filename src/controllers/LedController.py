import spidev
import ws2812

SPI = spidev.SpiDev()
SPI.open(0,0)

QTD_LEDS = 5
CORES = []

def setColor(r, g, b) -> None:
    return [ g, r, b ]

def setFitaAllColor(r, g, b) -> None:
    return [ setColor(r,g,b) ] * QTD_LEDS

def setColorArray(arrayColor) -> None:
    executarFita( setFitaAllColor( arrayColor[0], arrayColor[1], arrayColor[2] ) )
    return None


def executarFita(comando) -> None:
    ws2812.write2812( SPI, comando )
    return None

