try:
    num1 = 3
    num2 = 6
    result = num1/num2
    print(result)
except ZeroDivisionError:
    print("Undefined")
finally:
    print("This program is finished.")