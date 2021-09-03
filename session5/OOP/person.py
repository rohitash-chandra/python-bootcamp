
#https://www.thegeekstuff.com/2019/03/python-oop-examples/


class Person:
    def __init__(self, fname, lname, age, w, email):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.weight = w
        self.email = email
        self.past_weights = []
        self.weight_date = []
        # add others

    def print_infor(self):
        print(self.fname, ' first name')
        print(self.lname, ' last name')
        print(self.age, ' is age ')
        print(self.weight, ' is weight ')

        print(self.past_weights, ' is weight history ')
        print(self.weight_date, ' is weight input date history ')

    def update_weight(self, weight, date):
        self.past_weights.append(weight)
        self.weight_date.append(date)






if __name__ == "__main__":


    p = Person("ranjeeta", "kumari", 40, 55, '@x.com')
    r = Person("rohitash", "chandra", 37, 78, '@y.com')
    m = Person("michael", "horton", 23, 62, ' @z.com')
    z = Person("avimanyu", "sahoo", 42, 80, '@f.com')


    r.print_infor()
    p.print_infor()
    m.print_infor()
    z.print_infor()

    r.update_weight(78.1, '1 09 2021')
    r.update_weight(78.5, '3 09 2021')
    r.update_weight(78.3, '7 09 2021')

    r.print_infor()


    # define a list of Persons





