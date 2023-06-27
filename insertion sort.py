def insertionsort(list):
    for i in range(1, len(list)):
        current_value = list[i]
        position = i

        while position > 0 and list[position - 1] > current_value:
            list[position] = list[position - 1]
            position = position - 1
        
        list[position] = current_value


list = [2, 1, 5, 8, 2, 0, 0, 9]
print(f"Before: {list}")
insertionsort(list)
print(f"After: {list}")