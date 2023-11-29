"""
@Author: Ravi Singh

@Date: 2023-28-11 15:20:30

@Last Modified by:

@Last Modified time: 2023-28-11 2:20:30

@Title : Employee Wage Calculator
"""

import random


def attendance():
    """

        Description: Attendance function checks the attendance of employee is present or
                        not using random function.

        Parameter: None

        Return: 0 or 1

     """
    full_time = 1
    check = (random.randint(0, 100)) % 2
    print(check)
    if check == full_time:
        print("Employee is present")
    else:
        print("Employee is absent")


if __name__ == "__main__":
    print("Welcome to the Employee Wage Computation Problem ")
    attendance()
