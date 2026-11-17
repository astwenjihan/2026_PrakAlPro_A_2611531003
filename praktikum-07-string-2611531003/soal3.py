# Name: Jihan Iftinan Syadza Astwen
# NIM: 2611531003
# Question 3

# soal3.py (A)
text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:11])

# soal3.py (B)
text = "Algoritma dan Pemrograman"
count = 0
for char in text:
    if char in "AIUEOaiueo":
        count = count + 1
print("Vowels:", count)

text = "Jihan Iftinan Syadza Astwen"
count = 0
for char in text:
    if char in "AIUEOaiueo":
        count = count + 1
print("Vowels:", count)