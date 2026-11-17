# Name: Jihan Iftinan Syadza Astwen
# NIM: 2611531003
# Question 5

# soal5.py (A)
username = input("Username: ")
 
# Check the rules in a safe order and print the first rule that fails.
# Messages:
#   "Invalid: at least 5 characters"
#   "Invalid: letters and digits only"
#   "Invalid: must start with a letter"
#   "Valid"

if len(username) < 5:
    print("Invalid: at least 5 characters")
elif not username.alnum():
    print("Invalid: letters and digits only")
elif not username[0]