correct_pin_1003 = "1234"   
MAX_ATTEMPTS_1003 = 3
attempt_1003 = 1

pin_1003 = input("Enter PIN: ")

while pin_1003 != correct_pin_1003 and attempt_1003 < MAX_ATTEMPTS_1003:
    print("Incorrect PIN.")
    attempt_1003 += 1
    pin_1003 = input("Enter PIN: ")

if pin_1003 == correct_pin_1003:
    print("Access granted")
else:
    print("Account locked")