from collections import Counter

def analisar_frequencia(mensagem):
    mensagem = mensagem.upper()

    mensagem_filtrada = ''.join(
        c for c in mensagem 
        if c.isalpha()
    )


    frequencias = Counter(mensagem_filtrada)
    total = sum(frequencias.values())

    print(f"{'Caractere':^10} | {'Frequência':^10} | {'Porcentagem':^12}")
    print("-" * 36)

    for char, freq in frequencias.most_common():
        porcentagem = (freq / total) * 100
        print(f"{repr(char):^10} | {freq:^10} | {porcentagem:>9.2f} %")

# Exemplo de uso
mensagem_criptografada = "Ulirekv fj lckzdfj refj, f trdgf ur tizgkfxirwzr kvd rmretruf tfejzuvirmvcdvekv, tfd r tfejkrekv sljtr gfi dvkfufj drzj vwztzvekvj v jvxlifj grir gifkvxvi rj zewfidrtfvj. F ljf uv rcxfizkdfj jfwzjkztrufj, tfdf r tzwir uv tvjri, v vjjvetzrc grir xrirekzi r tfewzuvetzrczuruv ufj urufj vd ldr vir trur mvq drzj uzxzkrczqrur. R rgcztrtrf uvjjvj rcxfizkdfj vemfcmv f ljf uv tyrmvj jvtivkrj, hlv jrf vjjvetzrzj grir tizgkfxirwri v uvjtizgkfxirwri rj dvejrxvej, xrirekzeuf hlv rgverj fj ljlrizfj rlkfizqrufj kveyrd rtvjjf rf tfekvluf. Rcvd uzjjf, r tizgkfrerczjv uvjvdgveyr ld grgvc tiltzrc er dvcyfizr uvjjvj jzjkvdrj, gvidzkzeuf hlv fj vjgvtzrczjkrj kvjkvd r jfczuvq ufj rcxfizkdfj v zuvekzwzhlvd gfekfj wirtfj hlv gfuvd jvi vogcfirufj gfi rkrtrekvj. F vjkluf urj wivhlvetzrj uv trirtkvivj, gfi vovdgcf, v ldr kvteztr lkzczqrur grir hlvsiri tfuzxfj uv tzwirxvd jzdgcvj, tfdf r tzwir uv tvjri, rf rerczjri r rgriztrf urj cvkirj ef kvokf tizgkfxirwruf v tfdgrireuf-rj tfd rj wivhlvetzrj vjgvirurj grir ldr czexlr erklirc. Vjjv giftvjjf vozxv ldr tfdgivvejrf gifwleur urj gifgizvuruvj ur czexlr v urj kvteztrj uv tizgkfxirwzr, rcvd uv ldr yrszczuruv vjgvtzrc grir zuvekzwztri gruifvj hlv gfjjrd zeuztri r tyrmv lkzczqrur. R tizgkfxirwzr kvd jzuf rdgcrdvekv rgcztrur vd rivrj tfdf tfdvitzf vcvkifeztf, gifkvtrf uv urufj gvjjfrzj v tfdleztrtfvj jzxzcfjrj, v jvl ljf tfekzelr r tivjtvi tfd f rldvekf urj rdvrtrj uzxzkrzj. Zjjf kfier r tizgkfrerczjv ldr wviirdvekr vjjvetzrc grir r jvxliretr tzsvievkztr, ralureuf r uvkvtkri mlcevirszczuruvj v r uvjvemfcmvi jzjkvdrj uv gifkvtrf drzj ifsljkfj. R dvuzur hlv efmrj kvtefcfxzrj v kvteztrj uv rkrhlv jrf uvjvemfcmzurj, fj gifwzjjzferzj uv jvxliretr givtzjrd vjkri jvdgiv ld grjjf r wivekv, rgizdfireuf jvlj tfeyvtzdvekfj vd tizgkfxirwzr v tizgkfrerczjv grir xrirekzi r gifkvtrf urj zewfidrtfvj jvejzmvzj. R kveuvetzr v hlv, ef wlklif, rj kvteztrj uv tizgkfxirwzr jv kfievd trur mvq drzj jfwzjkztrurj, f hlv vozxzir ld vjwfitf tfejkrekv grir rtfdgreyri fj rmretfj ur rivr."
analisar_frequencia(mensagem_criptografada)




""" 
Ao executar esse codigo python ele gera essa tabela de frequencia de caracteres:
Caractere  | Frequência | Porcentagem 
------------------------------------
   'R'     |    252     |     15.03 %
   'V'     |    195     |     11.63 %
   'J'     |    165     |      9.84 %
   'F'     |    148     |      8.83 %
   'Z'     |    125     |      7.45 %
   'I'     |    114     |      6.80 %
   'T'     |     99     |      5.90 %
   'U'     |     84     |      5.01 %
   'E'     |     81     |      4.83 %
   'K'     |     81     |      4.83 %
   'D'     |     65     |      3.88 %
   'G'     |     60     |      3.58 %
   'L'     |     53     |      3.16 %
   'C'     |     42     |      2.50 %
   'X'     |     29     |      1.73 %
   'W'     |     28     |      1.67 %
   'M'     |     16     |      0.95 %
   'H'     |     13     |      0.78 %
   'Y'     |     8      |      0.48 %
   'Q'     |     7      |      0.42 %
   'S'     |     6      |      0.36 %
   'O'     |     5      |      0.30 %
   'A'     |     1      |      0.06 %

   Ao analisar essa tabela vemos que a frequencia do caracter R é bem parecido com a frequencia do caracter A, conforme esse link: https://pt.wikipedia.org/wiki/Frequ%C3%AAncia_de_letras, logo podemos supor que o deslocamento usado é a distancia de A ate R, que no caso é 17, que foi exatamento o deslocamento usado para criptografar a mensagem no arquivo encrypt_decrypt.py
"""