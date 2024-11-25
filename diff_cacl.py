def calculate(n1, n2):
    diff = n1 - n2
    percent = (diff / n1) * 100
    percent = round(percent, 2)
    print(f"{n1}-{n2}={diff}s ({percent}%)")

while True:
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    calculate(n1, n2)