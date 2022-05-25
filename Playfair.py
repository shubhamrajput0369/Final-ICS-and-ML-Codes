
def create_matrix(key):
  letter_added=[]
  key=key.upper()
  matrix = [[0 for i in range(5)] for j in range(5)]
  for i in range(len(key)):
    if key[i] not in letter_added:
      letter_added.append(key[i])

  for i in range(65,91):
    if i==74:
      continue
    if chr(i) not in letter_added:
      letter_added.append(chr(i))
      
  k=0
  for i in range(5):
    for j in range(5):
      matrix[i][j] = letter_added[k]
      k+=1
  return matrix


def replace_duplicate(msg):
  i=0
  while(i<len(msg)):
    l1=msg[i]
    if(i == len(msg)-1):
      msg = msg+"X"
      i+=2
      continue
    l2 = msg[i+1]
    if l1==l2:
      msg = msg[:i+1] + "X" + msg[i+1:]
    i+=2
  return msg

def indexof(l, matrix):
  for i in range(5):
    if l in matrix[i]:
      return i,matrix[i].index(l)

def playfair(msg , key, encrypt = True):
  inc = 1
  if encrypt == False:
    inc = -1
  matrix = create_matrix(key)
  msg=msg.upper()
  msg.replace(' ','')
  msg=replace_duplicate(msg)

  cipher_text = ''

  for i in range(0,len(msg),2):
    l1 = msg[i]
    l2 = msg[i+1]
    row1, col1 = indexof(l1, matrix)
    row2, col2 = indexof(l2, matrix)    
    
    if row1 == row2:
      cipher_text += matrix[row1][(col1+inc)%5] + matrix[row2][(col2+inc)%5]
    elif col1 == col2:
      cipher_text += matrix[(row1+inc)%5][(col1)] + matrix[(row2+inc)%5][(col2)]
    else:
      cipher_text += matrix[row1][(col2)] + matrix[row2][(col1)]
  return cipher_text


plaintext = input("Enter your Message: ")
key = input("Enter the key: ")
cipher_text = playfair(plaintext , key, True)
print(cipher_text)
decrypt_text = playfair(cipher_text , key, False)
print(decrypt_text)



