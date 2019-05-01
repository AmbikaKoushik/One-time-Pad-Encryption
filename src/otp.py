from enc import enc #importing Encryption module
from dec import dec #importing Decryption module
from keygen import keygen #importing Key Generation module
from freqdist import freqdist #importing Frequency Distribution module
from avgruntime import avgruntime #importing Average Run Time for encryption module

if __name__ == '__main__': #calling main function
        import sys #importing sys module
        import os #importing os module
        #First argument i.e sys.argv[0] is always otp.py
        #Second argument i.e sys.argv[1] is the called function
        #Comparing the second command line argument with respective functions to call
        if sys.argv[1] == 'enc': #Comparing with enc
                enc(sys.argv[2], sys.argv[3], sys.argv[4]) #Calling enc function
        elif sys.argv[1] == 'dec': #Comparing with dec
                dec(sys.argv[2], sys.argv[3], sys.argv[4]) #Calling dec function
        elif sys.argv[1] == 'keygen': #Comparing with keygen
                keygen(sys.argv[2], sys.argv[3]) #Calling keygen function
        elif sys.argv[1] == 'freqdist': #Comparing with freqdist
                freqdist(sys.argv[2], sys.argv[3]) #Calling freqdist function
        elif sys.argv[1] == 'avgruntime': #Comparing with avgruntime
                avgruntime(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]) #Calling avgruntime function               
