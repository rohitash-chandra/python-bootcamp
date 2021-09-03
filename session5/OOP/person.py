
#https://www.thegeekstuff.com/2019/03/python-oop-examples/


class Person:
    def __init__(self, name, age, w):
        self.name = name
        self.age = age
        self.weight = w
        # add others

    def print_infor(self):
        print(self.name, ' name')
        print(self.age, ' is age ')
        print(self.weight, ' is weight ')



if __name__ == "__main__":


    p = Person("ranjeeta kumari", 40, 55)

    r = Person("rohitash chandra", 37, 78)

    # define yours 

    
    r.print_infor()

    p.print_infor()
