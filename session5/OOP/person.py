
#https://www.thegeekstuff.com/2019/03/python-oop-examples/


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # add others

    def print_infor(self):
        print(self.name, ' name')
        print(self.age, ' is age ')



if __name__ == "__main__":
    p = Person("ranjeeta", 23)
    print(p.name)

    r = Person("rohitash chandra", 37)
    #print(r.name)

    r.print_infor()
