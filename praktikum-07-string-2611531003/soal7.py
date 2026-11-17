# Name: Jihan Iftinan Syadza Astwen
# NIM: 2611531003
# Question 7

name = 'jihan iftinan syadza astwen'
nim = '2611531003'

clean = name.strip()
space = clean.find(' ')
first_name = clean if space == -1 else clean[:space]
username = first_name.lower() + nim[-3:]

print('=' * 30)
print(f'{'STUDENT CARD':^30}')
print('=' * 30)
print(f'{'Name':<10}: {name.title()}')
print(f'{'NIM':<10}: {nim}')
print(f'{'Username':<10}: {username}')
print(f'{'Intake':<10}: 20{nim[:2]}')
print('=' * 30)