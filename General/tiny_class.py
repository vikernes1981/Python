class Employee():
	"""creating employees"""
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
	def get_name(self):
		self.name = input("Give name : ")
		print(self.name)
	def get_salary(self):
		self.salary = input("How much money you get? : ")
		print(self.salary)

empList = []
while True:
	name = input("Give name : ")
	if not name : break
	salary = input("Give salary : ")
	if not salary : break
	empList.append(Employee(name, salary))

for item in sorted(empList, key = lambda x : x.salary):
	print(item.name,item.salary, sep="\t")
		
