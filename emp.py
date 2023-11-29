"""
@Author: Ravi Singh

@Date: 2023-28-11 15:20:30

@Last Modified by:

@Last Modified time: 2023-28-11 2:20:30

@Title : Employee Wage Calculator
"""

import random


def calculate_wage(hours):
    """

            Description: calculate_wage function to calculate the wage of an employee
                            working part-time or full-time.

            Parameter: Working hours

            Return:
        """

    wage_per_hour = 20
    total_wage = wage_per_hour * hours
    print('Total wage of the Employee is ', total_wage)


def emp_day():
    """
            Description: daily_wage function that is used to calculate the wage of an employee
                         part-time and full-time.

            Parameter: None

            Return: 0 or 1

         """
    atd = check_attendance()
    if atd == 1:
        print('Employee is present ')
        day = check_attendance()
        if day == 1:
            print('Employee is working full-time ')
            calculate_wage(8)
        else:
            print('Employee is working part-time ')
            calculate_wage(4)
    else:
        print('Employee is absent ')


def check_attendance():
    """

        Description: Attendance function checks the attendance of employee is present or
                        not using random function.

        Parameter: None

        Return: 0 or 1

     """

    check = (random.randint(0, 1))
    return check


if __name__ == "__main__":
    print("Welcome to the Employee Wage Computation Program on master branch ")
    emp_day()
