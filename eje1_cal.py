#!/usr/bin/python

sys de importanción 
import getopt 

def main ():

    try : 
        (opt,arg) = getopt.getopt(sys.argv[1:], 'm:n:o', [])
    except  getopt.GetoppError as error:
        print("ERROR", str(error))
        return()
    if len(opt) !=3:
        print("The number of parameters is incorrect.")
        return()
    else:
        print("options entered:", opt)
    number1 = 0
    number2 = 0

    
    for(op, arg) in opt:
        if op == "-n":
            print("number 1: ", arg)
            number1 = int(arg)
        elif op == "-m":
            print("Number 2: ", arg)
            number2 = int(arg)
        elif op == "-o":
            print("operation", arg)
     
     for(op, arg) in opt:
        if op == "-n":
            try:
                number1 = int(arg)
            except ValueError:
                print("The number 1 entered isn't an integer. ")
                print("Number: ", arg)
                exit()
        if op == "-o":
            if arg.lower() not in["+","-","x","/"]:
                print("The entered operation is invalid. Just use +, -, x or /")
                exit()
            operator = arg.lower()

    if op == "-o":
        if operator == "+":
            print(number1, "+", number2, "=", number1+number2)
        elif operator == "-":
            print(number1, "-", number2, "=", number1 - number2)
        elif operator == "x":
            print(number1, "x", number2, "=", number1*number2)
        elif operator == "/":
            print(number1, "/", number2, "=", number1 / number2)
            try:
                print(number1,"/",number2,"=",number1/number2)
            except ZeroDivisionError as err:
                print("Sorry, you can't divide by 0.", err)
                sys.exit()
main()
