import hashlib

pass_hash = input("Enter MD% hash : ")

wordlist = input("File Name : ")

try:
     pass_file = open (wordlist, "r")
  except:
       print("File not found")
       quit()

for word in pass_file:

   enc_wrd = word.encode('utf-8')
   digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    if digest == pass_hash :
        print("password is found")
        print("password is " + word)
        flag = 1
        break

     if flag == 0:
  print("assword is not found the list")
