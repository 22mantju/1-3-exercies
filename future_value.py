#!/usr/bin/env python3
        
#imports the file validation.py
import validation

def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest
    return future_value

####################################################################################################################

def get_float():
    # Get input from the user
    monthly_investment = float(input("Enter monthly investment: \t"))
    while monthly_investment <=0:
        print("Entry mys be greather than 0 and less then or equal to 1000\t")
        monthly_investment = float(input("Enter monthly investment: \t"))
        if monthly_investment >= 1 and monthly_investment <= 1000:
            break

    yearly_interest_rate = float(input("Enter yearly interest rate: \t"))
    while yearly_interest_rate <= 0 or yearly_interest_rate > 15:
        print("Entry must be greater than 0 and less than or equal to 15. Please try again.\t")
        yearly_interest_rate = float(input("Enter yearly interest rate: \t"))
        if yearly_interest_rate >= 1 and yearly_interest_rate <= 15:
            break        
    return monthly_investment, yearly_interest_rate

#####################################################################################################################

def get_int():
    years = int(input("Enter number of years\t\t"))
    while years <= 0 or years > 50:
        print("Entry must be greater than 0 and less than or equal to 50. Please try again.\t")
        years = int(input("Enter number of years: \t\t"))
        if years >=1 and years <= 50:
            break        
    return years

#####################################################################################################################

def main():
    choice = "y"
    monthly_investment = 0
    yearly_interest = 0
    yearly_interest_rate = 0
    years = 0
    while choice.lower() == "y":
        # Getting monthly_investment & yearly_interest_rate from user
        # "...validation.get_float()", is calling the file validation.py to this section in the def main()
        monthly_investment, yearly_interest_rate = validation.get_float()

        # Getting years from user
        # "...validation.get_int", is calling the file validation.py to this section in the def main()
        years = validation.get_int()

        # get and display future value
        future_value = calculate_future_value(monthly_investment, yearly_interest_rate, years)

        print()
        print("Future value:\t\t\t" + str(round(future_value, 2)))
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main ()
