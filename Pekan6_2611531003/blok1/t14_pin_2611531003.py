correct_pin = "1234"   
MAX_ATTEMPTS = 3
attempt = 1

pin = input("Enter PIN: ")

while pin != correct_pin and attempt < MAX_ATTEMPTS:
    print("Incorrect PIN.")
    attempt += 1
    pin = input("Enter PIN: ")

if pin == correct_pin:
    print("Access granted")
else:
    print("Account locked")