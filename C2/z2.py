n1 = int(input("A = "))
n2 = int(input("B = "))
op = input("Operation: ")

print("\nResult:")

match op:
    case "+":
        print(n1 + n2)
    case "-":
        print(n1 - n2)
    case "*":
        print(n1 * n2)
    case "/":
        print(n1 / n2)
