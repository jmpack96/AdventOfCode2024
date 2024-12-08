#the imports feel a bit messy, so maybe I could of done something different here
from days.day_01 import day_01
from days.day_02 import day_02
from days.day_03 import day_03
from days.day_04 import day_04
from days.day_05 import day_05
from days.day_06 import day_06
from days.day_07 import day_07
from days.day_08 import day_08
from days.day_09 import day_09
from days.day_10 import day_10
from days.day_11 import day_11
from days.day_12 import day_12
from days.day_13 import day_13
from days.day_14 import day_14
from days.day_15 import day_15
from days.day_16 import day_16
from days.day_17 import day_17
from days.day_18 import day_18
from days.day_19 import day_19
from days.day_20 import day_20
from days.day_21 import day_21
from days.day_22 import day_22
from days.day_23 import day_23
from days.day_24 import day_24
from days.day_25 import day_25

#Call to script that solves user selected day
def solve_selected_day(user_selected_day):
    #This is a map that will hold all the functions and will be updated every time a new day is solved 
    function_map = {"1": day_01, "2": day_02, "3": day_03, "4": day_04, "5": day_05,
                    "6": day_06, "7": day_07, "8": day_08, "9": day_09, "10": day_10,
                    "11": day_11, "12": day_12, "13": day_13, "14": day_14, "15": day_15,
                    "16": day_16, "17": day_17, "18": day_18, "19": day_19, "20": day_20,
                    "21": day_21, "22": day_22, "23": day_23, "24": day_24, "25": day_25,}

    #initial user logging
    _print_day_string(user_selected_day)

    #solve the problem based on user selected day, input is used to map to the correct function call
    solution = function_map[user_selected_day]()

    #print the results to the user
    _print_solution_string(user_selected_day, solution)

#the "_" at the start of this function marks it as an internal function that cannot be called by outside scripts
def _print_day_string(day):
    print("".join(["You have Selected Day ", day]))

#the "_" at the start of this function marks it as an internal function that cannot be called by outside scripts
def _print_solution_string(day, solution):
    print("".join(["The Solution to Day ", day, " is: ", solution]))

#main function
def main():
    print("***Welcome to the 2024 Advent of Code***")

    #for now just update this manually, but could eventually set this up to allow actual user
    user_input = "2"

    #call the function mapper that will run the script needed to solve the selected day
    solve_selected_day(user_input)

#Script main function
#Helpful Note: Python does not have a typical main function like some languages. Using this chunk of logic tells Python that if this script, start in this function. 
#Main only runs when you start running the script from this file. You can call functions directly that exist in other files and when called directly, the main function in that script won't run.
if __name__ == "__main__":
    main()

