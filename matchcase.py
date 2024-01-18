x = int(input("Enter the value of x:"))

match x:
    case 0:
        print("The value entered by you is zero")
        
    case 1:
        print("The value entered by you is one")
        
    case _:
        print("These are invalid value")