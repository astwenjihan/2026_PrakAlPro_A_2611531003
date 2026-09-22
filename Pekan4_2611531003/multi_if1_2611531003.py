umur_1003 = int(input("Input umur anda: "))
sim_1003 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0]

if umur_1003 >= 17 and sim_1003 == 'y':
    print("Anda sudah dewasa dan boleh bawa motor")

if umur_1003 >= 17 and sim_1003 != 'y':
    print("Anda sudah dewasa tapi tidak boleh bawa motor")

if umur_1003 < 17 and sim_1003 != 'y':
    print("Anda belum cukup umur untuk bawa motor")

if umur_1003 < 17 and sim_1003 == 'y':
    print("Anda belum cukup umur untuk punya SIM")