# Main Program
# Project 1 Fitness Tracking
#
# Name: Tyler Baxter
# Section: 03
# Date: 01/14/22

from fitnessTrackerFuncs import *


def main():
    welcome()
    while 1 == 1:
        name = input_name()
        age = input_age()
        height = input_height()
        weight_lb = input_weight()
        duration = input_duration()
        exercise_type = input_exercise_type()

        weight_kg = convert_lb_to_kg(weight_lb)
        met = compute_MET(exercise_type)
        cal_burned = compute_calorie_burned(duration, weight_kg, met)
        bmi = compute_BMI(weight_lb, height)
        bmi_cat = BMI_category(bmi)
        miles = compute_equivalent_miles(height, exercise_type, duration)

        print_info(name, age, height, weight_lb, cal_burned, bmi, bmi_cat, miles)
        response = input("Do you want to apply fitness tracking for another user (y/n)? ")
        while response != "n" and response != "y":
            response = input("Error: Response must be y or n: ")
        if response == "n":
            break


if __name__ == '__main__':
    main()
