def keygen(length,newkey): #define Key Generation function
        if int(length) in range(1,129): #Checking if 1<=length of Secret Key<=128
                import random #Importing random module
                k = format(random.randint(0,pow(2,int(length))-1), '0'+length+'b') #Generating a random key of given length
                f = open(newkey,'w') #Opening the newkey.txt file in write mode
                f.write(str(k)) #Writing the New Key
                print('Key Length:'+'   '+str(len(k))) #Printing the length of New Key to command prompt
                print('Key:'+'   '+k) #Printing the New Key to command prompt
                f.close() #Closing the newkey.txt file
        else:
                print('Please enter a value between 1 and 128 including the extreme values')
