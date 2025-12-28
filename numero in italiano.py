#last update approx. 15:43 28.12.2025.
#Italiano learning
numeros = ["zero",
           "uno",
           "due",
           "tre",
           "quattro",
           "cinque",
           "sei",
           "sette",
           "otto",
           "nove","dieci"]
numeros_11_20 = ["undici","dodici","tredici",
           "quattordici","quindici","sedici",
           "diciassette", "diciotto","diciannove","venti"]
numeros_30_100 = "trenta|quaranta|cinquanta|sessanta|settanta|ottanta|novanta|cento".split("|")

while True:
    count = 0
    numero = input("Il mio numero è: ")
    if numero == "":
        break
    for n in numero:
        if not n.isdigit() and count:
            print(" ")
            count = 0
        elif n >= "0" and n <= "9":
            count = 1
            print(n,":=",numeros[int(n)])
c = 0
for i in numeros:
    print(c,i)
    c += 1
for j in numeros_11_20[:-1]:
    print(c,j)
    c += 1
for x in ([numeros_11_20[-1]] + numeros_30_100):
    print(c,x)
    c += 1
    if x == "cento":
        break
    for y in numeros:
        if y == "zero" or y == "dieci":
            continue
        if y == "uno" or y == "otto":
            print(c,x[:-1]+y)
        else:
            print(c,x+y)
        c += 1
#learned from @italianpod101
#far from perfect but it works :)
