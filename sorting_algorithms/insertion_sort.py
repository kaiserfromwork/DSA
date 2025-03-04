
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        key = my_list[i]
        j = i - 1
        print(f"Key: {key}")
        print(f"J: {j}")
        while j >= 0 and my_list[j] > key:
            my_list[j + 1] = my_list[j]
            j = j - 1
        my_list[j + 1] = key
    return my_list


list_test = [5, 2, 4, 6, 1, 3]
print(insertion_sort(list_test))
