

#This is a simple introduction 
print("\nThis program is about password manage")

menu = """
Enter [1] to add new details."
Enter [2] to display stored details."
Enter [q] to exit the program."
"""
print("\n", menu,)

choice = ' '

# create a while loop that runs untiil the user enters 'q' to exit the program
while choice != 'q':     

    #prompt the user to enter selection
    choice = input("\nNow, Enter your selection here: ")

    #respond to the user's choice. 
    if choice == '1': 
        print("You have selected Option 1 ")
    elif choice == '2':
        print("You have selected Option 2 ")
    elif choice == 'q':
        print("You have selected Option 'q', this program will be exited. ")
    else:
        print("Invalid option, please try again...")

print("\nProgram ended!\n")

