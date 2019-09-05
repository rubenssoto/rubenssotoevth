import json
import requests
import re

def limpanumero(cnpjnumber):
    return re.sub('\W+', '', cnpjnumber)

class File():

    def __init__(self, filename):
        self.filename = filename

    def learquivo(self):
        with open(self.filename, 'r') as files:
            lines = files.readlines()
            return lines

    def gravaarquivo(self, conteudo):
        with open(self.filename, 'w') as writefile:
            json.dump(conteudo, writefile)

class Cnpj():

    def __init__(self, cnpjnumber):
        self.cnpjnumber = cnpjnumber

    def consultacnpj(self):
        receitaurl = 'https://www.receitaws.com.br/v1/cnpj/'
        result = requests.get(receitaurl + limpanumero(self.cnpjnumber)).json()
        cnpjcode = result['atividade_principal'][0]['code']
        return limpanumero(cnpjcode)
