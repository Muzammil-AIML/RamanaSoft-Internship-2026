text = input("Enter a string: ")
max_length = 0
start = 0
seen_positions = {}

for end in range(len(text)):
    current_char = text[end]

    # If char is seen and is inside the current window, move start
    if current_char in seen_positions and seen_positions[current_char] >= start:
        start = seen_positions[current_char] + 1

    seen_positions[current_char] = end

    # Calculate current window length
    current_length = end - start + 1
    if current_length > max_length:
        max_length = current_length

print(f"Length of longest unique substring: {max_length}")
