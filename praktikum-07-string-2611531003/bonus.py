# Name: Jihan Iftinan Syadza Astwen
# NIM: 2611531003
# Question Bonus

text = input('Kalimat: ')
clean = text.replace(' ', '').lower()

if clean == clean[::-1]:
    print('Palindrome')
else:
    print('Not a palindrome')