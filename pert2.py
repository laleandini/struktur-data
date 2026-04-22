nama_benar = "andin"
nama = input("masukkan nama anda: ")
if nama == nama_benar:
    print("nama benar, lanjut ke program")
    angka = int(input("masukkan angka : "))
    for i in range(1, 11): print(f"{angka} x {i} = {angka * i}")
else:
    print("silahkan coba lagi")
