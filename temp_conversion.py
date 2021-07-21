import sys
import math

supported_input_units = ["kelvin", "celsius", "fahrenheit", "rankine"]
supported_target_units = ["kelvin", "celsius", "fahrenheit", "rankine"]

print("Welcome to Temptarature Conversion Program\nYou will be prompted for the required input parameters\n")

numeric_value = input("Enter numerical value : ")
unit_of_measure = input("Enter unit of measure : ").lower()
target_unit = input("Enter target unit of measure : ").lower()
student_response = input("Enter students numeric response : ")

if not numeric_value:
    sys.exit("Failed to read numerical value..Program exiting")
elif not unit_of_measure:
    sys.exit("Failed to read unit of measure..Program exiting")
elif not target_unit:
    sys.exit("Failed to read target unit of measure..Program exiting")
elif not student_response:
    sys.exit("Failed to read students response..Program exiting")

if "." in numeric_value:
    try:
        val = float(numeric_value)
    except ValueError as e:
        sys.exit("Invalid")
else:
    try:
        val = int(numeric_value)
    except ValueError as e:
        sys.exit("Invalid")

if "." in student_response:
    try:
        val = float(student_response)
    except ValueError as e:
        sys.exit("Invalid")
else:
    try:
        val = int(student_response)
    except ValueError as e:
        sys.exit("Invalid")

numeric_value = round(float(numeric_value), 2)
student_response = round(float(student_response), 2)

def conversion_pgm(numeric_value):
    if unit_of_measure == "kelvin" and target_unit == "kelvin":
        K =  numeric_value
        K = round(K, 2)
        if math.isclose(K, student_response):
            print("Correct")
        else:
            print("Incorrect")
    elif unit_of_measure == "kelvin" and target_unit == "celsius":
        C = numeric_value - 273.15
        C = round(C, 2)
        if math.isclose(C, student_response):
            print("Correct")
        else:
            print("Incorrect")
    elif unit_of_measure == "kelvin" and target_unit == "fahrenheit":
        F = numeric_value * 1.8 - 459.67
        F = round(F, 2)
        if math.isclose(F, student_response):
            print("Correct")
        else:
            print("Incorrect")
    elif unit_of_measure == "kelvin" and target_unit == "rankine":
        Ra = numeric_value * 1.8
        Ra = round(Ra, 2)
        if math.isclose(Ra, student_response):
            print("Correct")
        else:
            print("Incorrect")

    if unit_of_measure == "celsius" and target_unit == "celsius":
        C =  numeric_value
        C = round(C, 2)
        if math.isclose(C, student_response):
            print("Correct")
        else:
            print("Incorrect")
    elif unit_of_measure == "celsius" and target_unit == "kelvin":
        K = numeric_value  + 273.15
        K = round(K, 2)
        if math.isclose(K, student_response):
            print("Correct")
        else:
            print("Incorrect")
    elif unit_of_measure == "celsius" and target_unit == "fahrenheit":
        F =  C * 1.8 + 32
        F = round(F, 2)
        if math.isclose(F, student_response):
            print("Correct")
        else:
            print("Incorrect")
    elif unit_of_measure == "celsius" and target_unit == "rankine":
        Ra = unit_of_measure * 1.8 + 32 + 459.67
        Ra = round(Ra, 2)
        if math.isclose(Ra, student_response):
            print("Correct")
        else:
            print("Incorrect")

    if unit_of_measure == "fahrenheit" and target_unit == "fahrenheit":
       F =  numeric_value
       F = round(F, 2)
       if math.isclose(F, student_response):
           print("Correct")
       else:
           print("Incorrect")
    elif unit_of_measure == "fahrenheit" and target_unit == "kelvin":
       K = ( numeric_value + 459.67) / 1.8
       K = round(K, 2)
       if math.isclose(K, student_response):
           print("Correct")
       else:
           print("Incorrect")
    elif unit_of_measure == "fahrenheit" and target_unit == "celsius":
       C = ( numeric_value - 32) / 1.8
       C = round(C, 2)
       if math.isclose(C, student_response):
           print("Correct")
       else:
           print("Incorrect")
    elif unit_of_measure == "fahrenheit" and target_unit == "rankine":
       Ra =  numeric_value + 459.67
       Ra = round(Ra, 2)
       if math.isclose(Ra, student_response):
           print("Correct")
       else:
           print("Incorrect")

    if unit_of_measure == "rankine" and target_unit == "rankine":
       Ra  =  numeric_value
       Ra = round(Ra, 2)
       if math.isclose(Ra, student_response):
           print("Correct")
       else:
           print("Incorrect")
    elif unit_of_measure == "rankine" and target_unit == "kelvin":
       K =  numeric_value / 1.8
       K = round(K, 2)
       if math.isclose(K, student_response):
           print("Correct")
       else:
           print("Incorrect")
    elif unit_of_measure == "rankine" and target_unit == "fahrenheit":
       F =  numeric_value - 459.67
       F = round(F, 2)
       if math.isclose(F, student_response):
           print("Correct")
       else:
           print("Incorrect")
    elif unit_of_measure == "rankine" and target_unit == "celsius":
       C = ( numeric_value - 32 - 459.67) / 1.8
       C = round(C, 2)
       if math.isclose(C, student_response):
           print("Correct")
       else:
           print("Incorrect")

if  unit_of_measure in supported_input_units:
    if target_unit in supported_target_units:
        print("Analysing the student response....")
        #print("converting "+ str(numeric_value) + " " + unit_of_measure + " to " + target_unit)
        conversion_pgm(numeric_value)
    else:
        sys.exit("Invalid")
else:
    sys.exit("Invalid")

