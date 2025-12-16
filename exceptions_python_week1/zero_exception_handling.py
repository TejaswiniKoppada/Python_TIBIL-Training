# 1. Divide numbers with zero exception handling

def divide_num(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        print("Number can't be divided by zero")
        return None
    except TypeError:
        print("Make sure you enter only numbers")
        return None
    else:
        print("Division is perfect")
    finally:
        print("Division is Completed")

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
result = divide_num(num1, num2)
print("Result:", result)


# while True:
#     try:
#         num1 = float(input("Enter the first number: "))
#         num2 = float(input("Enter the second number: "))
#         break  # stop asking once valid numbers are entered
#     except ValueError:
#         print("Please enter only numbers.\n")  # show message and loop again
#
# # call the function
# result = divide_num(num1, num2)
# print("Result:", result)