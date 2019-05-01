def avgruntime(length, key, plaintext, ciphertext): #define Average Run Time for Encryption function
   from keygen import keygen #Importing keygen module from keygen.py
   from enc import enc #Importing enc module from enc.py
   import time #Importing time module
   a = [0]*5 #Initializing an array of 5 integers
   for i in range(len(a)): #Iterating the array
      keygen(length, key) #Calling keygen function
      start = time.time() #Noting the Start time
      enc(key, plaintext, ciphertext) #Calling enc function
      end = time.time() #Noting the end time
      a[i] = end - start #Calculate the time elapsed for Encryption function
      print('Time Taken = '+str(a[i])+' seconds') #Printing the elapsed time on Command Prompt
   averageRunTime = sum(a) / float(len(a)) #Calculating the average time elapsed for Encryption function
   print('Average Run time for lambda=' +length+' is:'+' '+str(averageRunTime)) #Printing the length of a Secret Key and time elapsed for Encryption function on Command Prompt
