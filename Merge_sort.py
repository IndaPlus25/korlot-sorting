#Merge sort

def third_sort(my_list):
    main_list = []
    split_list = []
    target_length = len(my_list)

    while len(split_list) < target_length:
        first_output, second_output = mergesort(my_list)


def mergesort(ms_list):
    ms_first_half = []

    ms_half = int(len(ms_list)/2)

    if len(ms_list) == 1:
            return ms_list
    
    while ms_half > 0:
        ms_first_half.append(ms_list.pop(0))
        ms_half -= 1
    
    return ms_first_half, ms_list

def merge(first_list, second_list):
    merge_list = []

    while len(first_list) > 0 & (len(second_list) > 0):
        if first_list[0] > second_list[0]:
            merge_list.append(second_list.pop(0))
        else:
            merge_list.append(first_list.pop(0))

    while len(first_list) > 0:
        merge_list.append(first_list.pop(0))
    
    while len(second_list) > 0:
        merge_list.append(second_list.pop(0))
    
    return merge_list

if __name__ == "__main__":
    x = [1,2,5,6,9]
    y = [3,4,7,8,10,11]
    z = [1,2,3,4,6,7,8,11]
    
    print(merge(x,y))

    print(mergesort(z))
