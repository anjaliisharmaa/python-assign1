def count_occurrences(element, lst):
    return lst.count(element)

lst = [1, 2, 3, 4, 1, 4, 1]
element = 1
print(f"The element {element} occurs {count_occurrences(element, lst)} times in the list.")
