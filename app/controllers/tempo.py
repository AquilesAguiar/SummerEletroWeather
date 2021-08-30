import requests
class Tempo():
    def __init__(self):
        self.url = 'https://api.hgbrasil.com/weather?key=00764386&user_ip=remote'
        self.req = requests.get(self.url).json()
    
    def getTempo(self):
        return self.req['results']

    def getFotoTempo(self):
        req = self.getTempo()
        cod_img = req['img_id']
        img = 'http://assets.api.hgbrasil.com/weather/images/{0}.png'.format(cod_img)
        return img
    
    def getProxTempo(self):
        req = self.getTempo()
        tempoProxDias = req["forecast"]
        return tempoProxDias