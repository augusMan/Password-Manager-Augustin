def add_new_credentials():
    menu = """
    Create a text file for credential storage if a text file does not already exist\n
    Append new records to the text file without overwriting previous entries\n
    """
    print(menu)

    #get user name
    name = input ("Enter your name here: ")

    # to encrypte the user password
    password = input("Enter your password here: ")
    charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, "
    enpassword = "".join([charSet[(charSet.find(c)+3)%95] for c in password])
    print("\nYour encrypted password is", enpassword)

    website = input("Enter your URL here: ")

    f = open("file.txt", "a")
    f.write(name + "   " + enpassword + "   " + website + "   ")
    print("\nYour new details have now been stored. ")


def display_stored_details():
    
    #to check if a file exists
    try:
        f = open('file.txt')  
        print("File Exists! \n")
        f.close()    
    #display an error message if the file not found
    except FileNotFoundError:
        print('No password file created, create and add data to a new file first \n') 

    # open the file
    f = open("file.txt", "r")
    data = f.read() 
    print(data)
    stripped_data = data.strip() 
    dataList = stripped_data.split("   ") 

    #to decrypt the password
    if dataList != "":
        i = 0
        border = "|"
        print(f"{border}{'Username' : ^20}{border}{'Password' : ^20}{border}{'website' : ^20}{border}")
        print("--------------------------------------------------------------------")
        
        #repeat until 'i' is larger than the list length
        while i < len(dataList): 
            
            password = dataList[i+1]
            
            charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, "
            decryptpassword = "".join([charSet[(charSet.find(c)-3)%95] for c in password])

            print(f"{border}{dataList[i] : ^20}{border}{decryptpassword : ^20}{border}{dataList[i+2] : ^20}{border}")
            i += 3
    else:
        print("\nAll data has now been displayed\n")

# This is a simple introduction for this program
print("\nThis program is about password manager. ")


# to display the information of creator
print("""
      ****************************************************************************************
            Name: Augustin Pi
            Student ID: s8062928
            Program: User Password manager
      ****************************************************************************************""")

#This is a simple introduction 
print("\nThis program is about password manage")

# Give all the choices in a series of print statements.
print("Enter [1] to add new details.")
print("Enter [2] to display stored details.")
print("Enter [q] to exit the program.")

choice = ''
# create a while loop that runs untiil the user enters 'q' to exit the program
while choice != 'q': 

    #prompt the user to enter selection and respond to the user's choice. 
    choice = input("\nMake your choice here: ")
    if choice == '1': 
        add_new_credentials()     #call the function that created before
    elif choice == '2':
        display_stored_details()      #call the function 
    elif choice == 'q':
        print("You have selected Option 'q', this program will be exited. ")
    else:
        print("Invalid option, please try again...")
print("\nProgram ended!\n")