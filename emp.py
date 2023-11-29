"""
@Author: Ravi Singh

@Date: 2023-28-11 15:20:30

@Last Modified by:

@Last Modified time: 2023-28-11 2:20:30

@Title : Employee Wage Calculator
"""

import random


def daily_wage(present):
    """
            Description: daily_wage function that is used to calculate the wage of an employee
                         part-time and full-time.

            Parameter: None

            Return: 0 or 1

         """
    wage_per_hour = 20
    full_time = present
    part_time = 2
    emp = random.randint(0,100) % 3
    if emp == full_time:
        working_hour = 8
        print('Employee is working full time. ')
    else:
        working_hour = 4
        print('Employee is working part time. ')

    total_wage = wage_per_hour * working_hour
    print('Employee Daily Wage is ', total_wage)


def attendance():
    """

        Description: Attendance function checks the attendance of employee is present or
                        not using random function.

        Parameter: None

        Return: 0 or 1

     """
    full_time = 1
    check = (random.randint(0, 100)) % 2
    if check == full_time:
        print("Employee is present")
        daily_wage(check)
    else:
        print("Employee is absent")


if __name__ == "__main__":
    print("Welcome to the Employee Wage Computation Program on master branch ")
    attendance()
