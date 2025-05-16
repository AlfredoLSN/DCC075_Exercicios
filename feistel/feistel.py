import os
from struct import pack
from base64 import b64encode, b64decode



# Mostrar cada byte como bits (8 bits por caractere)
def retornaBits(bytes):
    bits = ' '.join(format(byte, '08b') for byte in bytes)
    return bits


def divideEmBlocos(mensagem, tamanho_bloco):
    blocos = []
    i = 0
    while i < len(mensagem):
        bloco = mensagem[i : i + tamanho_bloco]
        blocos.append(bloco)
        i += tamanho_bloco
    return blocos

def rotacionaBitsDireita(chave):
    valor = int.from_bytes(chave)
    ultimo_bit = valor & 1
    valor = (valor >> 1) | (ultimo_bit << 63)
    return valor.to_bytes(8)

def rotacionaBitsEsquerda(chave):
    valor = int.from_bytes(chave)
    primeiro_bit = (valor >> 63) & 1
    valor = ((valor << 1) & ((1 << 64) - 1)) | primeiro_bit 
    return valor.to_bytes(8)

def executaXOR(bytes1, bytes2):
     return bytes([a ^ b for a, b in zip(bytes1, bytes2)])

def funcaoF(bloco, key):
    return bytes([a ^ b for a, b in zip(bloco, key)])

def adicionaPadding(mensagem, tamanhoBloco):
    padding_length = tamanhoBloco - (len(mensagem) % tamanhoBloco)
    padding = [padding_length] * padding_length
    padding = pack('b'*padding_length, *padding)
    mensagemComPadding = mensagem + padding
    return mensagemComPadding

def dividirBlocoAoMeio(bloco, tamanhoBloco):
    blocoEsquerda = bloco[0 : (tamanhoBloco // 2)]
    blocoDireita = bloco[(tamanhoBloco // 2) : len(bloco)]
    return blocoEsquerda, blocoDireita



class FeistelHelper:
    def __init__(self):
        self.key = os.urandom(8)
        self.tamanho_bloco = 8
        self.rodadas = 16
    def encrypt(self, mensagem):
        mensagem = adicionaPadding(mensagem.encode("utf-8"), self.tamanho_bloco)
        blocos = divideEmBlocos(mensagem, self.tamanho_bloco)
        mensagem_criptografada = b""
        for bloco in blocos:
            bloco_esquerda, bloco_direita = dividirBlocoAoMeio(bloco, self.tamanho_bloco)
            bloco_criptografado = ""
            chave_atual = self.key
            print("BlocoEsquerda: ", bloco_esquerda)
            print("BlocoDireita: ", bloco_direita)
            for i in range(self.rodadas):
                print("Rodada ", i+1)
                print("BlocoE - Rodada " + str(i + 1) + ": " + str(bloco_esquerda))
                print("BlocoD - Rodada " + str(i + 1) + ": " + str(bloco_direita))
                resultado_funcaoF = funcaoF(bloco_direita, chave_atual)
                resultado_XOR = executaXOR(resultado_funcaoF, bloco_esquerda)
                if(i < 15):
                    bloco_esquerda = bloco_direita
                    bloco_direita = resultado_XOR
                chave_atual = rotacionaBitsDireita(chave_atual)
            bloco_criptografado = bloco_esquerda + bloco_direita
            print("MensagemFinal: ", bloco_criptografado)
        mensagem_criptografada += bloco_criptografado
        return b64encode(mensagem_criptografada).decode("utf-8")

                


def main():
    feistel = FeistelHelper()
    mensagemTeste = "alfredo"
    print(feistel.encrypt(mensagemTeste))

main()


        

        

