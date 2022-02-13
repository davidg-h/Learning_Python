import math

class IsaNumber(Exception):
    pass

while True:
    try:
        n = int(input("Please enter a number: "))
        if not math.isnan(n):
            raise IsaNumber
        break
    except ValueError: # or Exception
        print("Input was not a number. Try again")
    except IsaNumber:
        print(f"{n} Is a number")
        break
    finally:
        print("This is for testing")
else:
    print("Programm ended")