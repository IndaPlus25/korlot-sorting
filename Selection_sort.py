#Selection_sort

def second_sort(import_list):
    step_value = 0

    #Go through list
    while step_value < len(import_list):
        current_min = import_list[step_value]
        current_min_spot = step_value
        start_check = step_value
        
        
        #See which spot has lowest value
        while start_check < len(import_list):
            if start_check == step_value:
                start_check += 1
                continue
            elif current_min > import_list[start_check]:
                current_min = import_list[start_check]
                current_min_spot = start_check
            start_check += 1

        import_list[step_value], import_list[current_min_spot] = import_list[current_min_spot], import_list[step_value]
        step_value += 1
    
    print(import_list)
    
if __name__ == "__main__":
    test = [5,6,9,2,4,1,8,10,3,7]
    print(second_sort(test))