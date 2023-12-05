"""
@Author: Ravi Singh

@Date: 2023-30-11 15:20:30

@Last Modified by:

@Last Modified time: 2023-05-12 17:20:30

@Title : Employee Wage Calculator
"""

import random


class Employee:
    """
            Description: daily_wage function that is used to calculate the wage of an employee
                         part-time and full-time.

            Parameter: None

            Return:

         """

    def __init__(self, total_days, total_working_hours, full_day, half_day, wage_per_hour):
        self.total_days = total_days
        self.total_working_hour = total_working_hours
        self.full_time = full_day
        self.part_time = half_day
        self.wage_per_hour = wage_per_hour

    def wage(self):
        day = 0
        total_hour = 0
        working_hour = 0
        full = part = absent = 0

        while day < self.total_days and total_hour < self.total_working_hour:
            emp = random.randint(0, 2)
            match emp:
                case 0:
                    # print('Employee is absent on Day ', day)
                    working_hour = 0
                    absent += 1
                case 1:
                    # print('Employee is present on Day ', day)
                    working_hour = self.full_time
                    full += 1
                case 2:
                    # print('Employee is working part-time on Day ', day)
                    working_hour = self.part_time
                    part += 1
            total_hour += working_hour
            day += 1
        print(f'Employee worked full-time for {full} days.')
        print(f'Employee worked part-time for {part} days.')
        print(f'Employee was absent for {absent} days.')
        print("Total Wage of the Employee for a month is ", total_hour * self.wage_per_hour)


if __name__ == "__main__":
    print(f'Welcome to the Employee Wage problem in the main branch.')
    month_days = int(input(f'Enter the Number of Working days for a month '))
    working_hours = int(input('Enter the Total Working Hours for a month'))
    full_time = int(input('Enter the full-time working hours '))
    part_time = int(input('Enter the part-time working hours '))
    per_hour_wage = int(input('Enter the wage per hour for the Employee '))
    employee1 = Employee(month_days, working_hours, full_time, part_time, per_hour_wage)
    employee1.wage()
