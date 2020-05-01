# -*- coding: utf-8 -*-
"""
Aceleradev Python Codenation

Criptografia de Júlio César

@author: Ubiratan da Silva Tavares

# https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=SEU_TOKEN
# Token: 0d98ee1d5f3c5577f9538b5b8b2d29b998b958a1

"""

import requests
import json
from hashlib import sha1

# fazer requisicao HTTP
def fazerRequisicaoHTTP(url):
    response = requests.get(url)
    return response.json()

# salvar dados_json em nome_arquivo
def salvarArquivoJSON(nome_arquivo, dados_json):
    try:
        arq = open(nome_arquivo, 'w')
        dados_json_str = json.dumps(dados_json)
        arq.write(dados_json_str)
        arq.close()
    except Exception as erro:
        print('Erro:', erro)

# ler dados_json em nome_arquivo
def abrirArquivoJSON(nome_arquivo):
    try:
        arq = open(nome_arquivo, 'r')
        dados_json = json.load(arq)
        arq.close()
        return dados_json
    except Exception as erro:
        print('Erro:', erro) 

# lista completa do alfabeto    
def alfabeto():
    lista = []
    for i in range(97, 123):
        lista.append(chr(i))
    return lista
        
# decifrar mensagem
def decifrarMensagem(msg_cifrada, numero_casas):
    msg_decifrada = ''
    lista = alfabeto()     
    for c in msg_cifrada:
        estaNaLista = c in lista    
        if estaNaLista:
            pos = lista.index(c)            
            msg_decifrada += lista[pos - numero_casas]
        else:
            msg_decifrada += c    
    return msg_decifrada.lower()

# gerar resumo criptografico de mensagem
def gerarResumoCriptografico(msg):
    return sha1(msg.encode()).hexdigest()

# submete o arquivo via post
def submeterRespostaHTTP(url, files):
    r = requests.post(url, files = files)
    print(r.text)

# funcao principal
def main():
    # define a url de entrada
    url_input = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=0d98ee1d5f3c5577f9538b5b8b2d29b998b958a1'
    dados_json = fazerRequisicaoHTTP(url_input)
   
    # salva dados_json no arquivo answer.json
    salvarArquivoJSON('answer.json', dados_json)
    
    # le o conteudo do arquivo answer.json
    dados_json = abrirArquivoJSON('answer.json')
    print(dados_json)    

    # atualizar a chave 'decifrado' em dados_json   
    dados_json['decifrado'] = decifrarMensagem(dados_json['cifrado'], dados_json['numero_casas'])
    
    # atualizar a chave 'resumo_criptografico' em dados_json
    dados_json['resumo_criptografico'] = gerarResumoCriptografico(dados_json['decifrado'])
    
    # salva dados_json no arquivo answer.json
    salvarArquivoJSON('answer.json', dados_json)
    
    # le o conteudo do arquivo answer.json
    dados_json = abrirArquivoJSON('answer.json')
    print(dados_json)
    
    print(len(dados_json['resumo_criptografico']))
    
    # submete o arquivo answer.json atualizado via post
    
    # define a url de saida
    url_output = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=0d98ee1d5f3c5577f9538b5b8b2d29b998b958a1'
    files = {'answer': ('answer.json', open('answer.json', 'rb'))}
    
    submeterRespostaHTTP(url_output, files)
    
if __name__ =='__main__':
    main()   
    