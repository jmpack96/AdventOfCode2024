#Function to solve the current days problem
def day_02():
    print("Starting to Solve Day Two")

    ##PART ONE
    safe_count = 0
    failed_list = []

    #loop over each line from input file
    with open('inputs/day_02_input.txt','r') as input_file:
        for line in input_file:
            nums = [float(i) for i in line.split()]

            #check if current line is safe
            is_safe = check_if_line_safe(nums)

            #if this line is considered safe, increment the counter. Otherwise add the line to a list for use later
            if is_safe:
                safe_count = safe_count + 1
            else:
                failed_list.append(nums)

    part_one_sol = str(safe_count)

    ##PART TWO
    #loop over each line that was marked as a failure in part one. All of the passes are still passes and don't need rechecked
    for i, line in enumerate(failed_list):
        #loop through every number in the line, removing it in each loop and testing if this solves the safety requirements
        for j, _ in enumerate(line):
            cleaned_line = line[:j] + line[j+1:]

            #check if line with one number is now passing the safety test
            is_safe = check_if_line_safe(cleaned_line)

            #if line is marked safe increment safe counter and break the loop to go the next line
            if is_safe:
                safe_count = safe_count + 1
                break

    part_two_sol = str(safe_count)

    #combine part one and part two solution and return
    solution = "".join(["\nPart 1 - ", part_one_sol, "\nPart 2 - ", part_two_sol])

    return solution

#function that takes a list of numbers and checks if they are "safe" given the problem statement
#using multiple returns, because once a check is failed there is no need to run further checks
def check_if_line_safe(nums):

    #check if first two numbers are increasing or decreasing
    if (nums[0] - nums[1] > 0):
        is_safe = True
        is_decreasing = True
    elif (nums[0] - nums[1] < 0):
        is_safe = True
        is_decreasing = False
    else:
        #if two numbers are equal it is an auto fail
        return False

    #loop through each number in list, we only need to go through all numbers -1 since we only care about the relation to the number to the right
    if is_safe:
        for i,_ in enumerate(nums[:-1]):
            first_num = nums[i]
            second_num = nums[i+1]

            #check if values starts decreasing and switches to 
            if is_decreasing and (first_num - second_num < 0):
                return False
            #check if values starts decreasing and switches to 
            elif not is_decreasing and (first_num - second_num > 0):
                return False

            #check if difference between two numbers is between 1 and 3
            diff = abs(first_num - second_num)
            if diff > 3 or diff == 0:
                return False

    return is_safe

#it is always good practice to have a main function even if you do not plan to use it. In this file the plan is just to call the day_xx function directly
def main():
    pass

#Script main function
#Helpful Note: Python does not have a typical main function like some languages. Using this chunk of logic tells Python that if this script, start in this function. 
#Main only runs when you start running the script from this file. You can call functions directly that exist in other files and when called directly, the main function in that script won't run.
if __name__ == "__main__":
    main()