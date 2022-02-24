#Conversione binario in decimale senza l'utilizzo di librerie precaricate

num_bin = int(input("Inserisci un numero binario: "))
num_dec = 0
esponenz = 1
lunghezza = len(str(num_bin))

for k in range(lunghezza):
    convers = num_bin % 10
    num_dec = num_dec + (convers * esponenz)
    esponenz = esponenz * 2
    num_bin = int(num_bin/10)

print("Il tuo numero in decimale è: ", num_dec)


#Input ottetti binario

ott1 = "11111111"
ott2 = "11111111"
ott3 = "11111111"
ott4 = "0"

#Funzione di conversione binario a decimale

def bintodec (ottetto):
    lunghezza = len(str(ottetto))
    num_dec = 0
    esponenz = 1

    for k in range(lunghezza):
        convers = ottetto % 10
        num_dec = num_dec + (convers * esponenz)
        esponenz = esponenz * 2
        ottetto = int(ottetto/10)
    return num_dec


ip = [bintodec (int(ott1)), bintodec (int(ott2)), bintodec (int(ott3)), bintodec (int(ott4))]

print("Il tuo numero in decimale è: ", ip)
