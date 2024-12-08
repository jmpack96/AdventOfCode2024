#Function to solve the current days problem
def day_01():
    print("Starting to Solve Day One")

    ##PART ONE
    with open('inputs/day_01_part_1_input.txt','r') as input_file:
        #split lists into two, list one being left numbers and list two being right numbers
        left_list = []
        right_list = []
        #loop over each line and assign number to correct list
        for line in input_file:
            split_line = line.split()
            left_list.append(split_line[0]) #note that python uses [] for indexing and indexing starts at 0 like most languages except matlab
            right_list.append(split_line[1])

    #python has built in list shorting, yay
    left_list.sort()
    right_list.sort()

    #loop over both lists, now sorted and calculate a subtraction value for each index (python can do this in one line, but I wrote it out for readability)
    diff_total = 0
    for left_number, right_number in zip(left_list, right_list):
        diff = abs(float(left_number) - float(right_number)) #when reading in a text file the numbers are strings, so we convert to float to do math
        diff_total = diff + diff_total

    ##PART TWO

    #default solution for all days is unsolved, once the day is solved then this block of code be replaced with the real solution
    solution = str(diff_total)

    return solution


#it is always good practice to have a main function even if you do not plan to use it. In this file the plan is just to call the day_xx function directly
def main():
    pass

#Script main function
#Helpful Note: Python does not have a typical main function like some languages. Using this chunk of logic tells Python that if this script, start in this function. 
#Main only runs when you start running the script from this file. You can call functions directly that exist in other files and when called directly, the main function in that script won't run.
if __name__ == "__main__":
    main()