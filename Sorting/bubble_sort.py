def bubblesort(elements):
for n in range(len(elements)-1, 0, -1):
	for i in range(n):
	if elements[i] > elements[i + 1]:
		elements[i], elements[i + 1] = elements[i + 1], elements[i]
elements = [9,3,6,11,77,2,33,43,34,90]

print("Unsorted list is,")
print( elements)
bubblesort(elements)
print("Sorted Array is, ")
print(elements)
