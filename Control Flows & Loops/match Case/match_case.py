a = int(input("Enter a Lucky Number Between 1 & 10:- "))

match a :
    case 1:
        print("Congrats! You Got Apple Phone");
    case 3:
        print("OMG! You Got a chance to go Dubai!");
    case 6:
        print("Woooo Bro U Got Rolls Roys");
    case _ : # Default Case
        print("Better luck Next Time!");

print("End of Program!");


week = int(input("Enter Date to Know which day but only between 1 to 7:- "));

match week:
    case 1 :
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thrusday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _ : # Default Case
        print("Invalid Input Enter By User, Try Again!")

print("End of Program")

# Basic Calculator

a = int(input("Enter Number :- "));
b = int(input("Enter Number :- "));
num = int(input("Enter Value to Calculate:- "))

match num :
    case 1:
        print(f"{a}+{b} =",a+b)
    case 2:
        print(f"{a}-{b} =",a-b)
    case 3:
        print(f"{a}*{b} =",a*b)
    case 4:
        print(f"{a}/{b} =",a/b)
    case _ :  # Default Case
        print("Wrong Value")
print("End of Program");

