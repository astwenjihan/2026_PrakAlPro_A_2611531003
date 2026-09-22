bulan_1003 = int(input("Masukkan angka bulan (1-12): "))

match bulan_1003:
    case 1:
        print("Januari")
    case 2:
        print("Februari")
    case 3:
        print("Maret")
    case 4:
        print("April")
    case 5:
        print("Mei")
    case 6:
        print("Juni")
    case 7:
        print("Juli")
    case 8:
        print("Agustus")
    case 9:
        print("September")
    case 10:
        print("Oktober")
    case 11:
        print("November")
    case 12:
        print("Desember")
    case _:
        print("Angka tidak valid")
