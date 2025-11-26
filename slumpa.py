#Create a new scrambeled list of target value

import random as random

def rdn_new_list():
    target_val = int(input("Skriv det högsta talet att slumpa ut: "))
    temp_target_val = target_val
    sort_list = []
    random_list = []

    while temp_target_val > 0:
        sort_list.append(temp_target_val)
        temp_target_val -= 1

    while sort_list != []:
        rnd_index = random.randint(1, target_val)
        random_list.append(sort_list[rnd_index - 1])
        del sort_list[rnd_index - 1]
        target_val -= 1

    #Uncomment to view the list:
    #print(random_list)

    return random_list

if __name__ == "__main__":
        rdn_new_list()
