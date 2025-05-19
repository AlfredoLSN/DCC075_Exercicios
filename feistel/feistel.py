import os
from struct import pack
from base64 import b64encode, b64decode


#Essa funcao recebe como parametro uma mensagem e o tamanho do bloco do algoritmo e rotarna uma lista com os blocos separados de acordo com o tamanho do bloco
def divideEmBlocos(mensagem, tamanho_bloco):
        blocos = []
        i = 0
        while i < len(mensagem):
            bloco = mensagem[i : i + tamanho_bloco]
            blocos.append(bloco)
            i += tamanho_bloco
        return blocos


#Essa funcao recebe a chave em Bytes e a qnt de rotação a direita que deve ser feita na chave.
def rotacionaBitsDireita(chave, qnt):
    #Bytes não funciona com a operacao >>, logo é necessaria passar para int
    valor = int.from_bytes(chave)
    for i in range(qnt):
        ultimo_bit = valor & 1
        valor = (valor >> 1) | (ultimo_bit << 63)
    return valor.to_bytes(8)

#Essa funcao recebe a chave em Bytes e a qnt de rotação a esquerda que deve ser feita na chave.
def rotacionaBitsEsquerda(chave, qnt):
    #Bytes não funciona com a operacao >>, logo é necessaria passar para int
    valor = int.from_bytes(chave)
    for i in range(qnt):
        primeiro_bit = (valor >> 63) & 1
        valor = ((valor << 1) & ((1 << 64) - 1)) | primeiro_bit 
    return valor.to_bytes(8)

#Essa funcao executa o XOR entre dois Bytes, é usado o zip para o funcionamento correto com o tipo Bytes
def executaXOR(bytes1, bytes2):
    return bytes([a ^ b for a, b in zip(bytes1, bytes2)])

#Essa funcao executa a função F do algoritmo entre um bloco e a chave, a minha função F é um simples XOR. É usado o zip para o funcionamento correto com o tipo Byte
def funcaoF(bloco, key):
    return bytes([a ^ b for a, b in zip(bloco, key)])


## Essa funcao adiciona um padding na minha mensagem, utilizei o padding PKCS7, ele sempre vai adicionar pelo menos 1 padding a minha mensagem, ou seja, se o tamanho do bloco é 8 bytes e minha mensagem possui 7 ele vai adionar um padding de tamanho 1 com o valor 1, se minha mensagem tivesse 6 bytes, ele ia adicionar um padding de tamanho 2 com o valor 2, ou seja, o padding sempre indica a quantidade de padding adicionado, pois assim na hora da descriptografia o algoritmo sabe o tamanho que ele deve retirar da mensagem.
# OBS: se a mensagem tiver 8 bytes, ele vai adicionar um padding de tamanho 8 com o valor 8.
def adicionaPadding(mensagem, tamanhoBloco):
    padding_length = tamanhoBloco - (len(mensagem) % tamanhoBloco)
    padding = bytes([padding_length] * padding_length)
    mensagemComPadding = mensagem + padding
    return mensagemComPadding


#Essa funcao recebe um bloco e o tamanho do bloco e retorna o lado esquerdo e direito desse bloco
def dividirBlocoAoMeio(bloco, tamanhoBloco):
    blocoEsquerda = bloco[0 : (tamanhoBloco // 2)]
    blocoDireita = bloco[(tamanhoBloco // 2) : len(bloco)]
    return blocoEsquerda, blocoDireita


#Classe com os metodos encrypt e decrypt do algoritmo
class FeistelHelper:
    def __init__(self):
        #Gera uma chave randomica de 8 bytes(64 bits)
        self.key = os.urandom(8)
        
        #Define o tamanho do bloco em 8 bytes(64 bits)
        self.tamanho_bloco = 8
        
        #Define o numero de rodadas em 16
        self.rodadas = 16
    
    #Esse metodo executa o algorimo de Feistel
    def encrypt(self, mensagem):
        mensagem = adicionaPadding(mensagem.encode("utf-8"), self.tamanho_bloco)
        blocos = divideEmBlocos(mensagem, self.tamanho_bloco)
        mensagem_criptografada = b""
        for bloco in blocos:
            bloco_esquerda, bloco_direita = dividirBlocoAoMeio(bloco, self.tamanho_bloco)
            chave_atual = self.key
            #print("BlocoEsquerda: ", bloco_esquerda)
            #print("BlocoDireita: ", bloco_direita)
            for i in range(self.rodadas - 1):
                #print("Rodada ", i+1)
                #print("BlocoE - Rodada " + str(i + 1) + ": " + str(bloco_esquerda))
                #print("BlocoD - Rodada " + str(i + 1) + ": " + str(bloco_direita))
                #print("chave: ", chave_atual)
                resultado_funcaoF = funcaoF(bloco_direita, chave_atual)
                #print("Item1 F: ", bloco_direita)
                #print("Item2 F: ", chave_atual)
                #print("Resultado F: ", resultado_funcaoF)
                resultado_XOR = executaXOR(resultado_funcaoF, bloco_esquerda)
                bloco_esquerda = bloco_direita
                bloco_direita = resultado_XOR
                chave_atual = rotacionaBitsDireita(chave_atual, 1)
            bloco_criptografado = bloco_esquerda + bloco_direita
            #print("Bloco_criptografado: ", bloco_criptografado)
            mensagem_criptografada += bloco_criptografado
        
        #Retorna a mensagem criptograda em base64
        return b64encode(mensagem_criptografada).decode("utf-8")
    
    #Esse metodo descriptografa a mensagem
    def decrypt(self, mensagem):
        #Aqui ele fazer o decode da mensagem em base64
        mensagem = b64decode(mensagem.encode("utf-8"))
        blocos = divideEmBlocos(mensagem, self.tamanho_bloco)
        #print("Blocos: ", blocos)
        mensagem_descriptografada = b""
        for bloco in blocos:
            bloco_esquerda, bloco_direita = dividirBlocoAoMeio(bloco, self.tamanho_bloco)
            chave_atual = self.key
            chave_atual = rotacionaBitsDireita(self.key, 14)
            for i in range(self.rodadas - 1):
                #print("Rodada ", i+1)
                #print("BlocoE - Rodada " + str(i + 1) + ": " + str(bloco_esquerda))
                #print("BlocoD - Rodada " + str(i + 1) + ": " + str(bloco_direita))
                #print("chave: ", chave_atual)
                resultado_funcaoF = funcaoF(bloco_esquerda, chave_atual)
                resultado_XOR = executaXOR(resultado_funcaoF, bloco_direita)
                bloco_direita = bloco_esquerda
                bloco_esquerda = resultado_XOR
                chave_atual = rotacionaBitsEsquerda(chave_atual, 1)
            bloco_descriptografado = bloco_esquerda + bloco_direita
            mensagem_descriptografada += bloco_descriptografado
        tamanho_padding = mensagem_descriptografada[-1]
        mensagem_descriptografada = mensagem_descriptografada[:-tamanho_padding]
        return mensagem_descriptografada.decode("utf-8")
                



feistel = FeistelHelper()
texto = "Mensagem teste"
texto_criptografado = feistel.encrypt(texto)
texto_decriptografado = feistel.decrypt(texto_criptografado)
print("Texto original: ", texto)
print("Texto criptografado: ", texto_criptografado)
print("Texto decriptografado: ", texto_decriptografado)



