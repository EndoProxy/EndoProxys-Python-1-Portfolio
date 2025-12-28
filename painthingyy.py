def getFloatInput(s_prompt):
    while True:
        try:
            return float(input(s_prompt))
        except ValueError:
            print("Invalid input, please try entering a numeric input.")

def main():
    #Title
    print("PAINT JOB ESTIMATOR")
#User Input Values
    f_name = input("Enter the customer's last name: ")
    f_wallspace = getFloatInput("Enter the number of square feet of wallspace: ")
    f_gallons = getFloatInput("Enter the number of gallons of paint required: ")
    f_cost = getFloatInput("Enter the cost per gallon of paint: ")
    f_hours = getFloatInput("Enter the number of hours of labor required: ")
    f_laborCost = getFloatInput("Enter the labor cost per hour: ")
#Calculations
    f_totalPaintCost = f_gallons * f_cost
    f_totalLaborCost = f_hours * f_laborCost
    f_totalCost = f_totalPaintCost + f_totalLaborCost

    print(f"Total paint cost: ${f_totalPaintCost:.2f}")
    print(f"Total labor cost: ${f_totalLaborCost:.2f}")
    print(f"Total cost: ${f_totalCost:.2f}")
    print(f"{f_name}_paintjobestimate.txt has been created with the following details.")

main()
