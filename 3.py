a1 = int(input())
a2 = int(input())
x = input()
if x == "/":
    if a2 == 0:
        print("Деление на 0!")
    else:
        print(a1 / a2)
elif x == "*":
    print(a1 * a2)
elif x == "-":
    print(a1 - a2)
elif x == "+":
    print(a1 + a2)
elif x == "div":
    if a2 == 0:
        print("Деление на 0!")
    else:
        print(a1 // a2)
elif x == "mod":
    if a2 == 0:
        print("Деление на 0!")
    else:
        print(a1 % a2)
elif x == "pow":
    print(a1 ** a2)