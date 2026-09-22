umur_1003 = int(input("Input umur anda: "))
sim_1003 = input("Apakah Anda Sudah Punya SIM C: ")[0]

if umur_1003 >= 17 and sim_1003 == 'y':
    print("Anda sudah dewasa dan boleh bawa motor")
elif umur_1003 >= 17 and sim_1003 != 'y':
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")
elif umur_1003 < 17 and sim_1003 == 'y':
    print("Anda belum cukup umur untuk punya SIM")
else: 
    print("Anda belum cukup umur dan tidak boleh bawa motor")
print("Program Selesai")