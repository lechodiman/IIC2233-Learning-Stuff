class Employee:

	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
	raise_amt = 1.10

	def __init__(self, first, last, pay, prog_lang):
		#let the super class handle these arguments
		super().__init__(first, last, pay)
		#alternative form
		#Employee.__init__(self, first, last, pay)
		self.prog_lang = prog_lang

class Manager(Employee):

	def __init__(self, first, last, email, employees = None):
		super().__init__(first, last, email)
		if employees == None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Shcafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

#useful functions

print(isinstance(mgr_1, Developer))
print(issubclass(Manager, Developer))


#mgr_1.add_emp(dev_2)
#mgr_1.remove_emp(dev_1)

#mgr_1.print_emps()

#useful info
#print(help(Developer))

#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)


