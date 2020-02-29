def mySum(var1,var2,var3):
    var1=input("Give ")
    result=max(var1,var2,var3)
    print("Result:",str(result))
mySum(20,13,11)

#or
def greatest(num1, num2, num3):
    if(num1>num2 and num1>num3):
        print(num1)
    elif(num2>num1 and num2>num3):
            print(num2)
    else:
            print(num3)
greatest(4,23,89)
