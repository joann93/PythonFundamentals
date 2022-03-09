definitions = {}
while( True):
    print( "1: Add new definition")
    print( "2: Find definition")
    print( "3: Delete definition")
    print( "4: Ending the pogram ")
    choice= input ( " What do you want to do? ")
    if ( choice == "1" ):
      key = input (" Pass the word to define: ")
      definition = input ( "Pass the definition: ")
      definitions[key] = definition
      print( "Add definition- sucessful")
      print(definitions)
    elif ( choice == "2"):
        key = input ( "What do you want to find? " )
        if key in definitions:
            print ( definitions[key])
    elif (choice == "3"):
        key= input ( " What do you want to delete? ")
        del definitions[key]
        print("Delete sucessfully")
        print ( definitions)
    elif ( choice == "4"):
        print("Goodbye")
        break




