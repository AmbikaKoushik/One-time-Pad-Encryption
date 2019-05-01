def enc(key, plaintext, ciphertext): #define Encryption function
        f1 = open (key,'r') #Opening the key.txt file in read mode
        sk = (f1.readline()).strip('\n') #Reading the Secret Key
        f1.close() #Closing the key.txt file
        f2 = open (plaintext,'r') #Opening the plaintext.txt file in read mode
        m = (f2.readline()).strip('\n') #Reading the PlainText/Message
        f2.close() #Closing the plaintext.txt file
        if len(sk) == (8*len(m)): #Comparing the length of Secret Key with length of Message
                i = 0
                c = '' #Initializing the CipherText
                for ch in m: #Iterating each character in the Message
                        pt = format(ord(ch),'08b') #Converting each character into its ascii value into 8 bit binary form
                        k = sk[i:i+8] #Reading the corresponding 8 bits from Secret Key
                        ct = chr(int(pt,2) ^ int(k,2)) #Performing XOR (One Time Padding)
                        c = c + ct #Generating CipherText from One Time Padded values
                        i = i + 8 #Moving the Secret Key pointer to the next 8 bits

                f3 = open(ciphertext,'w') #Opening the ciphertext.txt file in write mode
                f3.write(c) #Writing the CipherText
                print(c) #Printing the CipherText to command prompt
                f3.close() #Closing the ciphertext.txt file
        else:
                print ('error: length is incorrect!') #Error message when length of Secret Key does not match with the length of Message
