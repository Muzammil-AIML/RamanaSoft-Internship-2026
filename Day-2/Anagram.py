str1 = input("Enter first word: ").lower()
str2 = input("Enter second word: ").lower()

# Basic sorting without built-in sorted() fxn
list1 = list(str1)
list2 = list(str2)

# Bubble sort list1
for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] > list1[j]:
            list1[i], list1[j] = list1[j], list1[i]

# Bubble sort list2
for i in range(len(list2)):
    for j in range(i + 1, len(list2)):
        if list2[i] > list2[j]:
            list2[i], list2[j] = list2[j], list2[i]

if list1 == list2:
    print("Anagram")
else:
    print("Not an Anagram")
