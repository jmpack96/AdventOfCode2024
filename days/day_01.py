#Function to solve the current days problem
def day_01():
    print("Starting to Solve Day One")

    ##PART ONE
    with open('inputs/day_01_input.txt','r') as input_file:
        #split lists into two, list one being left numbers and list two being right numbers
        left_list = []
        right_list = []
        #loop over each line and assign number to correct list
        for line in input_file:
            split_line = line.split()
            left_list.append(split_line[0]) #note that python uses [] for indexing and indexing starts at 0 like most languages except matlab
            right_list.append(split_line[1])

    #python has built in list shorting, yay
    sorted_left_list = sorted(left_list)
    sorted_right_list = sorted(right_list)

    #loop over both lists, now sorted and calculate a subtraction value for each index (python can do this in one line, but I wrote it out for readability)
    diff_total = 0
    for left_number, right_number in zip(sorted_left_list, sorted_right_list):
        diff = abs(float(left_number) - float(right_number)) #when reading in a text file the numbers are strings, so we convert to float to do math
        diff_total = diff + diff_total

    part_one_sol = str(diff_total)

    ##PART TWO
    #loop over left list only, Need to use unsorted list
    sim_score = 0
    for left_number in left_list:
        count = right_list.count(left_number) #count occurrences of left number in right list
        sim_score = sim_score + (count*float(left_number))

    part_two_sol = str(sim_score)

    #combine part one and part two solution and return
    solution = "".join(["\nPart 1 - ", part_one_sol, "\nPart 2 - ", part_two_sol])

    return solution

#it is always good practice to have a main function even if you do not plan to use it. In this file the plan is just to call the day_xx function directly
def main():
    pass

#Script main function
#Helpful Note: Python does not have a typical main function like some languages. Using this chunk of logic tells Python that if this script, start in this function. 
#Main only runs when you start running the script from this file. You can call functions directly that exist in other files and when called directly, the main function in that script won't run.
if __name__ == "__main__":
    main()