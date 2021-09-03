
#https://www.thegeekstuff.com/2019/03/python-oop-examples/


class Person:
	def __init__(self, id, fname, lname, age, w, email):
		self.personid = id
		self.fname = fname
		self.lname = lname
		self.age = age
		self.weight = w
		self.email = email
		self.past_weights = []
		self.weight_date = []

		# add others

	def print_infor(self):
		print(self.personid, ' is id')
		print(self.fname, ' first name')
		print(self.lname, ' last name')
		print(self.age, ' is age ')
		print(self.weight, ' is weight ')
		print(self.past_weights, ' is weight history ')
		print(self.weight_date, ' is weight input date history ')

	def add_person(self, id, fname, lname, age, w, email):
		self.personid = id
		self.fname = fname
		self.lname = lname
		self.age = age
		self.weight = w
		self.email = email

	def update_weight(self, weight, date):
		self.past_weights.append(weight)
		self.weight_date.append(date)






if __name__ == "__main__":




	'''r.print_infor()
	p.print_infor()
	m.print_infor()
	z.print_infor()'''


	#r.print_infor()


	# define a list of Persons

	size = 5

	list_person = [None]*size  # memory blocks of size 20

	for n in range(0,  size):  
		list_person[n] = Person(n, "first", "last", 0, 0, '@x.com')

	list_person[0].print_infor()

	
	for n in range(0,  size):  
		list_person[n].print_infor()


# another way to make a list

	print(' another way')

	list_per = []

	for n in range(0,  size):  
		list_per.append(Person(n, "pahla", "aakhri", 0, 0, '@x.com'))

	
	for n in range(0,  size):  
		list_per[n].print_infor()


	
	list_per[0].add_person(0, "ranjeeta", "kumari", 40, 55, '@x.com')
	list_per[1].add_person(1, "rohitash", "chandra", 37, 78, '@y.com')
	list_per[2].add_person(2, "michael", "horton", 23, 62, ' @z.com')
	list_per[3].add_person(4, "avimanyu", "sahoo", 42, 80, '@f.com')


	list_per[1].update_weight(78.1, '1 09 2021')
	list_per[1].update_weight(78.5, '3 09 2021')
	list_per[1].update_weight(78.3, '7 09 2021')



	for n in range(0,  size):  
		list_per[n].print_infor()

	print(' now lets search for a name in the list')

	name_search = 'sahoo'

	for n in range(0,  size):  

		if list_per[n].fname == name_search or list_per[n].lname == name_search:
			list_per[n].print_infor()


# think of sorting the list by weight ( bit difficult)

# searching name in the list




	 







