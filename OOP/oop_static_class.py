class Employee:

	#instance variable (depending on how you use it)
	raise_amt = 1.04

	#class variable
	num_of_emps = 0

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
		Employee.num_of_emps += 1

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	#Class method to change the class variable raise_amt
	#equal to Employee.raise_amt = amount
	#class methods pass the class as the first argument
	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount

	#Alternative constructor
	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		#this line is gonna create a new employee
		return cls(first, last, pay)

	#Static methods (they dont pass anything as the first argument)
	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True



emp_1 = Employee('Corey', 'Shcafer', 50000)
emp_2 = Employee('Test', 'User', 60000)


#this changes every instance variable named raise_amount
#Employee.raise_amount = 1.05

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

print(Employee.num_of_emps)

#Example on how yo use class method as an alternative constructor
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)

import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))


