

def gcd(x,y):
  if x < y:
    small=x
    large=y
  else:
    small=y
    large=x
  
  while small!=0:
    temp=large%small
    large=small
    small=temp
  return large

def find_e(z):
  e=2
  while e < z:
    if(gcd(e,z)==1):
      print(e)
      return e
    e+=1

def find_d(z,e):
  d=2
  while d < z:
    if((d*e)%z==1):
      print(d)
      return d
    d+=1

def rsa_algo(p,q,text):
  n=p*q
  z=(p-1)*(q-1)
  e=find_e(z)
  d=find_d(z,e)
  print("Private Key is: " , e, n)
  print("Public Key is: " , d, n)


#Now encryption and decryption

#->Encyrption
#->CipherText: C= (P^e)mod n
#Now as the plaintext we took in input is string we need to convert itinto ascii
#->we convert it into ascii using ord function
  cipher_text=''
  for ch in text:
    ch=ord(ch)
    #now we need the output in string so again chr and compute
    cipher_text+= chr((ch ** e) % n)

#-> Decryption
#-> Plain Text: P=(C^d)%n   C means cipher text
#same process
  plain_text=''
  for ch in cipher_text:
    ch=ord(ch)
    plain_text+= chr((ch ** d) % n)
  
  return cipher_text,plain_text

p=int(input())
q=int(input())
text=input()
rsa_algo(p,q,text)



