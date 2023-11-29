"""
@Author: Ravi Singh

@Date: 2023-28-11 15:20:30

@Last Modified by:

@Last Modified time: 2023-28-11 2:20:30

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
    emp = random.randint(0, 2)
    wage_per_hour = 20
    working_hour = 0
    match emp:
        case 0:
            print('Employee is absent')
            working_hour = 0
        case 1:
            print('Employee is present')
            working_hour = 8
        case 2:
            print('Employee is working part-time')
            working_hour = 4

    total_wage = working_hour * wage_per_hour
    print('Total wage for the day is ', total_wage)


if __name__ == "__main__":
    print("Welcome to the Employee Wage Computation Program on master branch ")
    daily_wage()
