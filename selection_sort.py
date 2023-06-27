def selectionSort(list, size):	
	for i in range(size):
		min_index = i

		for j in range(i + 1, size):
			# select the minimum element in every iteration
			if list[j] < list[min_index]:
				min_index = j
		# swapping the elements to sort the array
		(list[i], list[min_index]) = (list[min_index], list[i])

list = [2, 1, 5, 8, 2, 0, 0, 9]
print(f"Before: {list}")
size = len(list)
selectionSort(list, size)
print(f"After: {list}")