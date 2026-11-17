# Name: Jihan Iftinan Syadza Astwen
# NIM: 2611531003
# Question 4

phone = "081234567890"
masked = phone[:4] + "*" * 4 + phone[-4:]
print(masked)

# a.
phone = "08123456789"
masked = phone[:4] + "*" * 4 + phone[-4:]
print(masked)

# b.
phone = "0812345678"
masked = phone[:4] + '*' * 4 + phone[-3:]
print(masked)