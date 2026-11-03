correct_pin = "1234"
pin = input("Enter PIN: ")

if pin == correct_pin:
    print("Access granted")

else:
    print("Incorrect PIN.")

MAX_ATTEMPTS = 3
attempt = 1

while pin != correct_pin and attempt < MAX_ATTEMPTS:
    pin = input("Enter PIN: ")
    attempt += 1
    print("Account locked")