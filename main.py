import time
from classes import *

wait = 20

arquivo = File('cnpjs.txt')
resultadofinal = {}
for i in arquivo.learquivo():
    cnpjresultado = Cnpj(i)
    cnpjresultado = cnpjresultado.consultacnpj()
    cnpjlimpo = limpanumero(i)
    resultadofinal[cnpjlimpo] = cnpjresultado

    print('Consultando Cnpj:', cnpjlimpo)
    print('Aguardando por %s segundos' %(wait))
    time.sleep(wait)

#print(resultadofinal)
arquivoresultado = File('resultado.json')
arquivoresultado.gravaarquivo(resultadofinal)





