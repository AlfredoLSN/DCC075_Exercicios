message = 'Uzpw Spyctbfp'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
    message = message.upper()
    translated = ""
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            translated  = translated + LETTERS[num]
        else:
            translated = translated + symbol
    print("Key #" + str(key) + ": " + str(translated))