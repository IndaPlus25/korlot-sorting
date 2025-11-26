#Insertion sort

def main_insertion(my_list):
    start_value = 1

    if my_list == []:
            print("********************\nEmpty list!\nplease choose a new list.\n********************")
            quit()
    
    while start_value < len(my_list):
        control_value = start_value
        
        #todo
        #Kommer in i loopen men går ur den efter en runda
        while (my_list[control_value - 1] > my_list[control_value]) & control_value > 0:    
            my_list[control_value - 1], my_list[control_value] = my_list[control_value], my_list[control_value - 1]
            print("control value: ",control_value)
            control_value -= 1
        start_value += 1

    print(my_list)
if __name__== "__main__":
    test_list = [2,1,3,5,6,4,10,8,9,7]
    main_insertion(test_list)