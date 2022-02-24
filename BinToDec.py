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
