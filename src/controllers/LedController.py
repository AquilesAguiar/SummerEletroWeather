import spidev
import ws2812

SPI = spidev.SpiDev()
SPI.open(0,0)

QTD_LEDS = 5

CORES = []

def setColor(r, g, b):
    return [ g, r, b ]

def setFitaAllColor(r, g, b):
    return [ setColor(r,g,b) ] * QTD_LEDS

def efeitoLed(corDia):
    cont = 0
    while True:
        if cont >1:
            cont = 0
        sep = corDia[cont].split(',')
        executarFita(setFitaAllColor(int(sep[0]), int(sep[1]), int(sep[2])))
        cont += 1


def executarFita(comando):
    ws2812.write2812( SPI, comando)

