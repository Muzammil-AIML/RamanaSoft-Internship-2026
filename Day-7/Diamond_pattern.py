n = 5

# Upper Part
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")

    ch = 65
    for k in range(2 * i + 1):
        print(chr(ch), end="")
        ch += 1

    print()

# Lower Part
for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(" ", end="")

    ch = 65
    for k in range(2 * i + 1):
        print(chr(ch), end="")
        ch += 1

    print()