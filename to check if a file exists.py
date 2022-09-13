try:
    f = open('file.txt')  
    print("file exists")
    f.close()    
except FileNotFoundError: # File not found exception
    print('No password file created, create and add data to a new file first')