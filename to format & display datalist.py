
#to check if a file exists
try:
    f = open('file.txt')  
    print("File Exists! \n")
    f.close()    

except FileNotFoundError: # File not found exception
    print('No password file created, create and add data to a new file first \n') 


f = open("file.txt", "r")
data = f.read() 
print(data)
stripped_data = data.strip() 
dataList = stripped_data.split("   ") 
print(dataList) 


#to decrypt the password
if dataList != "":
    i = 0
    border = "|"
    print(f"{border}{'Username' : ^20}{border}{'Password' : ^20}{border}{'Website' : ^20}{border}")
    print("--------------------------------------------------------------------")

    while i < len(dataList): #repeat until 'i' is larger than the list length
        
        password = dataList[i+1]
        
        charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, "
        decryptpassword = "".join([charSet[(charSet.find(c)-3)%95] for c in password])

        print(f"{border}{dataList[i] : ^20}{border}{decryptpassword : ^20}{border}{dataList[i+2] : ^20}{border}")
        i += 3
else:
    print("\nAll data has now been displayed\n")