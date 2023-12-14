def weight_conversion():
    weight = int(input("masukan berat: "))
    types = input("Kg atau Lbs: ")

    if (types == "Kg"):
        Kg = weight * 0.453592
        print(Kg)
    elif (types == "Lbs"):
        Lbs = weight * 2.20462262185
        print(Lbs)