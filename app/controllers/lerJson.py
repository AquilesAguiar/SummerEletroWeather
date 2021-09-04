import json
class lerJson():
    
    def __init__(self,nomeArqu):
        self.nomeArqu = nomeArqu
    
    def lerJson(self,position):
        with open(self.nomeArqu,'r') as jsonTempo:
            return json.load(jsonTempo)[position]
