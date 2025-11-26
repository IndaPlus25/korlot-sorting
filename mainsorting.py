#Main file to choose which method to use

#import slumpa as slumpa
from Insertion_sort import *


def fun_programtask():
    command = (input("Type the number what you want to do\n 1 Insertion sort\n 2 Selection sort\n 3 Merge sort\n 4 My sort\n\n Anything else will end the program\n: "))

    if command == "1":
        my_list = slumpa.rdn_new_list()
        main_insertion(my_list)
        fun_programtask()

    elif command == "2":
        slumpa.rdn_new_list()
        fun_programtask()
    
    elif command == "3":
        slumpa.rdn_new_list()
        fun_programtask()
    
    elif command == "4":
        slumpa.rdn_new_list()
        fun_programtask()

    else:
        quit()

if __name__ == "__main__":
    fun_programtask()