#inptus
first_num = float(input("First number: "))
second_num = float(input("Second number: "))
operation = input("Choose an operation (+, -, *, /): ")

#operation
plus = "+"
subtract = "-"
divide = "/"
multiple = "*"

#process
if operation == plus:
    results0 = first_num + second_num
    print(f"{first_num} + {second_num} = {results0}")

if operation == subtract:
    results1 = first_num - second_num
    print(f"{first_num} - {second_num} = {results1}")

if operation == divide:
    results2 = first_num / second_num
    print(f"{first_num} / {second_num} = {results2}")

if operation == multiple:
    results3 = first_num * second_num
    print(f"{first_num} * {second_num} = {results3}")