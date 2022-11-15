with open('input', 'r') as f:
    content = f.readlines()
flag = content[2].split(':')[1]

solution = ''
little_a = ord('a')
big_a = ord("A")
for letter in flag:
    if letter.isalpha():
        if letter.isupper():
            letter = (((ord(letter) - big_a)-13)%26)+big_a
            solution += chr(letter)
        else:
            letter = (((ord(letter) - little_a)-13)%26)+little_a
            solution += chr(letter)
    else:
        solution += letter

with open('input', 'a') as f:
    f.write(solution)