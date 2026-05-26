items = [1, 2, 2, 3, 4, 4, 1, 5]
unique_items = []

for item in items:
    # Check if item is already in our unique list
    is_duplicate = False
    for unique_item in unique_items:
        if item == unique_item:
            is_duplicate = True
            break

    # If it is new, add it
    if not is_duplicate:
        unique_items.append(item)

print("List after removing duplicates:", unique_items)
