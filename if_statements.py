marks = 45
gradute = True
male = True
if marks >= 50:
    print("you are pass")   
elif male and gradute:
    print("you are male")

else:                                       # we cannot put condition in else 
    print("best of luck for next time")        


# comparison through if statements
    #  == comparison operator
def max(num1, num2, num3):
    if num1 > num2 and num2 > num3:
        return num1
    elif num2 >  num1 and num2 > num3:
        return num2

    else:
        return num3

print(max(12,23,34))