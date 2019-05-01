def freqdist(length, record): #define Frequency Distribution function
        from keygen import keygen #Importing keygen module from keygen.py
        import sys #Importing sys module
        import random #Importing random module
        f1 = open(record,'a') #Opening the record.txt file in append mode
        fd = [0]*pow(2,int(length)) #Initializing an array to store the key frequency
        for i in range(5000): #Iterating 5000 times
                keygen(length, '../data/temp.txt') #Calling keygen function to generate a key of given length
                f2 = open('../data/temp.txt','r') #Opening the temp.txt file that contains the generated key
                tk = f2.readline() #Reading the generated Key value
                f2.close() #Closing the temp.txt file
                r = int(tk,2)             
                fd[r] = fd[r] + 1 #Counting the no. of occurences of key
                f1.write(tk+'\n') #Collecting the generated key value into record.txt file
        f1.close() #Closing the record.txt file
        
        for i in range(0,len(fd)): #Iterating the frequency distribution array
                f1 = open(record,'a') #Opening the record.txt file in append mode
                f1.write('Value:'+'    '+'No. of Occurences\n')
                print('Value:'+'    '+'No. of Occurences')
                f1.write(str(i)+'   '+str(fd[i])+'\n') #Writing the KeyValue and its no. of occurences to record.txt file
                print(str(i)+'   '+str(fd[i]))
