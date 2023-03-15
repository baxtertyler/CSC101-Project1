# Project 1 Fitness Tracking
#
# Name: Tyler Baxter
# Section: 03
# Date: 01/14/22

# purpose: Print the welcome message for the program
# signature: none -> none
def welcome():
    print("Welcome to Fitness Tracker Application!")
    print(" ")
    print("    To begin you must specify the participant's name, age, height(in inches),")
    print("    weight (in lb), exercise duration (in minutes), and exercise type (1-4)!")
    print("    Now you can compute the burned calories and BMI")


# purpose: Prompts user for their name and returns the value
# signature: none -> string
def input_name():
    name = input("Enter name: ")
    return name


# purpose: Prompts user for their age and returns the (valid) value
# signature: none -> int
def input_age():
    age = int(input("Enter age: "))
    while age <= 0:
        print("Error: age must be an integer >0!")
        age = int(input("Enter age: "))
    return age


# purpose: Prompts user for their height and returns the (valid) value
# signature: none -> float
def input_height():
    height = float(input("Enter height in inches: "))
    while height <= 0:
        print("Error: Height must be greater than 0!")
        height = float(input("Enter height in inches: "))
    return height


# purpose: Prompts user for their weight and returns the (valid) value
# signature: none -> float
def input_weight():
    weight = float(input("Enter weight in lb: "))
    while weight <= 0:
        print("Error: Weight must be greater than 0!")
        weight = float(input("Enter weight in pounds: "))
    return weight


# purpose: Prompts user for their exercise duration and returns the (valid) value
# signature: none -> float
def input_duration():
    dur = float(input("Enter duration of exercise in minutes: "))
    while dur < 0:
        print("Invalid response : duration must be >=0!")
        dur = float(input("Enter duration of exercise in minutes: "))
    return dur


# purpose: Prompts user for their exercise type and returns the (valid) value
# signature: none -> int
def input_exercise_type():
    ex_type = float(input("Enter exercise type: 1) low-impact 2) high impact 3) slow-paced 4) fast paced "))
    while ex_type <= 0:
        print("Error: Exercise type must be an integer between [1,4]")
        ex_type = float(input("Enter exercise type [1,4]: "))
    return ex_type


# purpose: Prints all the user inputs and calculated values
# signature: string, int, float, float, float, float, float, int, float -> none
def print_info(name, age, height, weight, calorie_burned, BMI, category, miles):
    print("           Name : ", name)
    print("            Age : ", age)
    print("         Height : %6.2f" % height)
    print("         Weight : %6.2f" % weight)
    print("          Miles : %6.2f" % miles)
    print("Burned Calories : %6.2f" % calorie_burned)
    print("            BMI : %6.2f" % BMI)
    print("   BMI Category : ", category)


# purpose: To convert the input weight from lbs to kgs
# signature: float -> float
def convert_lb_to_kg(weight):
    weight = weight * 0.45359237
    return weight


# purpose: To declare the MET based on the exercise type
# signature: int -> int
def compute_MET(exercise_type):
    if exercise_type == 1:
        met = 5
    elif exercise_type == 2:
        met = 7
    elif exercise_type == 3:
        met = 3
    else:
        met = 4
    return met


# purpose: To calculate the amount of calories burned
# signature: int, float, int -> float
def compute_calorie_burned(duration, weight, met_value):
    cal_burned = duration * (met_value * 3.5 * weight) / 200
    return cal_burned


# purpose: To calculate the user's BMI
# signature: float, float -> float
def compute_BMI(weight, height):
    bmi = 703 * weight / height ** 2
    return bmi


# purpose: To declare the BMI of the user
# signature: float -> string
def BMI_category(BMI):
    if BMI < 18.59:
        cat = "Underweight"
    elif BMI < 24.99:
        cat = "Normal Weight"
    elif BMI < 29.99:
        cat = "Overweight"
    else:
        cat = "Obesity"
    return cat


# purpose: To compute the equivalent miles that the user exercised
# signature: float, int, float -> float
def compute_equivalent_miles(height, exercise_type, duration):
    distance_step = (0.413 * height) / 12
    if exercise_type == 1:
        steps = 120
    elif exercise_type == 2:
        steps = 227
    elif exercise_type == 3:
        steps = 100
    else:
        steps = 152
    distance_feet = distance_step * duration * steps
    distance_miles = distance_feet / 5280
    return distance_miles
