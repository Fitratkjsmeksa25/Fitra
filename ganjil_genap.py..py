while True :
    angka = int(input("masukkan sebuah angka: "))

    if angka % 2 == 0:
        print("bilangan genap")
    else:
        print("bilangan ganjil")

    lagi = input("ingin memasukkan angka lagi? (ya/tidak) ")

    if lagi.lower() !="ya":
        print("program selesai")
        break
