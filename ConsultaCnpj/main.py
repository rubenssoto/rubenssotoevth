import time
from classes import *

wait = 20

apresentacao.entrada()
arquivo = File(input('Informe o caminho do arquivo que contém os cnpjs:'))
arquivoresultado = File(input('Informe onde deseja salvar os resultados:'))
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
arquivoresultado.gravaarquivo(resultadofinal)





