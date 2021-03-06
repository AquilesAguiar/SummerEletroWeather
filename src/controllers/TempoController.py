import requests
from controllers.JsonController import JsonReader, getSettingsPath,getDatabasePath

class TempoController():
    def __init__(self):
        settingsJson = JsonReader( getSettingsPath() )
        settingsKeys = settingsJson['API_KEYS']
        database = JsonReader( getDatabasePath() )
        cityName = database["localizacao"]
        for key in settingsKeys:
            self.url = 'https://api.hgbrasil.com/weather?key='+key+'&city_name='+cityName
            self.req = requests.get(self.url)
            if self.req.status_code == 200:
                self.req = self.req.json()
                break

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

    def getProxTempoImg(self,condicoes):
        diasImg = []
        dias = self.getProxTempo()
        for cond in condicoes:
            for dia in dias:
                if condicoes[cond] == dia['description']:
                    img = 'http://assets.api.hgbrasil.com/weather/images/{0}.png'.format(cond)
                    diasImg.append({
                            'date': dia['date'],
                            'weekday': dia['weekday'],
                            'max': dia['max'],
                            'min': dia['min'],
                            'description': dia['description'],
                            'condition': dia['condition'],
                            'img':img
                        }
                    )
        return diasImg
