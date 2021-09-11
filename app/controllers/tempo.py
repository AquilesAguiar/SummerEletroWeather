import requests, os, platform
from controllers.lerJson import lerJson


class Tempo():
    def __init__(self):

        if platform.system().lower() == "windows":
            jsonKeys = lerJson( os.getcwd() + '\\static\\json\\keys.json' )
        else:
            jsonKeys = lerJson( os.getcwd() + '\static\json\keys.json' )
        jsonKeys = jsonKeys.lerJson()
        keys = jsonKeys['keys']
        for key in keys:
            self.url = 'https://api.hgbrasil.com/weather?key='+key+'&user_ip=remote'
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
