num_1 = float(input("Enter a Number : "))
operator = input("Enter the operator : ")
num_2 = float(input("Enter another Number : "))

if operator == "+":
    Result = num_1 + num_2
    print(Result)

elif operator == "-":
    Result = num_1 - num_2
    print(Result)

elif operator == "/":
    Result = num_1 / num_2
    print(Result)

elif operator == "^":
    Result = pow(num_1, num_2)
    print(Result)

elif operator == "%":
    Result = num_1 % num_2
    print(Result)

elif operator == "*":
    Result = num_1 * num_2
    print(Result)

else :
    print("Sorry!!, This Calculator is not equipped to perform the mentioned operation.")

