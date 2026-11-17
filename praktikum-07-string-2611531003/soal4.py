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

# b. 4 digit awal dan 3 digit akhir
phone = "082611531003"
hidden_count = len(phone) - 7
masked = phone[:4] + ('*' * hidden_count) + phone[-3:]
print(masked)