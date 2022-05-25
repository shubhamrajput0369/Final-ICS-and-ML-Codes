
import math

def getKeyMatrix(key):
  keyMatrix=[[0] * 3 for i in range(3)]
  k=0
  for i in range(3):
    for j in range(3):
      keyMatrix[i][j]=ord(key[k])%65
      k+=1
  return keyMatrix

def encrypt(messagevector,keyMatrix):
  col=len(messagevector[0])
  cipherMatrix=[[0 for i in range(col)]for j in range(3)]

  for i in range(3):
    for j in range(col):
      cipherMatrix[i][j]=0
      for x in range(3):
        cipherMatrix[i][j]+=(keyMatrix[i][x] * messagevector[x][j])
      cipherMatrix[i][j] = cipherMatrix[i][j] %26
  return cipherMatrix

def HillCipher(message, key):

  keyMatrix=getKeyMatrix(key)
  print(keyMatrix)

  msg_len=len(message)
  row=3
  col=math.ceil(msg_len/row)
  extra=(row*col)-msg_len
  message+="Z"*extra

  messagevector = [[0 for i in range(col)] for j in range(3)]

  msg_index=0
  for i in range(col):
    for j in range(3):
      messagevector[j][i]=ord(message[msg_index])%65
      msg_index+=1
  print(messagevector)

  cipherMatrix=encrypt(messagevector,keyMatrix)
  print(cipherMatrix)

  CipherText=[]
  for i in range(col):
    for j in range(3):
      CipherText.append(chr(cipherMatrix[j][i]+65))

  print("CipherText is: ", ''.join(CipherText))


if __name__ == "__main__":

  message= "ACTACTBO"
  key= "GYBNQKURP"

HillCipher(message,key)



