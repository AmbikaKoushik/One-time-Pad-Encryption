def dec(key, ciphertext, result): #define Decryption function
        f1 = open (key,'r') #Opening the key.txt file in read mode
        sk = (f1.readline()).strip('\n') #Reading the Secret Key
        f1.close() #Closing the key.txt file
        f2 = open (ciphertext,'r') #Opening the ciphertext.txt file in read mode
        c = (f2.readline()).strip('\n') #Reading the CipherText
        f2.close() #Closing the ciphertext.txt file
        if len(sk) == 8*len(c): #Comparing the length of Secret Key with length of CipherText
                i = 0
                m = '' #Initializing the Decrypted message
                for ch in c: #Iterating each character in the Decrypted message
                        ct = format(ord(ch),'08b') #Converting each character into its ascii value into 8 bit binary form
                        k = sk[i:i+8] #Reading the corresponding 8 bits from Secret Key
                        msg = chr(int(ct,2) ^ int(k,2)) #Performing XOR (One Time Padding)
                        m = m + msg #Generating Decrypted Message from One Time Padded values
                        i = i + 8 #Moving the Secret Key pointer to the next 8 bits

                f3 = open(result,'w') #Opening the result.txt file in write mode
                f3.write(m) #Writing the Plain Text
                print(m) #Printing the Decrypted Message to command prompt
                f3.close() #Closing the result.txt file
        
        else:
                print ('error: length is incorrect!') #Error message when length of Secret Key does not match with the length of CipherText
