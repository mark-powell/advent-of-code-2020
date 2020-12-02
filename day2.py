file = open('day2_input.txt', 'r')
lines = file.readlines()

valid_password_count = 0
valid_count_2 = 0
for line in lines:
    parts = line.split(' ')
    valid_counts = parts[0].split('-')
    valid_min = int(valid_counts[0])
    valid_max = int(valid_counts[1])
    letter_check = parts[1][0:1]
    password = parts[2]
    if password.count(letter_check) >= valid_min and password.count(letter_check) <= valid_max:
        valid_password_count+=1
    
    letter_one = password[valid_min-1:valid_min]
    letter_two = password[valid_max-1:valid_max]
    if (letter_one == letter_check and letter_two != letter_check) or (letter_two == letter_check and letter_one != letter_check):
        valid_count_2 += 1

print('Part 1:', valid_password_count)
print('Part 2:', valid_count_2)
