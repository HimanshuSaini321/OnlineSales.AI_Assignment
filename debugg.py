def compute(n):
    if n < 10:
        out = n ** 2
    elif n < 20:
        out = 1
        for i in range(1, n - 9):  # Changed n-10 to n-9 for correct factorial calculation
            out *= i
    else:
        lim = n - 20
        out = 0  # Initialize out as 0 for the sum calculation
        for i in range(1, lim + 1):
            out += i
    print(out)


n = int(input("Enter an integer: "))
compute(n)