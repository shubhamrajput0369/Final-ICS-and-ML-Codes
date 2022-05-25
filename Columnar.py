
import math

def encryptmsg(msg,key):
  cipher=''
  msg=msg.upper()
  msg=msg.replace(' ','X')
  msg_len=float(len(msg))
  msg_lst=list(msg)

  #cal no. of cols
  col=len(key)

  #no of rows
  row=int(math.ceil(msg_len/col))

  #add X in extra space
  fill_null=int((row*col)-msg_len)
  msg_lst.extend('X'*fill_null)

  #add to the matrix
  m=0
  matrix=[]
  for i in range(row):
    temp=[]
    for j in range(col):
      temp.append(msg_lst[m])
      m+=1
    matrix.append(temp)

  #to read the matrix
  k=0
  map={}
  for i in range(col):
    temp=[]
    for j in range(row):
      temp.append(matrix[j][i])
    if key[k] in map:
      map[key[k]]+= temp
    else:
      map[key[k]] = temp
    k+=1

  for key in sorted(map.keys()):
    cipher+= ''.join(map[key])
  
  return cipher


def decryptmsg(cipher, key):
  msg=''
  msg_indx=0
  k_indx=0
  msg_len=float(len(cipher))
  msg_lst=list(cipher)

  col=len(key)

  row=int(math.ceil(msg_len/col))

  key_lst=sorted(list(key))

  dec_cipher=[[None for i in range(col)] for j in range(row)]

  for _ in range(col):
    curr_indx=key.index(key_lst[k_indx])
    

    for j in range(row):
      dec_cipher[j][curr_indx] = msg_lst[msg_indx]
      msg_indx +=1
    k_indx+=1
  print(dec_cipher)

  try:
    msg= ''.join(sum(dec_cipher, []))
  except TypeError:
    raise TypeError("This Program cannot handle repeating words")

  return msg


msg="Geeks for Geeks"
key="HACK"
cipher=encryptmsg(msg,key)
print("Cipher Text is: ", cipher)
decrypt=decryptmsg(cipher,key)
print("Decrypted msg is: ", decrypt)


