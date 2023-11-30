"""
@Author: Ravi Singh

@Date: 2023-30-11 15:20:30

@Last Modified by:

@Last Modified time: 2023-30-11 12:20:30

@Title : Employee Wage Calculator
"""

import random


def daily_wage():
    """
            Description: daily_wage function that is used to calculate the wage of an employee
                         part-time and full-time.

            Parameter: None

            Return:

         """

    wage_per_hour = 20
    working_hour = 0
    total_hour = 0
    day = 0
    while day <= 20 and total_hour <= 100:
        emp = random.randint(0, 2)
        match emp:
            case 0:
                print('Employee is absent on Day ', day)
            case 1:
                print('Employee is present on Day ', day)
                working_hour = 8
            case 2:
                print('Employee is working part-time on Day ', day)
                working_hour = 4
        total_hour += working_hour
        day += 1
    print('Total working hours of an employee is', total_hour)
    print('The monthly wage of an employee is', total_hour*wage_per_hour)


if __name__ == "__main__":
    print("Welcome to the Employee Wage Computation Program on master branch ")
    daily_wage()