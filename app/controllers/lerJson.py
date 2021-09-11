import json
import os

class lerJson():
    def __init__(self,nomeArqu):
        self.nomeArqu = nomeArqu

    def lerJson(self):
        with open(self.nomeArqu,'r') as jsonTempo:
            return json.load(jsonTempo)
