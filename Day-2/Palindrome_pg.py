text = input("Enter a string or number: ").lower()
reversed_text = ""

# Reverse the string manually
for char in text:
    reversed_text = char + reversed_text

if text == reversed_text:
    print("Palindrome")
else:
    print("Not a Palindrome")
