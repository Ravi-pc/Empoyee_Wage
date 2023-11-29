"""
@Author: Ravi Singh

@Date: 2023-28-11 15:20:30

@Last Modified by: Ravi Singh

@Last Modified time: 2023-29-11 14:52:30

@Title : Employee Wage Calculator
"""

import random


def daily_wage():
    wage_per_hour = 20
    full_day_hour = 8
    total_wage = wage_per_hour * full_day_hour
    print('Employee Daily Wage is ', total_wage)


def attendance():
    """

        Description: Attendance function checks the attendance of employee is present or
                        not using random function.

        Parameter: None

        Return: 0 or 1

     """
    check = (random.randint(0, 1))
    print(check)
    if check == 1:
        print("Employee is present")
        daily_wage()
    else:
        print("Employee is absent")


if __name__ == "__main__":
    print("Welcome to the Employee Wage Computation Program on master branch ")
    attendance()
