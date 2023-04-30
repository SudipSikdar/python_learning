try:
    file = open("exception.py")
    age = int(input("Age:: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("please enter a numeric value")
else:
    print("No exception were thrown")
finally:
    file.close()    

        


