from Dados import *
import json

dados_json = json.dumps(clientes_dicionario, indent=4)
print(dados_json)

dados_json1 = json.loads(clientes_json)
print(dados_json1)

for chave, valor in dados_json1.items():
    print(chave)
    print(valor)

with open('clientes_json', 'w') as arquivo:
    json.dump(clientes_dicionario, arquivo, indent=4)
    dados = json.loads(arquivo)

for i, j in dados.items():
    print(i)
    print(j)