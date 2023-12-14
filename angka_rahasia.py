
angka_rahasia = 9
G = 0
G_L = 3
while G < G_L:
    user = int(input("masukan tebak angka "))
    G +=1
    if user == angka_rahasia:
        print("anda berhasil ")
        break
    else: 
        print ("salah")
else:
    print("kesempatan habis")