import sys

from tip_calculator_as_functions import calculate_rate, calculate_meal_costs

def valid_meal_base(price):
    '''Return True if price is a valid value for the meal'''
    try:
        price = float(price)
    except ValueError:
        return False
    if price < 0:
        return False
    return True

def valid_percentage(rate):
    '''Return True if rate is a valid percentage between 0 and 100'''
    try:
        rate = float(rate)
    except ValueError:
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
            
    
    

# def get_meal_base():
#     '''get base price of meal using raw input'''
#     while True:
#         try:
#             meal_base = float(raw_input('Enter base price for meal in dollars: '))
#             if meal_base < 0.0:
#                 raise ValueError
#             break
#         except ValueError:
#             print 'Please enter a positive number'
#     return meal_base

