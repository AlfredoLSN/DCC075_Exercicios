def encrypt(text, s):
    alphaUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphaLower = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char in alphaUpper:
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char in alphaLower:
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(key, message):
    #message = message.upper()
    alphaUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphaLower = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for letter in message:
        if letter in alphaUpper:
            letter_index = (alphaUpper.find(letter) - key) % len(alphaUpper)
            result += alphaUpper[letter_index]
        elif letter in alphaLower:
            letter_index = (alphaLower.find(letter) - key) % len(alphaLower)
            result += alphaLower[letter_index]
        else:
            result += letter
    return result

text = "Durante os ultimos anos, o campo da criptografia tem avancado consideravelmente, com a constante busca por metodos mais eficientes e seguros para proteger as informacoes. O uso de algoritmos sofisticados, como a cifra de cesar, e essencial para garantir a confidencialidade dos dados em uma era cada vez mais digitalizada. A aplicacao desses algoritmos envolve o uso de chaves secretas, que sao essenciais para criptografar e descriptografar as mensagens, garantindo que apenas os usuarios autorizados tenham acesso ao conteudo. Alem disso, a criptoanalise desempenha um papel crucial na melhoria desses sistemas, permitindo que os especialistas testem a solidez dos algoritmos e identifiquem pontos fracos que podem ser explorados por atacantes. O estudo das frequencias de caracteres, por exemplo, e uma tecnica utilizada para quebrar codigos de cifragem simples, como a cifra de cesar, ao analisar a aparicao das letras no texto criptografado e comparando-as com as frequencias esperadas para uma lingua natural. Esse processo exige uma compreensao profunda das propriedades da lingua e das tecnicas de criptografia, alem de uma habilidade especial para identificar padroes que possam indicar a chave utilizada. A criptografia tem sido amplamente aplicada em areas como comercio eletronico, protecao de dados pessoais e comunicacoes sigilosas, e seu uso continua a crescer com o aumento das ameacas digitais. Isso torna a criptoanalise uma ferramenta essencial para a seguranca cibernetica, ajudando a detectar vulnerabilidades e a desenvolver sistemas de protecao mais robustos. A medida que novas tecnologias e tecnicas de ataque sao desenvolvidas, os profissionais de seguranca precisam estar sempre um passo a frente, aprimorando seus conhecimentos em criptografia e criptoanalise para garantir a protecao das informacoes sensiveis. A tendencia e que, no futuro, as tecnicas de criptografia se tornem cada vez mais sofisticadas, o que exigira um esforco constante para acompanhar os avancos da area."
s = 17
textEncrypt = encrypt(text, s)
textDecrypt = decrypt(s, textEncrypt)
print("Texto encrypado: " + textEncrypt)
#print("Texto decryptado: \n" + textDecrypt)
