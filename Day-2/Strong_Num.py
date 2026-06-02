num = int(input("Enter a number: "))

temp = num
total_sum = 0

# Loop one by one to extract digits and calculate factorial
while temp > 0:
    digit = temp % 10

    # Calculating factorial of the digit
    fact = 1
    for i in range(1, digit + 1):
        fact *= i

    total_sum += fact
    temp //= 10

# Check and print result
if total_sum == num:
    print(f"{num} is a Strong Number")
else:
    print(f"{num} is NOT a Strong Number")