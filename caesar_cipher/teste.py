from collections import Counter

# Frequências esperadas (tabela fornecida)
frequencia_esperada = {
    'a': 14.63,
    'e': 12.57,
    'o': 10.73,
    's': 7.81,
    'r': 6.53,
    'i': 6.18,
    'n': 5.05,
    'd': 4.99,
    'm': 4.74,
    'u': 4.63,
    't': 4.34,
    'c': 3.88,
    'l': 2.78,
    'p': 2.52,
    'v': 1.67,
    'g': 1.30,
    'h': 1.28,
    'q': 1.20,
    'b': 1.04,
    'f': 1.02,
    'z': 0.47,
    'j': 0.40,
    'x': 0.21,
    'k': 0.02,
    'w': 0.01,
    'y': 0.01
}

def analisar_frequencia(mensagem):
    # Converte a mensagem para maiúsculas (você pode usar .lower() para minúsculas)
    mensagem = mensagem.upper()

    # Remove acentos e caracteres especiais (como ç, á, etc.)
    mensagem = ''.join(
        c for c in mensagem
        if c.isalpha()
    )

    # Calculando a frequência das letras no texto
    frequencias = Counter(mensagem)
    total = sum(frequencias.values())

     # Exibindo a tabela de diferenças
    print(f"{'Caractere Criptografado':^20} | {'Caractere Esperado':^20} | {'Diferença Absoluta (%)':^30}")
    print("-" * 80)

    for char_cripto, freq_cripto in frequencias.most_common():
        porcentagem_cripto = (freq_cripto / total) * 100
        for char_esperado, freq_esperado in frequencia_esperada.items():
            # Calcula a diferença absoluta entre a frequencia observada e esperada
            diferenca_absoluta = abs(porcentagem_cripto - freq_esperado)
            print(f"{repr(char_cripto):^20} | {repr(char_esperado):^20} | {diferenca_absoluta:>9.2f}")

# Exemplo de uso
mensagem_criptografada = "Evsbouf pt vmujnpt bopt, p dbnqp eb dsjquphsbgjb ufn bwbodbep dpotjefsbwfmnfouf, dpn b dpotubouf cvtdb qps nfupept nbjt fgjdjfouft f tfhvspt qbsb qspufhfs bt jogpsnbdpft. P vtp ef bmhpsjunpt tpgjtujdbept, dpnp b djgsb ef dftbs, f fttfodjbm qbsb hbsboujs b dpogjefodjbmjebef ept ebept fn vnb fsb dbeb wfa nbjt ejhjubmjabeb. B bqmjdbdbp efttft bmhpsjunpt fowpmwf p vtp ef dibwft tfdsfubt, rvf tbp fttfodjbjt qbsb dsjquphsbgbs f eftdsjquphsbgbs bt nfotbhfot, hbsboujoep rvf bqfobt pt vtvbsjpt bvupsjabept ufoibn bdfttp bp dpoufvep. Bmfn ejttp, b dsjqupbobmjtf eftfnqfoib vn qbqfm dsvdjbm ob nfmipsjb efttft tjtufnbt, qfsnjujoep rvf pt ftqfdjbmjtubt uftufn b tpmjefa ept bmhpsjunpt f jefoujgjrvfn qpoupt gsbdpt rvf qpefn tfs fyqmpsbept qps bubdbouft. P ftuvep ebt gsfrvfodjbt ef dbsbdufsft, qps fyfnqmp, f vnb ufdojdb vujmjabeb qbsb rvfcsbs dpejhpt ef djgsbhfn tjnqmft, dpnp b djgsb ef dftbs, bp bobmjtbs b bqbsjdbp ebt mfusbt op ufyup dsjquphsbgbep f dpnqbsboep-bt dpn bt gsfrvfodjbt ftqfsbebt qbsb vnb mjohvb obuvsbm. Fttf qspdfttp fyjhf vnb dpnqsffotbp qspgvoeb ebt qspqsjfebeft eb mjohvb f ebt ufdojdbt ef dsjquphsbgjb, bmfn ef vnb ibcjmjebef ftqfdjbm qbsb jefoujgjdbs qbespft rvf qpttbn joejdbs b dibwf vujmjabeb. B dsjquphsbgjb ufn tjep bnqmbnfouf bqmjdbeb fn bsfbt dpnp dpnfsdjp fmfuspojdp, qspufdbp ef ebept qfttpbjt f dpnvojdbdpft tjhjmptbt, f tfv vtp dpoujovb b dsftdfs dpn p bvnfoup ebt bnfbdbt ejhjubjt. Jttp upsob b dsjqupbobmjtf vnb gfssbnfoub fttfodjbm qbsb b tfhvsbodb djcfsofujdb, bkveboep b efufdubs wvmofsbcjmjebeft f b eftfowpmwfs tjtufnbt ef qspufdbp nbjt spcvtupt. B nfejeb rvf opwbt ufdopmphjbt f ufdojdbt ef bubrvf tbp eftfowpmwjebt, pt qspgjttjpobjt ef tfhvsbodb qsfdjtbn ftubs tfnqsf vn qbttp b gsfouf, bqsjnpsboep tfvt dpoifdjnfoupt fn dsjquphsbgjb f dsjqupbobmjtf qbsb hbsboujs b qspufdbp ebt jogpsnbdpft tfotjwfjt. B ufoefodjb f rvf, op gvuvsp, bt ufdojdbt ef dsjquphsbgjb tf upsofn dbeb wfa nbjt tpgjtujdbebt, p rvf fyjhjsb vn ftgpsdp dpotubouf qbsb bdpnqboibs pt bwbodpt eb bsfb."
analisar_frequencia(mensagem_criptografada)
