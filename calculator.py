import sys
from optparse import OptionParser

from tip_calculator_as_functions import calculate_rate, calculate_meal_costs

def valid_meal_base(price):
    '''Return True if price is a valid value for the meal'''
    try:
        price = float(price)
    except (ValueError, TypeError):
        return False
    if price < 0:
        return False
    return True

def valid_percentage(rate):
    '''Return True if rate is a valid percentage between 0 and 100'''
    try:
        rate = float(rate)
    except (ValueError, TypeError):
        return False
    if rate < 0 or rate > 100:
        return False
    return True

def get_user_value(condition, message, error_message):
    '''
    Get value from user
    
    message is a message to prompt the user
    condition is a function that must return true for value
    
    Returns a string value for the user's input
    '''
    while True:
        user_input = raw_input(message)
        if condition(user_input):
            break
        else:
            print error_message
    return user_input
            
def main():
    ''' Calculate costs for a meal
    
    The user inputs meal cost, tax rate, and tip rate as parameters
    If any parameters are invalid, the program will
    ask the user for valid ones.
    '''
    
    parser = OptionParser()
    parser.add_option("-m", "--meal", dest="meal", help="base cost of meal")
    parser.add_option("-x", "--tax", dest="tax_percent")
    parser.add_option("-t", "--tip", dest="tip_percent", 
                        help="percent tip you want to leave", default=20)  
                        #let's accrue good karma by defaulting to a decent 20%
                        #tip!
    (options, args) = parser.parse_args()

    #make sure we get valid values
    if not valid_meal_base(options.meal):
        options.meal = get_user_value(valid_meal_base, 
                        'Please enter a valid meal price: ', 
                        'That is not a positive number')
    meal = float(options.meal)
    
    if not valid_percentage(options.tax_percent):
        options.tax_percent = get_user_value(valid_percentage,
                                  'Please enter a valid tax percentage: ',
                                  'Enter a positive number between 0 and 100')
    tax_percent = float(options.tax_percent)
    
    if not valid_percentage(options.tip_percent):
        options.tip_percent = get_user_value(valid_percentage,
                                  'Please enter a valid tip percentage: ',
                                  'Enter a positive number between 0 and 100')
    tip_percent = float(options.tip_percent)
    
    costs = calculate_meal_costs(meal, 0.01*tax_percent, 0.01*tip_percent)
    meal_plus_tax = calculate_rate(0.01*tax_percent, meal) + meal
    tip_amount = costs['total'] - meal_plus_tax
    
    print 'The meal plus tax costs {:.2f} dollars'.format(meal_plus_tax)
    print 'You should tip {:.2f} dollars.'.format(tip_amount)

if __name__ == '__main__':
    main()
                                         