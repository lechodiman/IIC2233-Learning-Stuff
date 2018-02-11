var = 50

class A:
	class_variable = var

	@property
	def i_am_property(self):
		if self.class_variable == 50:
			return "i am 50"
		else:
			return "i am not 50"



a = A()
print(a.i_am_property)
A.class_variable = 25
print(a.i_am_property)


